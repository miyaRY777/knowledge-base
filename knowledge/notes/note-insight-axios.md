---
id: note-insight-axios
title: "AxiosはJavaScriptからHTTPリクエストを簡単に送るためのライブラリ"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **JavaScriptでサーバーにHTTPリクエストを簡単に送るためのライブラリ（道具）**
- `Axios` は、JavaScriptからサーバーとやり取りするときに使うライブラリです。
- たとえば、一覧データを取りに行ったり、フォームの内容を送信したりするときに使います。

## Tags
#javascript #http

## Links

## Body
Axios はブラウザ・Node.js の両方で動くHTTPクライアントライブラリで、標準の Fetch API を使いやすくラップしたものです。
レスポンスの JSON 自動パース、4xx/5xx エラーの自動例外化、リクエスト・レスポンスの共通処理（インターセプター）などが標準で備わっています。
Fetch API と違いインストールが必要ですが、記述量が減り、エラーハンドリングが統一しやすいため実務でよく使われます。


## Example
```js
axios.get("/users")
  .then(response => {
    console.log(response.data);
  });
```

このコードでは、`/users` からデータを取得するために `Axios` を使っています。
