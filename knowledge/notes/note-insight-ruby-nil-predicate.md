---
id: note-insight-ruby-nil-predicate
title: "Rubyの`nil?`は値そのものがnilかを見る"
created: 2026-04-08
source: [[2026-04-08_insight-ruby-nil-empty-blank-present-presence.md]]
review_streak: 0
last_reviewed_on: 2026-05-26
quiz_fail_log: []
---

## Summary
- `nil?` は値そのものが `nil` かどうかだけを判定するメソッドです。
- 空文字 `""` や空配列 `[]` は `nil` ではないので `false` になります。
- 値そのものが存在しないかを明確に確認したい場面で使います。

## Tags
#ruby #language #predicate

## Links
- [[note-insight-ruby-empty-predicate]]
- [[note-insight-rails-blank-predicate]]

## Body
`nil?` は Ruby のすべてのオブジェクトに定義されたメソッドで、`nil` のときだけ `true` を返します。
空文字 `""` や空配列 `[]` は「中身が空」ですが `nil` ではないので `false` です。「値そのものが存在しないか」を確認したい場面で使い分けます。
Rails では `blank?` が nil・空文字・空白文字・空コレクションを一括でカバーするため、「空かどうかの判定」には `blank?`/`present?` を使い、「未設定かどうかの判定」には `nil?` を使うと意図が明確になります。

## Example
```ruby
value = nil

value.nil?   # => true
"".nil?      # => false
[].nil?      # => false
```

このコードでは、値そのものが `nil` かどうかを確認するために `nil?` を使っています。

## Action
- [ ] `nil` と空値の違いを説明するときの例を増やす
