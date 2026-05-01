---
id: note-insight-sql-group-by
title: GROUP BYは同じ値ごとに行をまとめるSQL句
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
---

## Summary
- `GROUP BY` は、同じ値を持つ行をグループ化する SQL 句。
- 件数や合計など、集計関数と一緒に使うことが多い。
- ユーザーごとの投稿数や月ごとの売上などを出すときに使える。

## Tags
#database #sql #aggregation #要復習

## Links
- [[note-insight-sql]]
- [[note-insight-sql-sum]]

## Body
`GROUP BY` は、行を共通する値ごとにまとめて集計するために使います。単に一覧を取得するのではなく、「ユーザーごと」「月ごと」「カテゴリごと」のように集約した結果が欲しいときに役立ちます。

## Example
```sql
SELECT user_id, COUNT(*)
FROM posts
GROUP BY user_id;
```

<!-- review_log: 2026-05-02 -->
