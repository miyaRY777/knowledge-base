---
id: note-insight-primary-key
title: 主キーはテーブル内の1件を一意に識別するキー
created: 2026-05-17
source: [[2026-05-17_insight_database-null-and-keys]]
review_streak: 0
last_reviewed_on: 2026-06-18
quiz_fail_log: []
---

## Summary
- 主キーは、テーブル内の1件のレコードを一意に識別するためのキーです。
- 主キーには重複する値を入れられず、`NULL` も入れられません。
- Rails では、多くの場合 `id` カラムが主キーとして使われます。

## Tags
#database #sql #key #primary-key #rails

## Links
- [[note-insight-database-key]]
- [[note-insight-null-value]]
- [[note-insight-foreign-key]]
- [[note-insight-bigint-data-type]]

## Body
主キーは、そのテーブルの中で各レコードを一意に見分けるためのキーです。同じ値が複数行に入ると1件を特定できなくなるため、重複は許されません。また、対象レコードを必ず識別できる必要があるため、`NULL` も許されません。

Rails では、多くのテーブルで `id` カラムが主キーとして自動的に使われます。外部キーは、この主キーを参照して別テーブルとの関係を表します。

## Example
```sql
CREATE TABLE users (
  id bigserial PRIMARY KEY,
  name varchar(255)
);
```

この例では、`users.id` が各ユーザーを一意に識別します。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
