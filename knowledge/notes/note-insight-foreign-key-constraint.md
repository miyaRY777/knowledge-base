---
id: note-insight-foreign-key-constraint
title: "外部キー制約は存在する関連先だけを参照させる"
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-05-01
---

## Summary
- 外部キー制約は、別テーブルに存在するデータだけを参照できるようにする。
- 存在しないユーザーに投稿が紐づくような不整合を防ぐ。
- テーブル同士の関係を DB 側で守るために使う。

## Tags
#database #sql #constraint #rails #要復習

## Links
- [[note-insight-database-constraint]]
- [[note-insight-relational-database]]
- [[note-insight-dependent-restrict-with-error]]

## Body
外部キー制約は、あるテーブルの値が、別テーブルの実在するレコードを参照していることを保証する仕組みです。たとえば `posts.user_id` が `users.id` を参照する場合、存在しないユーザーIDの投稿を保存できないようにできます。

これにより、アプリ側の処理漏れがあっても、関係の壊れたデータが残りにくくなります。

## Example
```ruby
add_foreign_key :posts, :users
```

<!-- review_log: 2026-05-02 -->
