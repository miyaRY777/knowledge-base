---
id: note-insight-get-request
title: "GETリクエストの要点"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **サーバーからデータを取得するときのリクエストのこと**
- `GETリクエスト` は、データを読むときに使う基本的なHTTPメソッドです。
- 一覧表示や詳細表示のデータ取得でよく使います。

## Tags
#javascript #http

## Links
- [[note-insight-http-request]]
- [[2026-05-06_insight_http-message-methods]]

## Body
**サーバーからデータを取得するときのリクエストのこと**

**解説：**
`GETリクエスト` は、データを読むときに使う基本的なHTTPメソッドです。
一覧表示や詳細表示のデータ取得でよく使います。
Axiosでは `axios.get()` のように書けます。

HTTP メッセージとして見ると、`GET /posts HTTP/1.1` のようにリクエストラインへ書かれます。`GET` は「指定したリソースを取得したい」という意味で、サーバー上のデータを新しく作ったり変更したりする目的では使いません。

## Example
```js
axios.get("/posts/1")
  .then(response => {
    console.log(response.data);
  });
```

このコードでは、投稿データを取得するために `GETリクエスト` を使っています。

```http
GET /posts HTTP/1.1
Host: example.com
```

この例では、投稿一覧を取得したいことを HTTP リクエストとしてサーバーに伝えています。
