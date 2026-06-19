---
id: note-insight-scientific-notation
title: 指数表記は大きな数を仮数×基数^指数で短く表す書き方
created: 2026-06-03
source: [[2026-06-03_insight_floating-point-and-scientific-notation]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- 指数表記は、非常に大きい数や小さい数を「仮数 × 基数^指数」の形で短く表す書き方です。
- `3.4 × 10^38` のように書くことで、長い数値を簡潔に表現できます。
- 浮動小数点数の仕組みの土台となる考え方です。

## Tags
#math #programming #floating-point

## Links
- [[note-insight-floating-point]]
- [[note-insight-mantissa]]
- [[note-insight-exponent]]
- [[note-insight-radix]]

## Body
指数表記は `仮数 × 基数^指数` の形で数を表します。`340000000000000000000000000000000000000` のような長い数を `3.4 × 10^38` と短く書けます。日常では10進数（基数10）を使いますが、コンピュータ内部では2進数（基数2）の指数表記が浮動小数点数の基礎になっています。
