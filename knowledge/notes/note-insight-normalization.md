---
id: note-insight-normalization
title: 正規化は指数表記の形を一定ルールにそろえること
created: 2026-06-03
source: [[2026-06-03_insight_floating-point-and-scientific-notation]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- 正規化とは、指数表記の仮数部を一定のルールにそろえて表現を統一することです。
- 10進数では仮数の整数部が1桁になるよう `3.40282 × 10^38` の形にそろえます。
- 同じ値でも正規化されていないと比較や演算が複雑になるため、統一が重要です。

## Tags
#math #floating-point #programming

## Links
- [[note-insight-scientific-notation]]
- [[note-insight-mantissa]]
- [[note-insight-floating-point]]

## Body
`34.0282 × 10^37`、`3.40282 × 10^38`、`0.340282 × 10^39` はすべて同じ値ですが、表し方が異なります。正規化はこうした揺れをなくし、仮数の整数部が必ず1桁（10進数なら1〜9）になる形にそろえる操作です。浮動小数点のIEEE 754では仮数部の先頭ビットが常に `1` になるよう正規化し、その `1` を省略（暗黙ビット）することで精度を1ビット分節約しています。

## Example
```
正規化前：34.0282 × 10^37
正規化後：3.40282 × 10^38  ← 仮数の整数部が1桁
```
