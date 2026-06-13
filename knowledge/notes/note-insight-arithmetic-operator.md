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
算術演算子はオペランドが数値の場合に計算を行います。JavaScriptでは `+` が文字列に使われると連結演算子として機能するため、オペランドの型の確認が重要です。

## Example
```js
console.log(12 + 5); // 17
console.log(12 - 5); // 7
console.log(12 * 5); // 60
console.log(12 / 5); // 2.4
console.log(12 % 5); // 2
```
