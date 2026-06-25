---
id: note-insight-axios-instance
title: "AxiosインスタンスはbaseURLやheadersなど共通設定をまとめたカスタムAxiosオブジェクト"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
quiz_fail_log: []
---

## Summary
- **共通設定をまとめたAxios専用の通信オブジェクトのこと**
- `Axiosインスタンス` は、`axios.create()` で作るカスタム設定付きのAxiosです。
- `baseURL` や `headers` などを最初にまとめて設定できるので、同じ設定を書く手間を減らせます。

## Tags
#javascript #http

## Links

## Body
`axios.create()` で作ったインスタンスは、`baseURL`・`headers`・`timeout` などの共通設定を持つ独立した Axios オブジェクトです。
複数の API（認証が必要なAPIとパブリックAPIなど）を使い分けるとき、インスタンスを分けることで設定の混在を防げます。
インスタンスに `interceptors` を追加すると、そのインスタンス経由のリクエスト/レスポンス全体に共通処理（トークン付与・エラーログなど）を差し込めます。

## Example

```js
const apiClient = axios.create({
  baseURL: "https://api.example.com",
  timeout: 5000
});

apiClient.get("/users");
```

このコードでは、共通設定を使い回して通信を簡潔にするために `Axiosインスタンス` を使っています。

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
