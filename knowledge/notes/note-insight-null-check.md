---
id: note-insight-null-check
title: nullチェックはnullかどうかを確認してから処理する
created: 2026-06-05
source: [[2026-06-05_insight_null-and-related-values]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- nullチェックは、値が null かどうかを確認してから処理を行う手法です。
- null のままプロパティやメソッドを呼ぶとエラーになるため必要です。
- `=== null` で厳密比較するのが基本で、`??` や Optional Chaining と組み合わせることも多いです。
- `typeof null` は `"object"` を返すため、`typeof` での判定はできない点に注意。

## Tags
#javascript #programming

## Links
- [[note-insight-null-js]]
- [[note-insight-nullish-coalescing]]

## Body
null のまま `.name` や `.length` などのプロパティにアクセスすると `TypeError` が発生します。そのため処理の前に null かどうかを確認するnullチェックが必要です。`=== null` による厳密比較が基本ですが、`??`（nullish coalescing）や `?.`（Optional Chaining）を使うことで簡潔に書けます。

## Example
```js
const user = null;

if (user === null) {
  console.log("ユーザーが存在しません");
}

// Optional Chaining を使う場合
console.log(user?.name); // undefined（エラーにならない）
```
