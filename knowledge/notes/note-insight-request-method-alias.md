---
id: note-insight-request-method-alias
title: リクエストメソッドエイリアスの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **HTTPメソッドを短くわかりやすく書ける便利な書き方**
- `axios.get()` や `axios.post()` のような書き方は、`Axios` が用意しているエイリアスです。
- `axios.request({ method: ... })` よりも短く書けるので、コードが読みやすくなります。

## Tags
#javascript #http

## Links
- [[関連ノート]]

## Body
**HTTPメソッドを短くわかりやすく書ける便利な書き方**

**解説：**
`axios.get()` や `axios.post()` のような書き方は、`Axios` が用意しているエイリアスです。
`axios.request({ method: ... })` よりも短く書けるので、コードが読みやすくなります。
よく使う `GET` `POST` `PUT` `DELETE` などが用意されています。

## Example

```js
axios.get("/users");
axios.post("/users", { name: "Taro" });
```

このコードでは、HTTPメソッドを簡潔に書くために `リクエストメソッドエイリアス` を使っています。
