---
id: note-insight-jsonplaceholder
title: JSONPlaceholderの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- 本物のAPIのようにHTTP通信を試せる練習用サービス（**モックAPIサービス**）
- `JSONPlaceholder` は、本物のAPIのようにHTTP通信を試せる練習用サービスです。
- `GET` や `POST` などを気軽に試せるので、学習やサンプルコードによく使われます。

## Tags
#javascript #http

## Links
- [[関連ノート]]

## Body
本物のAPIのようにHTTP通信を試せる練習用サービス（**モックAPIサービス**）

**解説：**
`JSONPlaceholder` は、本物のAPIのようにHTTP通信を試せる練習用サービスです。
`GET` や `POST` などを気軽に試せるので、学習やサンプルコードによく使われます。
実際の本番データではなく、練習用のダミーデータです。

具体例：

```js
axios.get("https://jsonplaceholder.typicode.com/posts/1")
  .then(response => {
    console.log(response.data);
  });
```

このコードでは、練習用APIに通信して動作確認するために `JSONPlaceholder` を使っています。
