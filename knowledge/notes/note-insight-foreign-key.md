---
id: note-insight-foreign-key
title: 外部キーは別テーブルの主キーを参照して関係を表す
created: 2026-05-17
source: [[2026-05-17_insight_database-null-and-keys]]
review_streak: 0
last_reviewed_on: 2026-05-22
quiz_fail_log: []
---

## Summary
- 外部キーは、別テーブルの主キーを参照してテーブル同士の関係を表すキーです。
- `posts.user_id` が `users.id` を参照するような形で使います。
- 外部キー制約を付けると、存在しない参照先を保存する不整合を防ぎやすくなります。

## Tags
#database #sql #key #foreign-key #rails

## Links
- [[note-insight-database-key]]
- [[note-insight-primary-key]]
- [[note-insight-foreign-key-constraint]]
- [[note-insight-bigint-data-type]]

## Body
外部キーは、あるテーブルのレコードが別テーブルのどのレコードと関係しているかを示すキーです。たとえば `posts.user_id` が `users.id` を参照していれば、その投稿がどのユーザーのものかを表せます。

外部キーという列そのものと、外部キー制約は分けて考えると整理しやすいです。外部キーは関係を表す値で、外部キー制約はその値が実在する参照先だけを指すようにDB側で守るルールです。

## Example
```ruby
create_table :posts do |t|
  t.references :user, null: false, foreign_key: true
  t.string :title
end
```

この例では、`posts.user_id` が `users.id` を参照する関係を作っています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
