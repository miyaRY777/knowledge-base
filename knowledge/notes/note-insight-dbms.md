---
id: note-insight-dbms
title: DBMSはデータベースを管理・操作するソフトウェア
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
---

## Summary
- DBMS は、データベースを作成し、保存・検索・更新・削除を扱うためのソフトウェア。
- MySQL、PostgreSQL、Oracle Database などが代表例。
- Rails から直接ファイルを触るのではなく、DBMS を通してデータを操作する。

## Tags
#database #sql #dbms

## Links
- [[note-insight-database]]
- [[note-insight-sql]]

## Body
DBMS は、データベースそのものを管理するためのソフトウェアです。アプリがデータを保存したり取り出したりするとき、裏側では DBMS が SQL などの命令を受け取り、実際のデータ管理を担当します。

Rails アプリで PostgreSQL や MySQL を使う場合、Active Record は DBMS に対して SQL を発行し、その結果を Ruby のオブジェクトとして扱えるようにしています。
