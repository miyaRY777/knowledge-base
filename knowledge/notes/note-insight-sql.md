---
id: note-insight-sql
title: "SQLはデータベースを操作するための言語"
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
---

## Summary
- SQL は、データベースに対して取得・追加・更新・削除などを指示する言語。
- Rails では Active Record の裏側で SQL が実行される。
- SQL を理解すると、Rails の検索や関連取得の動きも追いやすくなる。

## Tags
#database #sql #rails #activerecord #要復習

## Links
- [[note-insight-database]]
- [[note-insight-dbms]]
- [[note-insight-active-record-relation]]

## Body
SQL は、データベースに「どのデータを取るか」「何を追加するか」「どの値を更新するか」を伝えるための言語です。Rails では `User.where(...)` のように Ruby で書くことが多いですが、最終的には SQL に変換されて DBMS に渡されます。

SQL の基本を押さえると、Active Record のメソッドがどのようなデータベース操作につながるのかを理解しやすくなります。

## Example
```sql
SELECT *
FROM users
WHERE email = 'sample@example.com';
```

<!-- review_log: 2026-05-02 -->
