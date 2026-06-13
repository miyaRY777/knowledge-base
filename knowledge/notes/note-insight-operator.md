---
id: note-insight-operator
title: 演算子はオペランドに特定の処理を行う記号
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
---

## Summary
- 演算子はオペランドに計算・比較・論理演算などを適用し、新しい値を返します。
- `+`（加算）、`-`（減算）、`===`（厳密等価）などが代表例です。

## Tags
#programming #operator #javascript

## Links
- [[note-insight-operand]]
- [[note-insight-arithmetic-operator]]
- [[note-insight-expression]]

## Body
演算子の種類には算術演算子・比較演算子・論理演算子などがあります。同じ記号でもオペランドのデータ型によって動作が変わる場合があります（例：`+` は数値なら加算、文字列なら連結）。

## Example
```js
console.log(8 + 3);    // 11（加算）
console.log("a" + "b"); // "ab"（文字列連結）
```
