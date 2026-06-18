---
id: note-insight-exponent
title: 指数は小数点をどれだけ動かすかを表す数
created: 2026-06-03
source: [[2026-06-03_insight_floating-point-and-scientific-notation]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
---

## Summary
- 指数は `3.4 × 10^38` の `38` にあたる部分で、小数点の移動量を表します。
- 指数が正の数なら大きい数、負の数なら小さい数を表します。
- 浮動小数点では指数部に割り当てるビット数が表現できる数の範囲を決めます。

## Tags
#math #floating-point #programming

## Links
- [[note-insight-scientific-notation]]
- [[note-insight-mantissa]]
- [[note-insight-floating-point]]

## Body
指数表記 `仮数 × 基数^指数` の中で、指数は小数点を何桁動かすかを表します。`10^38` なら小数点を右に38桁動かす（大きい数）、`10^-27` なら小数点を左に27桁動かす（小さい数）ことを意味します。浮動小数点型では指数部のビット数が数値の表現範囲（どれだけ大きい・小さい数まで扱えるか）を決めます。

## Example
- `3.4 × 10^38` → 小数点を右に38桁移動（巨大な数）
- `1.67 × 10^-27` → 小数点を左に27桁移動（極小の数）
