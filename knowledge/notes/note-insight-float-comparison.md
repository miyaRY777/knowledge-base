---
id: note-insight-float-comparison
title: 浮動小数点数の比較は誤差を考慮して差が十分小さいか確認する
created: 2026-06-12
source: [[2026-06-12_insight_js-number-types-and-floating-point]]
---

## Summary
- 浮動小数点誤差により、計算した小数は期待値と完全一致しない場合があります。
- `===` で直接比較せず、差が `Number.EPSILON` より小さいかを確認する方法が有効です。

## Tags
#javascript #floating-point #programming

## Links
- [[note-insight-rounding-error]]
- [[note-insight-repeating-binary-fraction]]
- [[note-insight-javascript-number-type]]

## Body
`0.1 + 0.2 === 0.3` は `false` になります。浮動小数点誤差が生じるため、計算結果と期待値の差が十分に小さいかどうかで比較するのが安全です。`Number.EPSILON` はJavaScriptで表現できる最小の差（約`2.2 × 10⁻¹⁶`）です。

## Example
```js
const result = 0.1 + 0.2;
const expected = 0.3;

console.log(result === expected);                          // false
console.log(Math.abs(result - expected) < Number.EPSILON); // true
```
