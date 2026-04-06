---
id: note-insight-content-type
title: Content-Typeの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **送るデータの種類をサーバーに伝えるヘッダー**
- `Content-Type` は、送信するデータがどんな形式かを示すためのヘッダーです。
- `application/json` を指定すると、「JSON形式で送ります」という意味になります。

## Tags
#javascript #http

## Links
- [[関連ノート]]

## Body
**送るデータの種類をサーバーに伝えるヘッダー**

**解説：**
`Content-Type` は、送信するデータがどんな形式かを示すためのヘッダーです。
`application/json` を指定すると、「JSON形式で送ります」という意味になります。
APIにJSONを送るときによく使います。

具体例：

```js
axios.post("/posts", { title: "Hello" }, {
  headers: {
    "Content-Type": "application/json"
  }
});
```

このコードでは、送信データがJSON形式であることを伝えるために `Content-Type` を使っています。
