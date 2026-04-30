---
id: note-insight-sql-where
title: WHEREは条件に合う行だけを絞り込むSQL句
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
---

## Summary
- `WHERE` は、条件に一致する行だけを対象にするための SQL 句。
- 取得だけでなく、更新や削除の対象を絞るときにも重要。
- Rails の `where` メソッドの裏側でも SQL の `WHERE` が使われる。

## Tags
#database #sql #rails #activerecord #要復習

## Links
- [[note-insight-sql-select]]
- [[note-insight-where-not]]
- [[note-insight-active-record-relation]]

## Body
`WHERE` は、テーブルの中から条件に合う行だけを選ぶために使います。たとえば、特定のユーザーだけを取得したい場合や、公開済みの投稿だけを表示したい場合に使います。

更新や削除でも `WHERE` は重要です。条件を指定しないと、想定より広い範囲のデータを変更してしまう危険があります。

## Example
```sql
SELECT *
FROM users
WHERE id = 1;
```
