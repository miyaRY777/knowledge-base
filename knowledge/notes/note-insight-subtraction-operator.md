---
id: note-insight-subtraction-operator
title: 減算演算子（-）は左側の値から右側の値を引く演算子
created: 2026-06-13
source: [[2026-06-13_insight_js-arithmetic-operators-and-expressions]]
---

## Summary
- `-` は左のオペランドから右のオペランドを引いた差を返します。
- 順番によって結果の正負が変わります。

## Tags
#programming #javascript #operator

## Links
- [[note-insight-arithmetic-operator]]

## Body
`a - b` は `a` から `b` を引いた値を返します。`+` と異なり、文字列に使っても連結にはならず、数値への暗黙変換が試みられます。

## Example
```js
console.log(12 - 5);  // 7
console.log(5 - 12);  // -7
```
