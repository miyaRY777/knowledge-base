---
id: note-insight-rails-blank-is-safe
title: "`blank?`が安全と言われる理由"
created: 2026-04-08
source: [[2026-04-08_insight-ruby-nil-empty-blank-present-presence.md]]
review_streak: 0
last_reviewed_on: 2026-05-26
---

## Summary
- `blank?` は `nil` にもそのまま使えるので安全です。
- 空文字だけでなく空白だけの文字列も空として判定できます。
- 「とにかく空っぽか」を見たいときに初心者にも扱いやすいです。

## Tags
#rails #activesupport #safety

## Links
- [[note-insight-rails-blank-predicate]]
- [[note-insight-ruby-empty-predicate-nil-risk]]

## Body
`blank?` が安全と言われるのは、`nil` に呼んでもエラーにならず、空文字や空白文字列もまとめて空扱いできるからです。入力値が未設定か空白だけかを細かく分けずに扱いたい場面では、条件分岐を簡潔にできます。

## Example
```ruby
value = nil

if value.blank?
  puts "空です"
end
```

このコードでは、`nil` かもしれない値を安全に空判定するために `blank?` を使っています。

## Action
- [ ] `blank?` を使いすぎない場面も整理する
