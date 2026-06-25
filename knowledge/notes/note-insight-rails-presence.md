---
id: note-insight-rails-presence
title: "Railsの`presence`は空ならnilにできる"
created: 2026-04-08
source: [[2026-04-08_insight-ruby-nil-empty-blank-present-presence.md]]
review_streak: 0
last_reviewed_on: 2026-05-26
quiz_fail_log: []
---

## Summary
- `presence` は値が空でなければその値を返し、空なら `nil` を返します。
- フォールバック値を使いたい場面で短く書けます。
- `present?` と `||` を組み合わせるより簡潔になることがあります。

## Tags
#rails #activesupport #fallback

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


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] フォーム入力以外の活用例も追加する
