---
id: note-insight-dbms
title: "DBMSはデータベースを管理・操作するソフトウェア"
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
---

## Summary
- DBMS は、データベースを作成し、保存・検索・更新・削除を扱うためのソフトウェア。
- データの整合性、バックアップ、アクセス権限の管理も担う。
- MySQL、PostgreSQL、Oracle Database などが代表例。
- Rails から直接ファイルを触るのではなく、DBMS を通してデータを操作する。

## Tags
#database #sql #dbms

## Links
- [[note-insight-database]]
- [[note-insight-sql]]
- [[note-insight-centralized-data-management]]

## Body
DBMS は、データベースそのものを管理するためのソフトウェアです。アプリがデータを保存したり取り出したりするとき、裏側では DBMS が SQL などの命令を受け取り、実際のデータ管理を担当します。データの整合性を守ること、バックアップを扱うこと、誰がどのデータへアクセスできるかを制御することも役割に含まれます。

Rails アプリで PostgreSQL や MySQL を使う場合、Active Record は DBMS に対して SQL を発行し、その結果を Ruby のオブジェクトとして扱えるようにしています。複数のユーザーや複数のアプリケーションが同じデータベースを使う場合も、DBMS が中央でデータを管理することで、同じ最新データを共有しやすくなります。

## Example
- Rails アプリが PostgreSQL にユーザー情報を保存する
- 管理画面で更新した商品情報を、ECサイトや分析ツールでも参照する
- 複数ユーザーが同じ顧客データを使っても、DBMS が整合性や権限を管理する
