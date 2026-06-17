---
id: note-insight-promise
title: "Promiseは非同期処理の結果をあとから受け取るための仕組み"
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
Promise は、HTTPリクエストやタイマーなど「結果がすぐ返ってこない処理」を扱うためのオブジェクトです。
処理が完了すると「成功（fulfilled）」か「失敗（rejected）」のいずれかの状態になり、`.then()` で成功時の処理、`.catch()` で失敗時の処理を書きます。
`async/await` は Promise をより同期的に見える形で書くための構文糖衣で、内部的には同じ Promise が動いています。


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
