---
id: note-insight-fetch-api
title: "Fetch APIはブラウザ標準で使えるHTTPリクエストの仕組み"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
quiz_fail_log: []
---

## Summary
- **ブラウザ標準で使えるHTTP通信の仕組みのこと**
- `Fetch API` は、ブラウザに最初から用意されているHTTPリクエスト用の機能です。
- 追加インストールなしで使えますが、レスポンスをJSONとして使うには `response.json()` を呼ぶ必要があります。

## Tags
#javascript #http

## Links

## Body
Fetch API はブラウザ組み込みのHTTP通信機能で、外部ライブラリなしでサーバーとやり取りできます。
Axios と大きく違うのは「4xx/5xx でも例外を投げない」点で、`response.ok` を自分でチェックしないと失敗を見逃すバグが起きやすいです。
また JSON として使うには `await response.json()` という2段階の処理が必要で、Axios の `response.data` より記述量が増えます。

## Example

```js
fetch("/users")
  .then(response => response.json())
  .then(data => {
    console.log(data);
  });
```

このコードでは、ブラウザ標準の仕組みでデータを取得するために `Fetch API` を使っています。

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
