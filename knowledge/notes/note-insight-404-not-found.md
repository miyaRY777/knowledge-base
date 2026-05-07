---
id: note-insight-404-not-found
title: "404 Not Foundはリクエストされたリソースが見つからないことを表す"
created: 2026-05-07
source: [[2026-05-07_insight_http-status-codes]]
---

## Summary
- `404 Not Found` は、リクエストされたページやデータが見つからないことを表します。
- URLが間違っている場合や、対象ページが削除されている場合などに返されます。
- 存在しないIDの詳細ページへアクセスした場合にも関係します。

## Tags
#http #web #status-code #error

## Links
- [[note-insight-http-status-code]]
- [[note-insight-active-record-record-not-found]]

## Body
`404 Not Found` は、サーバーがリクエストされたリソースを見つけられなかったことを表すHTTPステータスコードです。URLが間違っている場合、ページが削除済みの場合、存在しないIDの詳細ページへアクセスした場合などに返されます。

Rails では、存在しないレコードを探したときの `ActiveRecord::RecordNotFound` とつながって理解できます。ユーザーにとっては「そのページやデータは存在しない」という意味のエラー画面として見えることが多いです。

## Example
- 存在しないURLにアクセスする
- 削除済みの記事ページを開こうとする
- 存在しないIDの詳細ページにアクセスする

## Action
- [ ] Rails の 404 ページ表示と `RecordNotFound` の関係を整理する
