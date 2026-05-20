---
id: note-insight-consistency
title: Consistencyはトランザクション後もデータベースのルールを守る性質
created: 2026-05-20
source: [[2026-05-20_insight_acid-properties.md]]
---

## Summary
- Consistency は、トランザクション前後でデータベースの整合性を保つ性質です。
- NOT NULL、外部キー、ユニーク制約などに反するデータを保存しないことと関係します。
- アプリ側の処理だけでなく、データベース側の制約も一貫性を守る支えになります。

## Tags
#database #sql #transaction #acid #consistency #data-integrity

## Links
- [[note-insight-acid-properties]]
- [[note-insight-data-integrity-and-consistency]]
- [[note-insight-database-constraint]]
- [[note-insight-not-null-constraint]]
- [[note-insight-foreign-key-constraint]]
- [[note-insight-unique-constraint]]

## Body
Consistency は、トランザクションを実行したあとも、データベースが守るべきルールに反しない状態を保つ性質です。処理が完了しても、必須項目が空だったり、存在しないレコードを参照していたり、重複禁止の値が重複していたりすると、一貫した状態とは言えません。

この性質は、アプリケーションのバリデーションだけでなく、データベースの制約とも強く関係します。ルール違反の保存を失敗させることで、不正な状態が確定するのを防ぎます。

## Example
- `email` が必須のユーザーを空メールアドレスで作成しない
- 存在しない `user_id` を持つ投稿を保存しない
- 同じメールアドレスを重複登録しない
