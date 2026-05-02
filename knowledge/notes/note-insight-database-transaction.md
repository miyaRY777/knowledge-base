---
id: note-insight-database-transaction
title: "トランザクションは複数のデータ操作をひとまとまりで扱う仕組み"
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
---

## Summary
- トランザクションは、複数のデータ操作をまとめて成功または失敗として扱う仕組み。
- 途中で失敗したときに中途半端な状態が残るのを防ぐ。
- 注文作成と在庫更新、ポイント減算と購入履歴作成のような処理で重要。

## Tags
#database #sql #transaction #rails

## Links
- [[note-insight-database-commit-rollback]]
- [[note-insight-data-integrity-and-consistency]]

## Body
トランザクションは、複数のデータ操作を1つのまとまりとして扱う仕組みです。すべて成功したときだけ確定し、途中で失敗した場合はまとめて取り消せます。

たとえば注文処理で、在庫だけ減って注文データが作られないとデータが矛盾します。こうした「片方だけ成功」を防ぐためにトランザクションを使います。

## Example
```ruby
ActiveRecord::Base.transaction do
  user.update!(points: user.points - 100)
  order.create!(user: user, item: item)
end
```
