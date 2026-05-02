---
id: note-insight-database-column
title: "カラムはテーブルで保存するデータ項目を表す列"
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
---

## Summary
- カラムは、テーブルに保存する項目を表す。
- `users` テーブルなら `name`、`email`、`created_at` などがカラムになる。
- カラムには型や制約を設定して、保存できる値を決められる。

## Tags
#database #sql #rails #要復習

## Links
- [[note-insight-database-table]]
- [[note-insight-database-record]]
- [[note-insight-database-constraint]]

## Body
カラムは、テーブルの中で「どんな項目を保存するか」を表す列です。ユーザーの名前、メールアドレス、作成日時のように、1つのレコードが持つ属性を定義します。

Rails の migration でカラムを追加すると、アプリが扱えるデータ項目も増えます。

<!-- review_log: 2026-05-02 -->
