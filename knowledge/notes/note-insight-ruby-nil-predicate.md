---
id: note-insight-ruby-nil-predicate
title: Rubyの`nil?`は値そのものがnilかを見る
created: 2026-04-08
source: [[2026-04-08_insight-ruby-nil-empty-blank-present-presence.md]]
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
`nil?` は、その値が本当に `nil` のときだけ `true` を返します。空文字や空配列のように「中身が空」の値とは区別されるため、「値が未設定か」をはっきり見たいときに向いています。

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
