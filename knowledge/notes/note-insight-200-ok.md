---
id: note-insight-200-ok
title: "200 OKはリクエスト成功を表すHTTPステータスコード"
created: 2026-05-07
source: [[2026-05-07_insight_http-status-codes]]
review_streak: 0
last_reviewed_on: 2026-05-25
quiz_fail_log: []
---

## Summary
- `200 OK` は、クライアントのリクエストが成功したことを表します。
- サーバーが正常にレスポンスを返せたときに使われます。
- `200` 番台は成功レスポンスに分類されます。

## Tags
#http #web #status-code

## Links
- [[note-insight-http-status-code]]
- [[note-insight-http-response]]

## Body
`200 OK` は、HTTPリクエストが成功し、サーバーが正常にレスポンスを返したことを表すステータスコードです。ブラウザで一覧ページや詳細ページを開き、サーバーがHTMLを問題なく返せた場合などに使われます。

ステータスコードの `200` 番台は成功を表すグループです。その中でも `200 OK` は、通常のページ表示やAPIレスポンスでよく見る基本的な成功レスポンスです。

## Example
- ユーザーが一覧ページにアクセスする
- サーバーがページのHTMLを正常に返す
- ブラウザに画面が表示される

## Action
- [ ] API レスポンスで `200 OK` と `201 Created` を使い分ける場面を整理する
