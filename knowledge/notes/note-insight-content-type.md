---
id: note-insight-content-type
title: "Content-Typeは送信するデータの形式をサーバーに伝えるHTTPヘッダー"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **送るデータの種類をサーバーに伝えるヘッダー**
- `Content-Type` は、送信するデータがどんな形式かを示すためのヘッダーです。
- `application/json` を指定すると、「JSON形式で送ります」という意味になります。

## Tags
#javascript #http

## Links

## Body
`Content-Type` ヘッダーはリクエストボディの形式をサーバーに伝えるもので、サーバーはこれを見てどう解析するかを決めます。
Axios はオブジェクトをボディに渡すと自動的に JSON にシリアライズして `Content-Type: application/json` をセットするため、明示的に指定しなくてよい場合がほとんどです。
フォームデータを送る場合は `application/x-www-form-urlencoded` や `multipart/form-data` に変わり、この場合は明示的に指定するか `FormData` を使う必要があります。

## Example

```js
axios.post("/posts", { title: "Hello" }, {
  headers: {
    "Content-Type": "application/json"
  }
});
```

このコードでは、送信データがJSON形式であることを伝えるために `Content-Type` を使っています。
