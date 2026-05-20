---
id: note-insight-atomicity
title: Atomicityはトランザクションを全部成功か全部失敗として扱う性質
created: 2026-05-20
source: [[2026-05-20_insight_acid-properties.md]]
---

## Summary
- Atomicity は、トランザクション内の処理を1つのまとまりとして扱う性質です。
- 途中で失敗した場合、一部だけ保存せず開始前の状態へ戻します。
- Rails の `transaction` は、複数の更新をまとめて成功または失敗にしたい場面で使います。

## Tags
#database #sql #transaction #acid #atomicity #rails

## Links
- [[note-insight-acid-properties]]
- [[note-insight-database-transaction]]
- [[note-insight-database-commit-rollback]]

## Body
Atomicity は、トランザクション内の複数の処理を「分割できない1つの処理」として扱う性質です。すべての処理が成功したときだけ変更を確定し、途中でエラーが起きた場合は、すでに実行した変更も取り消します。

たとえば購入処理で、ポイントだけ減って在庫更新が失敗すると、ユーザーにも商品管理にも不自然な状態が残ります。こうした片方だけ成功した状態を防ぐために、関連する更新を1つのトランザクションにまとめます。

## Example
```ruby
ActiveRecord::Base.transaction do
  user.update!(points: user.points - 100)
  item.update!(stock: item.stock - 1)
end
```
