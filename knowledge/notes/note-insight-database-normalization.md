---
id: note-insight-database-normalization
title: データベース正規化は重複と不整合を減らすためにテーブルを整理する考え方
created: 2026-05-19
source: [[2026-05-19_insight_database-normalization.md]]
review_streak: 0
last_reviewed_on: 2026-05-22
quiz_fail_log: []
---

## Summary
- 正規化は、同じ情報を何度も持たないようにテーブルを分ける設計方針です。
- 更新漏れや削除ミスによるデータ不整合を減らしやすくなります。
- 分割しすぎると結合が増えるため、読み書きのしやすさとのバランスも必要です。

## Tags
#database #sql #normalization #database-design

## Links
- [[note-insight-relational-database]]
- [[note-insight-centralized-data-management]]
- [[note-insight-first-normal-form]]
- [[note-insight-second-normal-form]]
- [[note-insight-third-normal-form]]

## Body
データベース正規化は、1つの表に重複した情報を詰め込むのではなく、意味のまとまりごとにテーブルを分けて管理する考え方です。たとえば注文ごとに住所を持つのではなく、住所をユーザー情報側に寄せると、住所変更時の更新箇所を減らせます。

目的は、保存するデータの重複を減らし、変更時に片方だけ古いまま残るような不整合を起こしにくくすることです。一方で、テーブルを細かく分けるほど取得時の結合が増えるため、実際の設計では整合性と扱いやすさのバランスを見ます。

## Example
- `users` にユーザー名や住所を保存する
- `orders` には `user_id` を持たせ、注文とユーザーを関連づける
- 住所変更時は `users` の該当行だけを更新する
