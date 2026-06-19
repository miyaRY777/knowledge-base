---
id: note-insight-database-key
title: キーはレコード識別やテーブル関連づけに使う目印
created: 2026-05-17
source: [[2026-05-17_insight_database-null-and-keys]]
quiz_fail_log: []
---

## Summary
- キーは、テーブルのデータを識別したり、別テーブルと関連づけたりするための目印です。
- 代表例として、1件を一意に見分ける主キーと、別テーブルを参照する外部キーがあります。
- リレーショナルデータベースでデータ同士の関係を扱う基礎になります。

## Tags
#database #sql #key

## Links
- [[note-insight-primary-key]]
- [[note-insight-foreign-key]]
- [[note-insight-relational-database]]

## Body
キーは、データベースの中でレコードを見分けたり、別のテーブルのレコードと結びつけたりするために使う項目です。単に値を保存するだけでなく、「この行は誰か」「この投稿はどのユーザーのものか」を表す役割を持ちます。

よく使う代表例が主キーと外部キーです。主キーはそのテーブル内で1件を一意に識別し、外部キーは別テーブルの主キーを参照して関係を表します。

## Example
- `users.id` でユーザーを見分ける
- `posts.user_id` で投稿の所有者を表す
- `orders.customer_id` で注文と顧客を結びつける

## Action
- [ ] 候補キーと複合キーを整理する
