---
id: note-insight-mantissa
title: 仮数は指数表記における数字の本体部分
created: 2026-06-03
source: [[2026-06-03_insight_floating-point-and-scientific-notation]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- 仮数は `3.4 × 10^38` の `3.4` にあたる、数値の本体部分です。
- 浮動小数点では仮数に使えるビット数が精度を決めます。
- 仮数の桁数が少ないと、細かい値を正確に表せず丸め誤差が生じます。

## Tags
#math #floating-point #programming

## Links
- [[note-insight-scientific-notation]]
- [[note-insight-exponent]]
- [[note-insight-significant-figures]]
- [[note-insight-floating-point]]

## Body
指数表記 `仮数 × 基数^指数` の中で、仮数は「数の実質的な値」を担う部分です。`3.4 × 10^38` なら `3.4` が仮数です。浮動小数点型では仮数部に割り当てるビット数が有効桁数を決めるため、仮数部が大きいほど精度が高くなります。IEEE 754の倍精度（64ビット）では仮数部に52ビットを使い、約15〜17桁の有効数字を持ちます。
