---
id: note-insight-http-response
title: "HTTPレスポンスはサーバーからクライアントへ返す返事"
created: 2026-05-06
source: [[2026-05-06_insight_http-message-methods]]
---

## Summary
- HTTPレスポンスは、HTTPリクエストに対してサーバーが返すメッセージです。
- ステータス行、ヘッダー、空行、本文で構成されることがあります。
- ステータスコードや `Content-Type` などで、処理結果や返すデータの種類を伝えます。

## Tags
#http #web #network

## Links
- [[note-insight-http-request]]
- [[note-insight-headers]]
- [[note-insight-content-type]]

## Body
HTTPレスポンスは、クライアントから届いた HTTP リクエストに対して、サーバーが返す返事のメッセージです。ブラウザがページを要求すると、サーバーは成功・失敗などの結果と、必要に応じて HTML や JSON などの本文を返します。

レスポンスの先頭にはステータス行があり、`HTTP/1.1 200 OK` のように HTTP バージョン、ステータスコード、人間向けの説明が並びます。そのあとにヘッダーが続き、空行を挟んで本文が続きます。ヘッダーには、レスポンス本文の種類を表す `Content-Type` や、本文の長さを表す `Content-Length` などが入ります。

## Example
```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

<html>
  <body><h1>Welcome</h1></body>
</html>
```

この例では、リクエストが成功し、HTML の本文が返されています。

## Action
- [ ] 代表的なステータスコードを別ノートで整理する
