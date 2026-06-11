---
id: note-insight-data-type
title: データ型は値の種類を表す分類
created: 2026-06-11
source: [[2026-06-11_insight_js-data-types-and-literals]]
---

## Summary
- データ型は、値が数値・文字列・真偽値のどれかを区別するための分類です。
- データ型によって使える操作や扱い方が変わります。
- JavaScriptでは `typeof` 演算子で型を確認できます。

## Tags
#javascript #programming #data-type

## Links
- [[note-insight-primitive-type]]
- [[note-insight-typeof]]
- [[note-insight-javascript-number-type]]
- [[note-insight-string-type]]
- [[note-insight-boolean-type]]

## Body
データ型は「この値は何者か」を定義します。同じ `100` でも `number` 型なら算術演算ができますが、`string` 型の `"100"` では文字列結合になります。型の違いを意識することはバグを防ぐ基本です。

## Example
```js
console.log(typeof 100);   // number
console.log(typeof "100"); // string
console.log(typeof false); // boolean
```
