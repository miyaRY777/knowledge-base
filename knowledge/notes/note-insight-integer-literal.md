---
id: note-insight-integer-literal
title: 整数リテラルは整数を直接コードに書いた値
created: 2026-06-11
source: [[2026-06-11_insight_js-data-types-and-literals]]
---

## Summary
- 整数リテラルは、小数点を含まない整数の値をそのままコードに書いたものです。
- JavaScriptでは整数も小数も `number` 型として扱われます。

## Tags
#javascript #programming

## Links
- [[note-insight-literal]]
- [[note-insight-javascript-number-type]]
- [[note-insight-floating-point-literal]]

## Body
`10` や `2048` のように小数点なしで書いた数値が整数リテラルです。JavaScriptには独立した整数型がなく、`number` 型として扱われます。

## Example
```js
console.log(10);
console.log(2048);
console.log(typeof 10); // number
```
