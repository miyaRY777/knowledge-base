---
id: note-insight-jsonplaceholder
title: "JSONPlaceholderはHTTP通信を練習できるモックAPIサービス"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
quiz_fail_log: []
---

## Summary
- 本物のAPIのようにHTTP通信を試せる練習用サービス（**モックAPIサービス**）
- `JSONPlaceholder` は、本物のAPIのようにHTTP通信を試せる練習用サービスです。
- `GET` や `POST` などを気軽に試せるので、学習やサンプルコードによく使われます。

## Tags
#javascript #http

## Links

## Body
JSONPlaceholder は `https://jsonplaceholder.typicode.com` で公開されているモック REST API で、users・posts・todos などのエンドポイントが用意されています。
GET は実際のデータを返しますが、POST・PUT・DELETE は成功レスポンスを返しながら実際にはデータを変更しません（サーバーサイドの状態が変わらない）。
Axios や Fetch API の動作確認、非同期処理の練習、フロントエンドの実装検証など「本物のAPIが不要な場面」で手軽に使えます。

## Example

```js
axios.get("https://jsonplaceholder.typicode.com/posts/1")
  .then(response => {
    console.log(response.data);
  });
```

このコードでは、練習用APIに通信して動作確認するために `JSONPlaceholder` を使っています。

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
