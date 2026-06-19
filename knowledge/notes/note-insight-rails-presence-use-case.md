---
id: note-insight-rails-presence-use-case
title: "`presence`は空なら別の値を使いたいときに便利"
created: 2026-04-08
source: [[2026-04-08_insight-ruby-nil-empty-blank-present-presence.md]]
review_streak: 1
last_reviewed_on: 2026-06-18
quiz_fail_log: []
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
`presence` は値が `blank?` なら `nil` を返し、そうでなければ値そのものを返します。
`params[:nickname].presence || "no-name"` のように `||` と組み合わせると、`if present?` の分岐を書かずにデフォルト値へのフォールバックが1行で書けます。
`presence_in(list)` を使うと「許可リストに含まれる値だけ使い、それ以外はnil」という絞り込みも同じ感覚で書けます。

## Example
```ruby
nickname = params[:nickname].presence || "no-name"
```

このコードでは、入力されたニックネームが空なら `"no-name"` を使うために `presence` を使っています。

## Action
- [ ] `presence_in` との違いも後で確認する
