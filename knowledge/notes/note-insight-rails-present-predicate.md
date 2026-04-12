---
id: note-insight-rails-present-predicate
title: Railsの`present?`は中身があるかを見る
created: 2026-04-08
source: [[2026-04-08_insight-ruby-nil-empty-blank-present-presence.md]]
---

## Summary
- `present?` は `blank?` の反対を表す Rails のメソッドです。
- 空ではないなら処理したい、という条件を自然に書けます。
- `blank?` を否定するより読みやすくなることがあります。

## Tags
#rails #activesupport #predicate

## Links
- [[note-insight-rails-blank-predicate]]
- [[note-insight-rails-presence]]

## Body
`present?` は `blank?` が `false` のときに `true` を返します。「空ではないなら使う」という条件分岐を表現しやすく、ビューやコントローラでよく使われます。

## Example
```ruby
name = "Ruby"

name.present?   # => true
"".present?     # => false
nil.present?    # => false
```

このコードでは、値が空ではなく、使える中身を持っているかどうかを確認するために `present?` を使っています。

## Action
- [ ] `if value.present?` が読みやすい場面の例を増やす
