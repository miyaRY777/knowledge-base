---
id: note-insight-get-request
title: GETリクエストの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **サーバーからデータを取得するときのリクエストのこと**
- `GETリクエスト` は、データを読むときに使う基本的なHTTPメソッドです。
- 一覧表示や詳細表示のデータ取得でよく使います。

## Tags
#javascript #http

## Links

## Body
**サーバーからデータを取得するときのリクエストのこと**

**解説：**
`GETリクエスト` は、データを読むときに使う基本的なHTTPメソッドです。
一覧表示や詳細表示のデータ取得でよく使います。
Axiosでは `axios.get()` のように書けます。


## Example
```js
axios.get("/posts/1")
  .then(response => {
    console.log(response.data);
  });
```

このコードでは、投稿データを取得するために `GETリクエスト` を使っています。
