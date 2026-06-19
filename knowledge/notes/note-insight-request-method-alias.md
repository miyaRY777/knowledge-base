---
id: note-insight-request-method-alias
title: "リクエストメソッドエイリアスはaxios.getなどHTTPメソッドを短く書ける便利な記法"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
quiz_fail_log: []
---

## Summary
- **HTTPメソッドを短くわかりやすく書ける便利な書き方**
- `axios.get()` や `axios.post()` のような書き方は、`Axios` が用意しているエイリアスです。
- `axios.request({ method: ... })` よりも短く書けるので、コードが読みやすくなります。

## Tags
#javascript #http

## Links

## Body
Axios のメソッドエイリアス（`axios.get()`, `axios.post()` など）は内部的に `axios.request({ method: "GET", ... })` を呼んでいる糖衣構文です。
HTTP メソッドの役割に対応していて、`GET`（取得）・`POST`（作成）・`PUT`/`PATCH`（更新）・`DELETE`（削除）がそれぞれ用意されています。
`PUT` は全体の置き換え、`PATCH` は一部の変更という使い分けがありますが、API 設計によって慣習が異なる場合もあります。

## Example

```js
axios.get("/users");
axios.post("/users", { name: "Taro" });
```

このコードでは、HTTPメソッドを簡潔に書くために `リクエストメソッドエイリアス` を使っています。
