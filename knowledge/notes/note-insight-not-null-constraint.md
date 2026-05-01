---
id: note-insight-not-null-constraint
title: NOT NULL制約は値が空の保存を防ぐ
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-05-01
---

## Summary
- `NOT NULL` 制約は、指定したカラムに `NULL` を保存できないようにする。
- 名前やメールアドレスなど、必須項目に使う。
- Rails の `null: false` は DB 側の必須ルールとして働く。

## Tags
#database #sql #constraint #rails #要復習

## Links
- [[note-insight-database-constraint]]
- [[note-insight-database-column]]
- [[note-insight-boolean-default-false-null-false]]

## Body
`NOT NULL` 制約は、カラムに空の値を入れられないようにする制約です。アプリ上で必須入力にしていても、DB 側でも `NULL` を禁止しておくと、データの抜け漏れを防ぎやすくなります。

## Example
```ruby
add_column :users, :name, :string, null: false
```

<!-- review_log: 2026-05-02 -->
