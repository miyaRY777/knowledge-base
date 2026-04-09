# frozen_string_literal: true

require "minitest/autorun"
require "tempfile"
require_relative "../scripts/review_tag_sync"

class ReviewTagSyncTest < Minitest::Test
  def with_note(content)
    Tempfile.create(["note", ".md"]) do |file|
      file.write(content)
      file.flush
      yield file.path
    end
  end

  def read_note(path)
    File.read(path)
  end

  def test_wrong_adds_review_tag_and_review_log_for_note_without_existing_log
    with_note(<<~NOTE) do |path|
      ---
      id: note-sample
      title: sample
      created: 2026-04-09
      ---

      ## Tags
      #rails #predicate
      NOTE
      result = ReviewTagSync::Runner.new(note_path: path, action: :wrong, date: "2026-04-09").run

      assert_equal 1, result.added_tags
      assert_equal 0, result.removed_tags
      assert_equal ["2026-04-09"], result.added_log_dates
      assert_includes read_note(path), "#rails #predicate #要復習"
      assert_includes read_note(path), "<!-- review_log: 2026-04-09 -->"
    end
  end

  def test_correct_does_not_remove_same_day_review_log
    with_note(<<~NOTE) do |path|
      ---
      id: note-sample
      title: sample
      created: 2026-04-09
      ---

      ## Tags
      #rails #要復習

      <!-- review_log: 2026-04-09 -->
      NOTE
      result = ReviewTagSync::Runner.new(note_path: path, action: :correct, date: "2026-04-09").run

      assert_equal 0, result.removed_tags
      assert_equal [], result.removed_log_dates
      assert_includes read_note(path), "#rails #要復習"
      assert_includes read_note(path), "<!-- review_log: 2026-04-09 -->"
    end
  end

  def test_correct_removes_oldest_prior_log_and_one_review_tag
    with_note(<<~NOTE) do |path|
      ---
      id: note-sample
      title: sample
      created: 2026-04-09
      ---

      ## Tags
      #rails #要復習 #要復習 #要復習

      <!-- review_log: 2026-04-07,2026-04-08,2026-04-09 -->
      NOTE
      result = ReviewTagSync::Runner.new(note_path: path, action: :correct, date: "2026-04-10").run

      assert_equal 1, result.removed_tags
      assert_equal ["2026-04-07"], result.removed_log_dates
      refute_includes read_note(path), "#rails #要復習 #要復習 #要復習"
      assert_includes read_note(path), "#rails #要復習 #要復習"
      assert_includes read_note(path), "<!-- review_log: 2026-04-08,2026-04-09 -->"
    end
  end

  def test_check_detects_mismatch_between_tag_count_and_review_log_count
    with_note(<<~NOTE) do |path|
      ---
      id: note-sample
      title: sample
      created: 2026-04-09
      ---

      ## Tags
      #rails #要復習 #要復習

      <!-- review_log: 2026-04-09 -->
      NOTE
      error = assert_raises(ReviewTagSync::MismatchError) do
        ReviewTagSync::Runner.new(note_path: path, action: :check, date: "2026-04-09").run
      end

      assert_includes error.message, "#要復習"
      assert_includes error.message, "review_log"
    end
  end
end
