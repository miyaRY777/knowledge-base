---
id: note-insight-database-table
title: テーブルは同じ種類のデータを行と列で保存する場所
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
---

## Summary
- テーブルは、同じ種類のデータを表形式で保存する単位。
- Rails では `users` や `posts` のようにモデルに対応するテーブルを作ることが多い。
- テーブルはレコードとカラムで構成される。

## Tags
#database #sql #rails #要復習

## Links
- [[note-insight-database]]
- [[note-insight-database-record]]
- [[note-insight-database-column]]

## Body
テーブルは、データベースの中でデータを種類ごとに整理して保存する場所です。ユーザー情報なら `users`、投稿情報なら `posts` のように、同じ性質のデータをまとめます。

テーブルを理解すると、Rails のモデルがどの保存場所と対応しているのかをイメージしやすくなります。
