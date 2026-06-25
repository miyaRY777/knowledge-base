---
id: note-insight-relational-database
title: "リレーショナルデータベースはテーブル同士の関係でデータを管理する"
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-05-01
quiz_fail_log: []
---

## Summary
- リレーショナルデータベースは、データをテーブルに分け、関係を使って管理する。
- `users` と `posts` のように、別テーブルを関連付けて扱える。
- Rails の関連付けは、リレーショナルデータベースの考え方とつながる。

## Tags
#database #sql #rails #association

## Links
- [[note-insight-database-table]]
- [[note-insight-foreign-key-constraint]]
- [[note-insight-active-record-relation]]

## Body
リレーショナルデータベースは、データを1つの大きな表に詰め込むのではなく、役割ごとにテーブルへ分け、必要に応じて関係でつなぐ仕組みです。

たとえば、ユーザー情報は `users`、投稿情報は `posts` に分け、`posts.user_id` でどのユーザーの投稿かを表します。こうすると、データの重複を減らしながら関係を表現できます。

<!-- review_log: 2026-05-02 -->

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
