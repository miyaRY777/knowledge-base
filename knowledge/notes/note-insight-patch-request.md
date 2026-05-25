---
id: note-insight-patch-request
title: "PATCHは既存リソースの一部を更新するHTTPメソッド"
created: 2026-05-06
source: [[2026-05-06_insight_http-message-methods]]
review_streak: 0
last_reviewed_on: 2026-05-25
---

## Summary
- `PATCH` は、指定したリソースの一部を変更するためのHTTPメソッドです。
- 既存データの一部だけを更新したい場面で使います。
- Rails では編集フォームから既存レコードを更新するときによく関係します。

## Tags
#http #rails #web

## Links
- [[note-insight-put-request]]
- [[note-insight-http-request]]

## Body
`PATCH` は、既存リソースの一部だけを変更したいときに使う HTTP メソッドです。たとえば投稿の本文はそのままで、タイトルだけを更新するような場面に向いています。

`PUT` がリソース全体の置き換えという意味合いを持つのに対して、`PATCH` は部分更新を表します。Rails の編集フォームから既存レコードを更新する処理では、この違いを意識しておくとルーティングやリクエストの意味を理解しやすくなります。

## Example
```http
PATCH /posts/1 HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded

title=NewTitle
```

この例では、ID が 1 の投稿のタイトルだけを更新しようとしています。

## Action
- [ ] Rails の `form_with` が更新時にどのメソッドを送るか確認する
