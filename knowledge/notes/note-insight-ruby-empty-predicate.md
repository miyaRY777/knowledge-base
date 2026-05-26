---
id: note-insight-ruby-empty-predicate
title: "Rubyの`empty?`は中身が空かを見る"
created: 2026-04-08
source: [[2026-04-08_insight-ruby-nil-empty-blank-present-presence.md]]
review_streak: 0
last_reviewed_on: 2026-05-26
---

## Summary
- `empty?` は文字列、配列、ハッシュなどの中身が空かどうかを判定します。
- `nil` には使えないため、呼び出し前に対象の型や値の有無に注意が必要です。
- 「オブジェクトはあるが中身がない」ことを見たいときに使います。

## Tags
#ruby #language #predicate

## Links
- [[note-insight-ruby-empty-predicate-nil-risk]]
- [[note-insight-ruby-nil-predicate]]

## Body
`empty?` は、文字列や配列やハッシュのように中身を持つオブジェクトに対して、その中身が空かどうかを確認するメソッドです。値が存在する前提で使うメソッドなので、`nil` の可能性がある値にはそのまま呼ばない方が安全です。

## Example
```ruby
"".empty?      # => true
"abc".empty?   # => false
[].empty?      # => true
{}.empty?      # => true
```

このコードでは、文字列や配列やハッシュの中身が空かどうかを確認するために `empty?` を使っています。

## Action
- [ ] `size.zero?` との使い分けも整理する
