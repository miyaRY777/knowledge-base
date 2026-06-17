---
id: note-insight-post-request
title: "POSTリクエストはサーバーに新しいデータを送るHTTPメソッド"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **サーバーに新しいデータを送るときのリクエストのこと**
- `POSTリクエスト` は、新規作成したいデータをサーバーに送るときによく使います。
- フォーム送信や新規登録の処理でよく登場します。

## Tags
#javascript #http

## Links
- [[note-insight-http-request]]
- [[2026-05-06_insight_http-message-methods]]

## Body
**サーバーに新しいデータを送るときのリクエストのこと**

**解説：**
`POSTリクエスト` は、新規作成したいデータをサーバーに送るときによく使います。
フォーム送信や新規登録の処理でよく登場します。
Axiosでは、送信したいデータを第2引数に渡せます。

HTTP メソッドとしての `POST` は、指定したリソースにデータを送るために使います。Rails では、新規作成フォームを送信してレコードを保存する場面でよく登場します。HTTP メッセージでは、ヘッダーのあとに空行を置き、その下に送信したい本文を含められます。

## Example

```js
axios.post("/posts", {
  title: "New Post",
  body: "Hello"
});
```

このコードでは、新しい投稿データを作成するために `POSTリクエスト` を使っています。

```http
POST /posts HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded

title=Hello
```

この例では、新しい投稿データをサーバーへ送信しています。
