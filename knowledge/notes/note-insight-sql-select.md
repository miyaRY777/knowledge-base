---
id: note-insight-sql-select
title: "SELECTはデータベースから行を取得するSQL文"
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
quiz_fail_log: []
---

## Summary
- `SELECT` は、テーブルからデータを取得する SQL 文。
- 一覧表示、詳細表示、検索結果の表示などで使われる。
- 条件を付けるときは `WHERE` と組み合わせる。

## Tags
#database #sql

## Links
- [[note-insight-sql]]
- [[note-insight-sql-where]]
- [[note-insight-database-query]]

## Body
`SELECT` は、データベースに保存されているデータを取り出すための SQL 文です。テーブル全体を取得することも、必要なカラムや条件に合う行だけを取得することもできます。

Rails の `User.all` や `User.where(...)` も、裏側では `SELECT` 系の SQL として実行されます。

## Example
```sql
SELECT *
FROM posts;
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
