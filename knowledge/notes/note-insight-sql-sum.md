---
id: note-insight-sql-sum
title: "SUMは数値カラムの合計を計算する集計関数"
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
quiz_fail_log: []
---

## Summary
- `SUM` は、数値データの合計を求める SQL の集計関数。
- 売上合計、ポイント合計、数量合計などに使える。
- グループ別に合計したい場合は `GROUP BY` と組み合わせる。

## Tags
#database #sql #aggregation

## Links
- [[note-insight-sql]]
- [[note-insight-sql-group-by]]

## Body
`SUM` は指定した数値カラムの合計を返す集計関数です。`NULL` は無視して計算され、対象行がゼロ件の場合は `NULL` を返します（`0` ではない）。
結果が `NULL` になると困る場合は `COALESCE(SUM(price), 0)` のように `COALESCE` で代替値を指定します。
`COUNT` が行数を数えるのに対し、`SUM` は値の合計を求めるという違いを意識して使い分けます。

## Example
```sql
SELECT SUM(price)
FROM orders;
```

<!-- review_log: 2026-05-02 -->

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
