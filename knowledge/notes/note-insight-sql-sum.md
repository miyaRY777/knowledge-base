---
id: note-insight-sql-sum
title: SUMは数値カラムの合計を計算する集計関数
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
---

## Summary
- `SUM` は、数値データの合計を求める SQL の集計関数。
- 売上合計、ポイント合計、数量合計などに使える。
- グループ別に合計したい場合は `GROUP BY` と組み合わせる。

## Tags
#database #sql #aggregation #要復習

## Links
- [[note-insight-sql]]
- [[note-insight-sql-group-by]]

## Body
`SUM` は、指定した数値カラムの合計を計算する関数です。単純な合計だけでなく、`GROUP BY` と合わせることでユーザー別や月別の合計も求められます。

## Example
```sql
SELECT SUM(price)
FROM orders;
```
