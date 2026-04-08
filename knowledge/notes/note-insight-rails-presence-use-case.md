---
id: note-insight-rails-presence-use-case
title: `presence`は空なら別の値を使いたいときに便利
created: 2026-04-08
source: [[2026-04-08_insight-ruby-nil-empty-blank-present-presence.md]]
---

## Summary
- `presence` は値が空なら `nil` を返すので、代替値と組み合わせやすいです。
- フォーム入力や表示名のデフォルト設定でよく使われます。
- 分岐を増やさずにフォールバックを書けるのが利点です。

## Tags
#rails #activesupport #fallback

## Links
- [[note-insight-rails-presence]]
- [[note-insight-rails-present-predicate]]

## Body
`presence` は「値があれば使い、空なら別の値を使う」という場面で便利です。`if value.present?` のような分岐を書かなくても、`||` と組み合わせて自然にデフォルト値へ流せます。

## Example
```ruby
nickname = params[:nickname].presence || "no-name"
```

このコードでは、入力されたニックネームが空なら `"no-name"` を使うために `presence` を使っています。

## Action
- [ ] `presence_in` との違いも後で確認する
