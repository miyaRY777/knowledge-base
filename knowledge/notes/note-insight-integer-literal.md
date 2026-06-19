---
id: note-insight-integer-literal
title: 整数リテラルは整数を直接コードに書いた値
created: 2026-06-11
source: [[2026-06-11_insight_js-data-types-and-literals]]
quiz_phase: 1
quiz_streak: 0
quiz_fail_streak: 0
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
整数リテラルはコードに直接書いた整数値です。JavaScriptには専用の整数型がなく `number` 型として扱われますが、`2^53 - 1` を超える整数は精度が保証されません。
大きな整数を扱う場合は `BigInt`（`9007199254740993n` のように末尾に `n`）を使います。
また `0xff`（16進数）や `0b1010`（2進数）のリテラル表記も整数リテラルの一種です。

## Example
```js
console.log(10);
console.log(2048);
console.log(typeof 10); // number
```
