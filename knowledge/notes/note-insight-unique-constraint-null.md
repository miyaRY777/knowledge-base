---
id: note-insight-unique-constraint-null
title: UNIQUE制約でNULLが重複扱いされない理由
created: 2026-03-30
source: [[2026-03-30_insight_rails-study.md]]
---

## Summary（3行）
- NULLは「値がない」ではなく「値が不明」という意味を持つ
- 不明同士を比較しても「等しい」とは判定できないため、UNIQUE制約の検査対象外になる
- 結果としてNULLは複数行に入れてもUNIQUE違反にならない

## Tags
#database #postgresql #sql

## Links
- [[note-insight-idempotent]]
- [[note-insight-slug]]

## Body
SQLにおけるNULLは「未知の値」であり、NULL = NULL の結果は TRUE ではなく UNKNOWN になる。UNIQUE制約は「同じ値の重複を禁止する」仕組みだが、NULLは比較自体ができないため制約の対象外となる。PostgreSQLではこの標準SQL仕様に従っており、UNIQUE制約のついたカラムにNULLを複数回INSERTしてもエラーにならない。任意入力のカラムにUNIQUE制約をかける時は、この挙動を理解しておく必要がある。


## Example
```sql
CREATE TABLE users (email TEXT UNIQUE);
INSERT INTO users (email) VALUES (NULL);
INSERT INTO users (email) VALUES (NULL); -- エラーにならない
```

このコードでは、UNIQUE 制約があっても `NULL` は重複扱いされず、複数回 INSERT できることを示しています。
