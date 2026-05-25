---
id: note-insight-put-request
title: "PUTは既存リソース全体を置き換えるHTTPメソッド"
created: 2026-05-06
source: [[2026-05-06_insight_http-message-methods]]
review_streak: 0
last_reviewed_on: 2026-05-25
---

## Summary
- `PUT` は、指定したリソースを作成または全体置き換えするHTTPメソッドです。
- 既存データをまるごと更新する意味合いで使われます。
- Rails の更新処理では、部分更新の `PATCH` と使い分けて理解すると整理しやすいです。

## Tags
#http #rails #web #要復習

## Links
- [[note-insight-http-request]]
- [[note-insight-patch-request]]
- [[note-insight-idempotent]]

## Body
`PUT` は、指定したリソースを作成または置き換えるための HTTP メソッドです。既存データに対して使う場合は、そのリソース全体を新しい内容で置き換える意味合いになります。

Rails では更新処理に関係しますが、実務では「一部だけ変更する」更新も多いため、`PATCH` が使われることも多いです。`PUT` は全体置き換え、`PATCH` は部分更新という違いで押さえると混乱しにくいです。

## Example
```http
PUT /posts/1 HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded

title=Updated&body=NewBody
```

この例では、ID が 1 の投稿を指定した内容で更新しようとしています。

## Action
- [ ] Rails のルーティングで `PUT` と `PATCH` がどう扱われるか確認する
