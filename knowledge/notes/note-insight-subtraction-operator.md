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
`a - b` は `a` から `b` を引いた値を返します。`+` と異なり `-` に文字列の特別扱いはなく、文字列オペランドには数値への暗黙変換が試みられます（`"10" - 3 = 7`）。
変換できない文字列が含まれる場合は `NaN` になります（`"hello" - 1 = NaN`）。
単項演算子としての `-x` は符号反転で、二項演算子の引き算とは別の用途です。

## Example
```js
console.log(12 - 5);  // 7
console.log(5 - 12);  // -7
```
