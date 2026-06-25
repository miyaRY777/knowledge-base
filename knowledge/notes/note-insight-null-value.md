---
id: note-insight-null-value
title: NULLは値がないことを表す特別な値
created: 2026-05-17
source: [[2026-05-17_insight_database-null-and-keys]]
review_streak: 0
last_reviewed_on: 2026-05-22
quiz_fail_log: []
---

## Summary
- `NULL` は、値がない、不明、または未入力であることを表す特別な値です。
- `0` や空文字 `""` とは別物です。
- SQL で `NULL` を調べるときは、`=` ではなく `IS NULL` を使います。

## Tags
#database #sql #null

## Links
- [[note-insight-not-null-constraint]]
- [[note-insight-unique-constraint-null]]
- [[note-insight-database-column]]

## Body
`NULL` は、データベースで「値が入っていない」「値が不明」「まだ入力されていない」といった状態を表す特別な値です。数値の `0` や空文字 `""` のように、何かしらの値が入っている状態とは区別されます。

SQL では `NULL` は通常の値と同じようには比較できません。そのため、`nickname = NULL` ではなく `nickname IS NULL` のように判定します。

## Example
```sql
SELECT * FROM users WHERE nickname IS NULL;
```

この例では、`nickname` に値が入っていないユーザーを探しています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] `NULL` と三値論理の関係を整理する
