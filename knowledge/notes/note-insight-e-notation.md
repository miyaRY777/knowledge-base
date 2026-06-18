---
id: note-insight-e-notation
title: E表記は指数表記をプログラムで書きやすくした記法
created: 2026-06-03
source: [[2026-06-03_insight_floating-point-and-scientific-notation]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
---

## Summary
- E表記は `× 10^n` を `En` や `E+n`、`E-n` の形で書く指数表記の省略記法です。
- `3.4E+38` は `3.4 × 10^38` と同じ意味です。
- JavaScriptを含む多くのプログラミング言語でそのまま数値リテラルとして使えます。

## Tags
#programming #javascript #floating-point #math

## Links
- [[note-insight-scientific-notation]]
- [[note-insight-floating-point-type]]

## Body
E表記は `×10^n` をキーボードで打ちやすくするために `E` で代替した記法です。`E` の後の数がプラスなら大きい数、マイナスなら小さい数を表します。JavaScriptでは `3.4E+38` と書くと数値リテラルとして直接使え、`console.log(3.4E+38)` のように利用できます。

## Example
```js
console.log(3.4E+38);   // 3.4 × 10^38
console.log(1.67E-27);  // 1.67 × 10^-27
```
