---
id: note-insight-js-division
title: JavaScriptの除算は整数同士でも小数を含む結果を返す
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
---

## Summary
- JavaScriptでは `2 / 5` が `0.4` になります（Javaの `0` とは異なる）。
- すべての数値が `number` 型のため整数除算は発生しません。

## Tags
#javascript #data-type

## Links
- [[note-insight-js-number-type-unified]]
- [[note-insight-integer-division-language-diff]]
- [[note-insight-division-operator]]

## Body
JavaScriptの除算は常に `number` 型の結果を返し、小数部分も保持されます。整数除算が必要な場合は `Math.trunc()` や `Math.floor()` を使います。

## Example
```js
console.log(2 / 5);   // 0.4
console.log(2.0 / 5); // 0.4
console.log(Math.trunc(2 / 5)); // 0（整数除算が必要なとき）
```
