---
id: note-insight-arithmetic-operator
title: 算術演算子は数値の計算を行う演算子
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
---

## Summary
- 算術演算子は数値の四則演算などを行う演算子です。
- 代表例：`+`（加算）、`-`（減算）、`*`（乗算）、`/`（除算）、`%`（剰余）。

## Tags
#programming #javascript #operator

## Links
- [[note-insight-operator]]
- [[note-insight-four-arithmetic-operations]]
- [[note-insight-operand-type]]

## Body
算術演算子は数値同士の四則演算に使いますが、JavaScriptでは `+` だけは特別で、オペランドに文字列が含まれると数値加算ではなく文字列連結になります。
`%`（剰余）は割り算の余りを返し、偶奇判定（`n % 2 === 0`）や周期的な処理でよく使われます。

## Example
```js
console.log(12 + 5); // 17
console.log(12 - 5); // 7
console.log(12 * 5); // 60
console.log(12 / 5); // 2.4
console.log(12 % 5); // 2
```
