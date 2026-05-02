---
id: note-insight-promise
title: "Promiseの要点"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **あとで結果が返ってくる処理を受け取るための仕組みのこと**
- `Promise` は、すぐには終わらない処理の結果を、あとから受け取るための仕組みです。
- HTTP通信のような非同期処理でよく使われます。

## Tags
#javascript #async

## Links

## Body
**あとで結果が返ってくる処理を受け取るための仕組みのこと**

**解説：**
`Promise` は、すぐには終わらない処理の結果を、あとから受け取るための仕組みです。
HTTP通信のような非同期処理でよく使われます。
成功時は `.then()`、失敗時は `.catch()` で処理を書くことが多いです。


## Example
```js
axios.get("/users")
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```

このコードでは、通信結果をあとで受け取るために `Promise` を使っています。
