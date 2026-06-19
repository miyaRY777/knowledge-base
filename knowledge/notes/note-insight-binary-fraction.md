---
id: note-insight-binary-fraction
title: 2進小数は小数部分を2のマイナス乗で表した数
created: 2026-06-12
source: [[2026-06-12_insight_js-number-types-and-floating-point]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
---

## Summary
- 2進小数では、小数点以下の各桁が `2⁻¹`（0.5）、`2⁻²`（0.25）、`2⁻³`（0.125）を表します。
- コンピュータは内部で小数をこの形式で扱います。

## Tags
#programming #binary #floating-point

## Links
- [[note-insight-decimal-to-binary-fraction]]
- [[note-insight-repeating-binary-fraction]]
- [[note-insight-binary-exact-decimal]]
- [[note-insight-floating-point]]

## Body
2進小数の各桁は2のマイナス乗で決まります。`0.011`（2進数）は `0×2⁻¹ + 1×2⁻² + 1×2⁻³ = 0.25 + 0.125 = 0.375`（10進数）です。10進数で有限の小数でも、2進小数では無限に続く場合があります。

## Example
| 2進小数 | 計算 | 10進数 |
|---|---|---|
| 0.1 | 2⁻¹ | 0.5 |
| 0.01 | 2⁻² | 0.25 |
| 0.011 | 2⁻² + 2⁻³ | 0.375 |
