---
id: note-insight-database
title: データベースはアプリのデータを保存して取り出す場所
created: 2026-04-28
source: [[2026-04-28_insight_n-plus-one-oop-database.md]]
review_streak: 0
---

## Summary
- データベースは、アプリで使うデータを保存・管理する場所。
- ユーザー情報や投稿などをあとから検索、更新、削除できるようにする。
- Rails では Active Record を通して PostgreSQL や MySQL などを操作することが多い。

## Tags
#database #sql #rails #activerecord #要復習

## Links
- [[note-insight-db-create]]
- [[note-insight-db-migrate]]
- [[note-insight-db-seed]]

## Body
データベースは、アプリで扱う情報を保存し、必要なときに取り出したり更新したりするための仕組みです。ユーザー、投稿、コメントのようなデータは、画面に表示するだけでなく、あとから検索したり変更したりできる形で管理する必要があります。

Rails では Active Record を通してデータベースを操作することが多く、裏側では SQL が実行されます。PostgreSQL や MySQL など、実際にデータを保存する仕組みと Rails のモデル操作をつなげて理解すると整理しやすいです。

## Example
```sql
SELECT *
FROM users;
```

このコードでは、`users` テーブルに保存されているデータを取り出すために SQL を使っています。

## Action
- [ ] テーブル、カラム、レコードの違いを整理する
