---
id: note-insight-decimal-to-binary-fraction
title: 10進小数を2進小数に変換するには小数部に2を掛けて整数部を取り出す
created: 2026-06-12
source: [[2026-06-12_insight_js-number-types-and-floating-point]]
quiz_phase: 1
quiz_streak: 0
quiz_fail_streak: 0
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
10進小数を2進数に変換するには、小数部分に2を掛けて整数部（0か1）を順番に取り出す操作を繰り返します。
`0.1` や `0.2` は2進数で割り切れず循環小数になります。これが `0.1 + 0.2 = 0.30000000000000004` になる理由で、コンピュータが10進数を完全に表現できないことを示します。
10進数で有限の小数でも2進数で無限になる場合があり、IEEE 754 は一定ビット数で打ち切るため誤差が生じます。

## Example
`0.375` の変換：
- `0.375 × 2 = 0.75` → 整数部 **0**
- `0.75 × 2 = 1.5` → 整数部 **1**
- `0.5 × 2 = 1.0` → 整数部 **1**（小数部が0で終了）
- 結果：`0.011`（2進数）
