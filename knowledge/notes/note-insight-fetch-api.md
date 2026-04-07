---
id: note-insight-fetch-api
title: Fetch APIの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **ブラウザ標準で使えるHTTP通信の仕組みのこと**
- `Fetch API` は、ブラウザに最初から用意されているHTTPリクエスト用の機能です。
- 追加インストールなしで使えますが、レスポンスをJSONとして使うには `response.json()` を呼ぶ必要があります。

## Tags
#javascript #http

## Links
- [[関連ノート]]

## Body
**ブラウザ標準で使えるHTTP通信の仕組みのこと**

**解説：**
`Fetch API` は、ブラウザに最初から用意されているHTTPリクエスト用の機能です。
追加インストールなしで使えますが、レスポンスをJSONとして使うには `response.json()` を呼ぶ必要があります。
`Axios` と比べると、少し記述が増えることがあります。

## Example

```js
fetch("/users")
  .then(response => response.json())
  .then(data => {
    console.log(data);
  });
```

このコードでは、ブラウザ標準の仕組みでデータを取得するために `Fetch API` を使っています。
