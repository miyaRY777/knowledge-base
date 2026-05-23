---
id: note-insight-exclusive-lock
title: 排他ロックは対象データを自分だけが変更できる状態にする
created: 2026-05-23
source: [[2026-05-23_insight_database-lock-types.md]]
---

## Summary
- 排他ロックは、ある処理が対象データを更新している間、他の処理による変更を防ぐ仕組みです。
- 同時更新による上書きや値のズレを防ぎたい場面で使います。
- 残高、在庫数、ポイントなど、整合性が重要な更新で特に役立ちます。

## Tags
#database #sql #transaction #lock #exclusive-lock #concurrency #rails

## Links
- [[note-insight-database-lock-types]]
- [[note-insight-database-locking]]
- [[note-insight-isolation]]
- [[note-insight-database-transaction]]

## Body
排他ロックは、対象データを「この処理だけが変更できる状態」にするロックです。あるトランザクションが更新対象をロックしている間、他のトランザクションは同じデータを変更できず、待たされるか失敗します。

この仕組みは、同時更新で値が壊れやすい処理に向いています。たとえば残高から100円を引く処理や、在庫を1つ減らす処理では、複数の更新が同時に走ると計算結果がずれる可能性があります。排他ロックを使うと、更新順序を制御して不整合を防ぎやすくなります。

## Example
```ruby
User.transaction do
  user = User.lock.find(1)
  user.points -= 100
  user.save!
end
```
