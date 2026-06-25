---
id: note-insight-division-operator
title: 除算演算子（/）は左側の値を右側の値で割る演算子
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- `/` は左のオペランドを右のオペランドで割った商を返します。
- 結果のデータ型や小数の扱いは言語によって異なります。

## Tags
#programming #javascript #operator

## Links
- [[note-insight-arithmetic-operator]]
- [[note-insight-integer-division-result]]
- [[note-insight-division-by-zero]]

## Body
JavaScriptでは `/` の結果は常に `number` 型で、小数も返されます（`12 / 5 = 2.4`）。Javaでは整数型同士の割り算は小数部分が切り捨てられます。0で割ると `Infinity` または `NaN` になります。

## Example
```js
console.log(12 / 5);  // 2.4
console.log(1 / 0);   // Infinity
console.log(0 / 0);   // NaN
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
