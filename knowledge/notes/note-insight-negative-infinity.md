---
id: note-insight-negative-infinity
title: -InfinityはJavaScriptで負の無限大を表すnumber型の特別な値
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
---

## Summary
- `-Infinity` は負の数を正の `0` で割るなどの計算で返されます。
- `Infinity` と同様に `number` 型の特別な値です。

## Tags
#javascript #number

## Links
- [[note-insight-infinity]]
- [[note-insight-division-by-zero]]

## Body
`-1 / 0` の結果は `-Infinity` です。`-Infinity` は数直線上の負の無限大を表し、あらゆる有限の数より小さい値です。

## Example
```js
console.log(-1 / 0);            // -Infinity
console.log(typeof -Infinity);  // number
console.log(-Infinity < -99999); // true
```
