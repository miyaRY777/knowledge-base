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
浮動小数点リテラルは `3.14` のように小数点を含む数値をコードに直接書いたものです。
JavaScriptでは整数も小数もすべて IEEE 754 倍精度浮動小数点数で表現されるため、`0.1 + 0.2` の結果が `0.30000000000000004` になるような誤差が生じます。
金額など精度が重要な計算では整数に変換してから扱うか、専用ライブラリを使うのが基本です。

## Example
```js
console.log(3.14);
console.log(typeof 3.14); // number
```
