---
id: note-insight-floating-point-literal
title: 浮動小数点リテラルは小数を直接コードに書いた値
created: 2026-06-11
source: [[2026-06-11_insight_js-data-types-and-literals]]
---

## Summary
- 浮動小数点リテラルは、`3.14` のように小数点を含む数値をコードに直接書いたものです。
- JavaScriptでは整数も小数もまとめて `number` 型（IEEE 754 倍精度）として扱われます。

## Tags
#javascript #programming

## Links
- [[note-insight-literal]]
- [[note-insight-javascript-number-type]]
- [[note-insight-integer-literal]]
- [[note-insight-ieee754]]
- [[note-insight-floating-point]]

## Body
`3.14` や `0.001` のように小数点を含む数値が浮動小数点リテラルです。内部的には IEEE 754 の倍精度浮動小数点数として扱われるため、精度に限界があります。

## Example
```js
console.log(3.14);
console.log(typeof 3.14); // number
```
