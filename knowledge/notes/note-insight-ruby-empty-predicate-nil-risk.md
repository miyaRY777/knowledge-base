---
id: note-insight-ruby-empty-predicate-nil-risk
title: "`empty?`はnilに使うとNoMethodErrorになる"
created: 2026-04-08
source: [[2026-04-08_insight-ruby-nil-empty-blank-present-presence.md]]
---

## Summary
- `empty?` は `nil` に対して呼ぶと `NoMethodError` になります。
- `nil` の可能性がある値にそのまま使うのは危険です。
- Rails では `blank?` を使うと安全に空判定しやすくなります。

## Tags
#ruby #rails #error-handling

## Links
- [[note-insight-ruby-check-nil-before-empty]]
- [[note-insight-rails-blank-is-safe]]

## Body
`empty?` は便利ですが、`nil` に対しては定義されていないためエラーになります。値が未設定かもしれない入力や検索結果に対して `empty?` を直接呼ぶと、意図しない例外の原因になります。

## Example
```ruby
value = nil

value.empty? # NoMethodError
```

このコードでは、`nil` に対して `empty?` を呼ぶとエラーになることを確認しています。

## Action
- [ ] `NoMethodError` が起きやすい場面の例を足す
