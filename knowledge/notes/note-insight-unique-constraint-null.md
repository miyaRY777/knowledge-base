---
id: note-insight-unique-constraint-null
title: "UNIQUE制約でNULLが重複扱いされない理由"
created: 2026-03-30
source: [[2026-03-30_insight_rails-study.md]]
quiz_fail_log: []
---

## Summary
- NULLは「値がない」ではなく「値が不明」という意味を持つ
- 不明同士を比較しても「等しい」とは判定できないため、UNIQUE制約の検査対象外になる
- PostgreSQL のデフォルトでは、NULL は複数行に入れても UNIQUE 違反にならない。
- ただし `NULLS NOT DISTINCT` を使うと、NULL 同士を重複扱いにできる。

## Tags
#database #postgresql #sql

## Links
- [[note-insight-idempotent]]
- [[note-insight-null-value]]
- [[note-insight-slug]]

## Body
SQLにおけるNULLは「未知の値」であり、NULL = NULL の結果は TRUE ではなく UNKNOWN になる。UNIQUE制約は「同じ値の重複を禁止する」仕組みだが、PostgreSQL のデフォルトでは NULL 同士は等しい値として扱われないため、UNIQUE制約のついたカラムにNULLを複数回INSERTしてもエラーにならない。任意入力のカラムにUNIQUE制約をかける時は、この挙動を理解しておく必要がある。

PostgreSQL では `NULLS NOT DISTINCT` を指定すると、NULL 同士を等しいものとして扱い、複数の NULL を UNIQUE 違反にできる。


## Example
```sql
CREATE TABLE users (email TEXT UNIQUE);
INSERT INTO users (email) VALUES (NULL);
INSERT INTO users (email) VALUES (NULL); -- エラーにならない
```

このコードでは、UNIQUE 制約があっても `NULL` は重複扱いされず、複数回 INSERT できることを示しています。

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
