---
id: note-insight-ruby-empty-predicate-nil-risk
title: "`empty?`はnilに使うとNoMethodErrorになる"
created: 2026-04-08
source: [[2026-04-08_insight-ruby-nil-empty-blank-present-presence.md]]
review_streak: 1
last_reviewed_on: 2026-05-26
---

## Summary
- `empty?` は `nil` に対して呼ぶと `NoMethodError` になります。
- `nil` の可能性がある値にそのまま使うのは危険です。
- Rails では `blank?` を使うと安全に空判定しやすくなります。

## Tags
#ruby #rails #error-handling #要復習

## Links
- [[note-insight-ruby-check-nil-before-empty]]
- [[note-insight-rails-blank-is-safe]]

## Body
`empty?` は String・Array・Hash など各クラスで定義されたメソッドで、`nil` には定義されていないため `NoMethodError` が発生します。
対策は3つあります：①事前に `nil` チェックをする、②`&.empty?`（safe navigation operator）を使う、③Rails であれば `blank?` を使う（`nil` にも安全）。
外部からの入力や検索結果など「`nil` が返ってくる可能性がある変数」に `empty?` を直接使うのは危険なパターンとして覚えておくと良いです。

## Example
```ruby
value = nil

value.empty? # NoMethodError
```

このコードでは、`nil` に対して `empty?` を呼ぶとエラーになることを確認しています。

## Action
- [ ] `NoMethodError` が起きやすい場面の例を足す
