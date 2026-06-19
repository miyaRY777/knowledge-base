---
id: note-insight-activerecord-eager-load
title: "`eager_load`とは？"
created: 2026-04-19
source: [[2026-04-19_insight_rails-and-tailwind-terms.md]]
quiz_fail_log: []
---

## Summary
- `eager_load` は、関連先を `LEFT OUTER JOIN` でまとめて読み込む Active Record のメソッドです。
- 関連先の条件や並び替えを SQL 上で扱いたいときに向いています。
- 関連を先に読んでおくことで、ループ中の追加クエリを減らせます。

## Tags
#rails #activerecord #n-plus-one #sql

## Links
- [[note-insight-fallback-url]]

## Body
`eager_load` は、関連テーブルも含めて 1 回の JOIN クエリで取得したいときに使う Active Record のメソッドです。`LEFT OUTER JOIN` を使って親と関連先をまとめて読み込むため、関連先カラムを使った条件や並び替えを扱いやすくなります。

関連を先に読んでおくことで N+1 を減らせますが、JOIN で結果が広がるぶん、大きなデータでは重くなることがあります。

## Example
```ruby
memberships = RoomMembership.eager_load(room: :share_link)

memberships.each do |membership|
  puts membership.room.share_link&.token
end
```

このコードでは、`room` と `share_link` を先にまとめて読み込むことで、繰り返し処理中の追加クエリを減らしています。

## Action
- [ ] `includes` と `preload` との違いを比較ノートにまとめる
