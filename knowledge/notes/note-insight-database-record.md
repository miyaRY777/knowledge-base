---
id: note-insight-database-record
title: "レコードはテーブルに保存される1件分のデータ"
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
quiz_fail_log: []
---

## Summary
- レコードは、テーブルの1行にあたるデータ。
- `users` テーブルなら、1人のユーザー情報が1レコードになる。
- Rails のモデルオブジェクトは、1つのレコードに対応して扱われることが多い。

## Tags
#database #sql #rails

## Links
- [[note-insight-database-table]]
- [[note-insight-database-column]]
- [[note-insight-active-record-record-not-found]]

## Body
レコードは、テーブルに保存されたデータ1件分です。たとえば `users` テーブルでは、名前やメールアドレスなどを持つ1人分のユーザー情報が1つのレコードになります。

Rails で `User.find(1)` のように取得したオブジェクトは、データベース上の1レコードを Ruby から扱える形にしたものです。

<!-- review_log: 2026-05-02 -->

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
