# frozen_string_literal: true

require "date"
require "optparse"

module ReviewTagSync
  class Error < StandardError; end
  class MismatchError < Error; end
  class ParseError < Error; end

  Result = Struct.new(
    :note_id,
    :note_path,
    :added_tags,
    :removed_tags,
    :added_log_dates,
    :removed_log_dates,
    :content,
    keyword_init: true
  )

  class Runner
    REVIEW_TAG = "#要復習"
    REVIEW_LOG_PATTERN = /<!--\s*review_log:\s*([^>]*)-->/

    def initialize(note_path:, action:, date:, dry_run: false)
      @note_path = note_path
      @action = action.to_sym
      @date = Date.iso8601(date).iso8601
      @dry_run = dry_run
    end

    def run
      note = NoteFile.load(@note_path)
      note.validate_consistency!

      result = case @action
               when :wrong
                 note.apply_wrong(@date)
               when :correct
                 note.apply_correct(@date)
               when :check
                 note.check(@date)
               else
                 raise Error, "Unknown action: #{@action}"
               end

      note.save! unless @dry_run || @action == :check
      result
    end
  end

  class NoteFile
    attr_reader :path

    def self.load(path)
      new(path, File.read(path))
    end

    def initialize(path, content)
      @path = path
      @content = content
    end

    def validate_consistency!
      return if review_tag_count == review_log_dates.length
      raise MismatchError, "#要復習 count (#{review_tag_count}) does not match review_log count (#{review_log_dates.length}) in #{path}"
    end

    def check(_date)
      Result.new(
        note_id: note_id,
        note_path: path,
        added_tags: 0,
        removed_tags: 0,
        added_log_dates: [],
        removed_log_dates: [],
        content: @content
      )
    end

    def apply_wrong(date)
      tags = tags_line
      tags << " #{Runner::REVIEW_TAG}"
      self.tags_line = tags

      dates = review_log_dates
      dates << date
      self.review_log_dates = dates

      Result.new(
        note_id: note_id,
        note_path: path,
        added_tags: 1,
        removed_tags: 0,
        added_log_dates: [date],
        removed_log_dates: [],
        content: @content
      )
    end

    def apply_correct(date)
      removable = review_log_dates.find { |logged_date| logged_date < date }
      return check(date) unless removable

      tags = tags_line.sub(/\s*#{Regexp.escape(Runner::REVIEW_TAG)}/, "")
      self.tags_line = normalize_spaces(tags)

      dates = review_log_dates.dup
      dates.delete_at(dates.index(removable))
      self.review_log_dates = dates

      Result.new(
        note_id: note_id,
        note_path: path,
        added_tags: 0,
        removed_tags: 1,
        added_log_dates: [],
        removed_log_dates: [removable],
        content: @content
      )
    end

    def save!
      File.write(path, @content)
    end

    private

    def note_id
      @note_id ||= @content[/^id:\s*(.+)$/, 1]&.strip || File.basename(path, ".md")
    end

    def tags_line
      idx = tags_line_index
      @content.lines[idx].chomp
    end

    def tags_line=(value)
      lines = @content.lines
      lines[tags_line_index] = "#{value}\n"
      @content = lines.join
    end

    def tags_line_index
      heading_index = @content.lines.find_index { |line| line.strip == "## Tags" }
      raise ParseError, "## Tags section not found in #{path}" unless heading_index

      idx = heading_index + 1
      lines = @content.lines
      idx += 1 while idx < lines.length && lines[idx].strip.empty?
      raise ParseError, "Tags line not found in #{path}" if idx >= lines.length

      idx
    end

    def review_tag_count
      tags_line.scan(Runner::REVIEW_TAG).length
    end

    def review_log_dates
      match = @content.match(Runner::REVIEW_LOG_PATTERN)
      return [] unless match

      raw = match[1].strip
      return [] if raw.empty?

      raw.split(",").map(&:strip)
    end

    def review_log_dates=(dates)
      stripped = remove_review_log_block(@content)
      @content = stripped.sub(/\s+\z/, "\n")
      return if dates.empty?

      @content = @content.sub(/\n*\z/, "\n\n") + "<!-- review_log: #{dates.join(',')} -->\n"
    end

    def remove_review_log_block(content)
      content.sub(/\n*<!--\s*review_log:\s*[^>]*-->\s*\z/m, "\n")
    end

    def normalize_spaces(text)
      text.split.join(" ")
    end
  end

  class CLI
    def self.run(argv)
      options = { dry_run: false }

      parser = OptionParser.new do |opts|
        opts.banner = "Usage: review_tag_sync.rb --note PATH --action wrong|correct|check --date YYYY-MM-DD [--dry-run]"
        opts.on("--note PATH") { |v| options[:note] = v }
        opts.on("--action ACTION") { |v| options[:action] = v }
        opts.on("--date DATE") { |v| options[:date] = v }
        opts.on("--dry-run") { options[:dry_run] = true }
      end

      parser.parse!(argv)
      missing = %i[note action date].reject { |key| options[key] }
      raise OptionParser::MissingArgument, missing.join(", ") unless missing.empty?

      result = Runner.new(
        note_path: options[:note],
        action: options[:action],
        date: options[:date],
        dry_run: options[:dry_run]
      ).run

      puts "更新したノート: [[#{result.note_id}]]"
      puts format_change("追加", result.added_tags, result.added_log_dates)
      puts format_change("削除", result.removed_tags, result.removed_log_dates)
      0
    rescue StandardError => e
      warn e.message
      1
    end

    def self.format_change(label, tag_count, log_dates)
      if tag_count.zero?
        "#{label}: なし"
      else
        "#{label}: #要復習 を #{tag_count} 個 / review_log #{label == '追加' ? 'に' : 'から'} #{log_dates.join(',')} を #{log_dates.length} 件"
      end
    end
  end
end

if $PROGRAM_NAME == __FILE__
  exit ReviewTagSync::CLI.run(ARGV)
end
