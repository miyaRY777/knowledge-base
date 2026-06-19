---
id: note-insight-b-tree-index
title: B-treeインデックスは範囲検索や並び替えにも使いやすい標準的なインデックス
created: 2026-05-21
source: [[2026-05-21_insight_database-index-types.md]]
review_streak: 0
last_reviewed_on: 2026-05-22
quiz_fail_log: []
---

## Summary
- B-tree インデックスは、値を順序づけて管理する標準的なインデックスです。
- `=` の検索だけでなく、大小比較、`BETWEEN`、`ORDER BY` にも向いています。
- 多くの DB でよく使われますが、細かな挙動は DBMS によって異なります。

## Tags
#database #sql #index #btree #performance

## Links
- [[note-insight-database-index-types]]
- [[note-insight-database-index]]
- [[note-insight-sql-where]]

## Body
B-tree インデックスは、値の並び順を利用して目的の行へたどり着きやすくするインデックスです。値が順序を持って管理されるため、完全一致だけでなく、「これより大きい」「この範囲内」「この順序で並べる」といったクエリでも使いやすい特徴があります。

たとえば `email` の検索、作成日の範囲指定、価格順の並び替えなどで候補になります。データベースで標準的に使われることが多い一方、実際にどの条件で使われるかは DBMS と実行計画に依存します。

## Example
```sql
CREATE INDEX index_users_on_email ON users (email);
```
