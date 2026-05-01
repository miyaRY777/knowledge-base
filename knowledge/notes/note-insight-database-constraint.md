---
id: note-insight-database-constraint
title: 制約は不正なデータを保存しないためのルール
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-05-01
---

## Summary
- 制約は、データベースに保存できる値のルール。
- 空欄禁止、重複禁止、関連先の存在保証などに使う。
- アプリ側のバリデーションだけでなく、DB 側でも守ると安全性が上がる。

## Tags
#database #sql #constraint #rails #要復習

## Links
- [[note-insight-not-null-constraint]]
- [[note-insight-unique-constraint]]
- [[note-insight-foreign-key-constraint]]
- [[note-insight-invariant]]

## Body
制約は、データベースに不正な値を入れないためのルールです。たとえば、名前を空にできない、メールアドレスを重複させない、存在しないユーザーに投稿を紐づけない、といったルールを DB 側で守れます。

Rails のバリデーションは使いやすいですが、DB 制約も併用すると、アプリのバグや同時実行があってもデータを壊しにくくなります。

