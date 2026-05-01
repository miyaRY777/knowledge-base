---
id: note-insight-axios-instance
title: Axiosインスタンスの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **共通設定をまとめたAxios専用の通信オブジェクトのこと**
- `Axiosインスタンス` は、`axios.create()` で作るカスタム設定付きのAxiosです。
- `baseURL` や `headers` などを最初にまとめて設定できるので、同じ設定を書く手間を減らせます。

## Tags
#javascript #http

## Links

## Body
**共通設定をまとめたAxios専用の通信オブジェクトのこと**

**解説：**
`Axiosインスタンス` は、`axios.create()` で作るカスタム設定付きのAxiosです。
`baseURL` や `headers` などを最初にまとめて設定できるので、同じ設定を書く手間を減らせます。
API通信が増えると特に便利です。

## Example

```js
const apiClient = axios.create({
  baseURL: "https://api.example.com",
  timeout: 5000
});

apiClient.get("/users");
```

このコードでは、共通設定を使い回して通信を簡潔にするために `Axiosインスタンス` を使っています。
