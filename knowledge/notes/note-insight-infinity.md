---
id: note-insight-infinity
title: InfinityはJavaScriptで無限大を表すnumber型の特別な値
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
---

## Summary
- `Infinity` は正の数を `0` で割ったときなどに返されるJavaScriptの特別な値です。
- エラーではなく `number` 型に属します。

## Tags
#javascript #number

## Links
- [[note-insight-negative-infinity]]
- [[note-insight-division-by-zero]]
- [[note-insight-javascript-number-type]]
- [[note-insight-number-max-value]]

## Body
JavaScriptでは `1 / 0` が例外にならず `Infinity` を返します。`Number.MAX_VALUE` を超えた場合も `Infinity` になります。`Infinity` との比較や演算も可能ですが、意図しない `Infinity` の伝播に注意が必要です。

## Example
```js
console.log(1 / 0);           // Infinity
console.log(typeof Infinity);  // number
console.log(Infinity > 99999); // true
```
