---
id: note-insight-crud-operations
title: CRUDはデータの作成・取得・更新・削除を表す基本操作
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
---

## Summary
- CRUD は Create、Read、Update、Delete の基本操作をまとめた考え方。
- SQL では `INSERT`、`SELECT`、`UPDATE`、`DELETE` が対応する。
- Web アプリの多くの機能は CRUD を組み合わせて作られる。

## Tags
#database #sql #crud #rails

## Links
- [[note-insight-sql]]
- [[note-insight-sql-select]]
- [[note-insight-database-query]]

## Body
CRUD は、データを扱う基本操作をまとめた言葉です。新しく保存する、取り出して表示する、内容を書き換える、不要になったものを消す、という4つの操作が中心になります。

Rails の一覧画面、詳細画面、作成フォーム、編集フォーム、削除ボタンも、多くはこの CRUD の考え方に沿って作られます。
