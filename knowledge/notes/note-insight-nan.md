---
id: note-insight-nan
title: NaNは数値として有効な結果を表せないときに返される特別な値
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
quiz_phase: 1
quiz_streak: 0
quiz_fail_streak: 0
---

## Summary
- `NaN`（Not a Number）は `0 / 0` や無効な数値変換の結果として返されます。
- `number` 型に属しますが、自分自身とも等しくない唯一の値です（`NaN === NaN` は `false`）。
- 判定には `Number.isNaN()` を使います。

## Tags
#javascript #number

## Links
- [[note-insight-division-by-zero]]
- [[note-insight-infinity]]
- [[note-insight-javascript-number-type]]

## Body
`NaN` は計算結果が数値として定まらないときに返されます。`NaN === NaN` が `false` になる点が特殊で、`typeof NaN` は `"number"` を返します。チェックには必ず `Number.isNaN()` を使います。

## Example
```js
console.log(0 / 0);             // NaN
console.log(NaN === NaN);       // false（自分自身と等しくない）
console.log(typeof NaN);        // number
console.log(Number.isNaN(0/0)); // true
```
