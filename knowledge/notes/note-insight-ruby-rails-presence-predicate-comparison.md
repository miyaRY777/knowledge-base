---
id: note-insight-ruby-rails-presence-predicate-comparison
title: "`nil?` `empty?` `blank?` `present?` `presence` の使い分け"
created: 2026-04-08
source: [[2026-04-08_insight-ruby-nil-empty-blank-present-presence.md]]
---

## Summary
- `nil?` は値そのものが未設定かを見る Ruby のメソッドです。
- `empty?` は中身が空かを見る Ruby のメソッドですが、`nil` には使えません。
- `blank?`、`present?`、`presence` は Rails で空判定やフォールバックを簡潔に書くために便利です。

## Tags
#ruby #rails #comparison

## Links
- [[note-insight-ruby-nil-predicate]]
- [[note-insight-ruby-empty-predicate]]
- [[note-insight-rails-blank-predicate]]
- [[note-insight-rails-present-predicate]]
- [[note-insight-rails-presence]]

## Body
これらのメソッドは似ていますが、見ている対象が違います。`nil?` は「値そのものがないか」、`empty?` は「オブジェクトの中身が空か」、`blank?` は「実質的に空っぽか」を見ます。`present?` は `blank?` の反対、`presence` は空なら `nil` に変えてフォールバックしやすくするためのものです。

## Example
```ruby
value = ""

value.nil?      # => false
value.empty?    # => true
value.blank?    # => true
value.present?  # => false
value.presence  # => nil
```

このコードでは、同じ値に対して各メソッドが何を判定するかを比較しています。

## Action
- [ ] 判定対象ごとの差分表を追加する
