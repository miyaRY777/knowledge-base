---
id: note-insight-negative-infinity
title: -InfinityはJavaScriptで負の無限大を表すnumber型の特別な値
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
quiz_phase: 1
quiz_streak: 0
quiz_fail_streak: 0
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
`-Infinity` は負の数を `0` で割った場合や `Math.log(0)` など特定の演算で返される `number` 型の特別な値です。
通常の数値との比較では常に最小値として振る舞い、`-Infinity < -999999` は `true` になります。
値が有限かどうかを確認するには `isFinite()` を使います（`-Infinity` に対しては `false` を返す）。

## Example
```js
console.log(-1 / 0);            // -Infinity
console.log(typeof -Infinity);  // number
console.log(-Infinity < -99999); // true
```
