---
id: note-insight-database-query
title: "クエリはデータベースへの命令文"
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
quiz_fail_log: []
---

## Summary
- クエリは、データベースに対して実行する命令。
- SQL で書かれた取得・更新・削除などの文をクエリと呼ぶことが多い。
- Rails のクエリメソッドも、最終的には SQL クエリとして実行される。

## Tags
#database #sql #activerecord

## Links
- [[note-insight-sql]]
- [[note-insight-query-method]]
- [[note-insight-active-record-relation]]

## Body
クエリは、データベースに「この条件で探して」「この値に更新して」と依頼する命令です。SQL の `SELECT` や `UPDATE` などが代表的なクエリです。

Rails では Ruby のメソッドとしてクエリを書けますが、どのタイミングで SQL が発行されるかを意識すると、N+1 や不要な取得に気づきやすくなります。

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
