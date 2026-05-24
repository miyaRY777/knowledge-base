---
id: note-insight-database-server
title: データベースサーバーはアプリのデータを保存して取り出せるようにするサーバー
created: 2026-05-24
source: [[2026-05-24_insight_database-server-and-distributed-database.md]]
---

## Summary
- データベースサーバーは、アプリのデータを保存・管理するためのサーバーです。
- ユーザー情報や投稿、商品データなどを検索・更新・削除できるようにします。
- PostgreSQL や MySQL のような DBMS が動く場所として考えると整理しやすいです。

## Tags
#database #server #dbms #web-app #sql

## Links
- [[note-insight-database]]
- [[note-insight-dbms]]
- [[note-insight-sql]]
- [[note-insight-centralized-data-management]]

## Body
データベースサーバーは、Webアプリなどで使うデータを保存し、必要なときに取り出したり更新したりできるようにするサーバーです。ユーザー情報、投稿、商品情報のように、アプリが継続的に扱うデータを管理します。

Rails アプリから見ると、アプリケーションサーバーが Active Record などを通して SQL を発行し、データベースサーバー側の PostgreSQL や MySQL が保存・検索・更新・削除を担当する、という関係で理解できます。

## Example
- ECサイトの会員登録でユーザー情報を保存する
- ログイン時にメールアドレスやパスワード情報を照合する
- 商品一覧を表示するために商品データを取得する
