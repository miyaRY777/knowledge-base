---
id: note-insight-hash-index
title: ハッシュインデックスは完全一致検索に向いたインデックス
created: 2026-05-21
source: [[2026-05-21_insight_database-index-types.md]]
review_streak: 0
last_reviewed_on: 2026-06-18
quiz_fail_log: []
---

## Summary
- ハッシュインデックスは、値から作ったハッシュ値を手がかりに探すインデックスです。
- `email = ...` のような完全一致検索に向いています。
- 値の順序を扱いにくいため、範囲検索や並び替えには向きません。

## Tags
#database #sql #index #hash-index #performance

## Links
- [[note-insight-database-index-types]]
- [[note-insight-database-index]]
- [[note-insight-sql-where]]
- [[note-insight-b-tree-index]]

## Body
ハッシュインデックスは、対象の値をハッシュ値に変換し、その結果を使って該当データを探すインデックスです。等しいかどうかを調べる検索では効率よく使える一方、値の大小や順序を利用する検索には向きません。

そのため、`email = 'example@example.com'` のような完全一致検索では候補になりますが、`BETWEEN` や `ORDER BY` のように順序が必要なクエリでは B-tree インデックスのほうが適している場合があります。利用可否や制約は DBMS によって異なります。

## Example
```sql
CREATE INDEX index_users_on_email_hash ON users USING hash (email);
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
