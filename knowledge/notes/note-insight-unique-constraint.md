---
id: note-insight-unique-constraint
title: 一意性制約は同じ値の重複保存を防ぐ
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-05-01
---

## Summary
- 一意性制約は、特定のカラムに同じ値を重複して保存できないようにする。
- メールアドレス、ユーザー名、slug などで使われる。
- `NULL` の扱いには注意が必要。

## Tags
#database #sql #constraint #rails #要復習

## Links
- [[note-insight-database-constraint]]
- [[note-insight-unique-constraint-null]]
- [[note-insight-slug]]

## Body
一意性制約は、同じ値を複数レコードに保存できないようにするためのルールです。ユーザーのメールアドレスのように、システム内で重複してほしくない値に使います。

Rails では `unique: true` のインデックスとして設定することが多いです。ただし、`NULL` を含む場合の扱いは DB の仕様を確認する必要があります。

## Example
```ruby
add_index :users, :email, unique: true
```

<!-- review_log: 2026-05-02 -->
