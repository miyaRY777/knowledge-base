---
id: note-insight-rails-presence
title: Railsの`presence`は空ならnilにできる
created: 2026-04-08
source: [[2026-04-08_insight-ruby-nil-empty-blank-present-presence.md]]
---

## Summary
- `presence` は値が空でなければその値を返し、空なら `nil` を返します。
- フォールバック値を使いたい場面で短く書けます。
- `present?` と `||` を組み合わせるより簡潔になることがあります。

## Tags
#rails #activesupport #fallback #要復習 #要復習

## Links
- [[note-insight-rails-presence-use-case]]
- [[note-insight-rails-present-predicate]]

## Body
`presence` は「使える値ならそのまま使い、空なら `nil` にする」という意図をそのまま表せるメソッドです。空文字をそのまま通したくないときに特に便利で、デフォルト値との組み合わせがしやすくなります。

## Example
```ruby
label = ""

label.presence || "この部屋の趣味" # => "この部屋の趣味"
```

このコードでは、`label` が空なら代わりの文字を使うために `presence` を使っています。

## Action
- [ ] フォーム入力以外の活用例も追加する

<!-- review_log: 2026-04-09,2026-04-09 -->
