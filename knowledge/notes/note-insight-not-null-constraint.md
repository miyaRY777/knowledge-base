---
id: note-insight-not-null-constraint
title: "NOT NULL制約は値が空の保存を防ぐ"
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-05-01
quiz_fail_log: []
---

## Summary
- `NOT NULL` 制約は、指定したカラムに `NULL` を保存できないようにする。
- 名前やメールアドレスなど、必須項目に使う。
- Rails の `null: false` は DB 側の必須ルールとして働く。

## Tags
#database #sql #constraint #rails

## Links
- [[note-insight-database-constraint]]
- [[note-insight-database-column]]
- [[note-insight-null-value]]
- [[note-insight-boolean-default-false-null-false]]

## Body
`NOT NULL` 制約はDBレベルで `NULL` の保存を禁止する制約で、アプリ側のバリデーションとは独立して機能します。
アプリ側で `validates :name, presence: true` があっても、DB直接操作やマイグレーションのバグで `NULL` が入り込む可能性があるため、重要カラムにはDB制約も合わせて設けるのが二重防御の基本です。
`null: false` のカラムに `NULL` を挿入しようとすると `ActiveRecord::NotNullViolation` 例外が発生します。

## Example
```ruby
add_column :users, :name, :string, null: false
```

<!-- review_log: 2026-05-02 -->
