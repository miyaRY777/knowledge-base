---
id: note-insight-number-max-value
title: Number.MAX_VALUEはJavaScriptのnumber型で表現できる最大の有限値
created: 2026-06-12
source: [[2026-06-12_insight_js-number-types-and-floating-point]]
quiz_phase: 1
quiz_streak: 0
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- `Number.MAX_VALUE` はJavaScriptの `number` 型で扱える最大の有限値です。
- 安全に整数として扱える最大値を示す `Number.MAX_SAFE_INTEGER` とは別の概念です。

## Tags
#javascript #number #data-type

## Links
- [[note-insight-javascript-number-type]]
- [[note-insight-number-min-value]]

## Body
`Number.MAX_VALUE` はIEEE 754倍精度で表現できる最大の有限値（約`1.8 × 10³⁰⁸`）です。この値を超えると `Infinity` になります。整数を安全に扱える上限は `Number.MAX_SAFE_INTEGER`（`2⁵³ - 1`）で、こちらとは意味が異なります。

## Example
```js
console.log(Number.MAX_VALUE);        // 1.7976931348623157e+308
console.log(Number.MAX_SAFE_INTEGER); // 9007199254740991
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
