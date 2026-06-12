---
id: note-insight-decimal-to-binary-fraction
title: 10進小数を2進小数に変換するには小数部に2を掛けて整数部を取り出す
created: 2026-06-12
source: [[2026-06-12_insight_js-number-types-and-floating-point]]
---

## Summary
- 小数部分に2を掛け、結果の整数部分を順番に並べる方法で変換します。
- 小数部が0になれば終了ですが、無限に続く場合もあります（循環小数）。

## Tags
#programming #binary #floating-point

## Links
- [[note-insight-binary-fraction]]
- [[note-insight-repeating-binary-fraction]]

## Body
10進小数を2進小数に変換する手順は以下の通りです。小数部分に2を掛け、整数部分（0か1）を取り出すことを繰り返します。10進数で有限の小数でも、変換が無限ループになる場合があります。

## Example
`0.375` の変換：
- `0.375 × 2 = 0.75` → 整数部 **0**
- `0.75 × 2 = 1.5` → 整数部 **1**
- `0.5 × 2 = 1.0` → 整数部 **1**（小数部が0で終了）
- 結果：`0.011`（2進数）
