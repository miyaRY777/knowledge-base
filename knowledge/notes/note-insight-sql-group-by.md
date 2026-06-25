---
id: note-insight-sql-group-by
title: "GROUP BYは同じ値ごとに行をまとめるSQL句"
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
quiz_fail_log: []
---

## Summary
- `GROUP BY` は、同じ値を持つ行をグループ化する SQL 句。
- 件数や合計など、集計関数と一緒に使うことが多い。
- ユーザーごとの投稿数や月ごとの売上などを出すときに使える。

## Tags
#database #sql #aggregation

## Links
- [[note-insight-sql]]
- [[note-insight-sql-sum]]

## Body
`GROUP BY` でグループ化すると、`SELECT` に書けるのは「グループ化した列」と「集計関数（COUNT, SUM など）」だけになります。グループ化していない列を SELECT に書くとエラーになります。
グループ化後に条件を絞り込みたい場合は `WHERE` ではなく `HAVING` を使います（`HAVING COUNT(*) > 5` のように集計結果に対して条件を付ける）。
`WHERE` はグループ化前の行を絞り込み、`HAVING` はグループ化後の集計結果を絞り込むという役割の違いを押さえておくことが重要です。

## Example
```sql
SELECT user_id, COUNT(*)
FROM posts
GROUP BY user_id;
```

<!-- review_log: 2026-05-02 -->

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
