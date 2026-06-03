---
id: note-insight-floating-point
title: 浮動小数点は小数点位置を指数で動かせる数の表し方
created: 2026-06-03
source: [[2026-06-03_insight_floating-point-and-scientific-notation]]
---

## Summary
- 浮動小数点は、仮数と指数を使って小数点の位置を動かしながら数を表す方式です。
- 非常に大きい数から非常に小さい数まで幅広く扱えますが、精度には限界があります。
- 固定小数点と対になる概念で、コンピュータの小数表現の主流です。

## Tags
#programming #data-type #binary #math

## Links
- [[note-insight-scientific-notation]]
- [[note-insight-floating-point-type]]
- [[note-insight-fixed-point-type]]
- [[note-insight-mantissa]]
- [[note-insight-exponent]]

## Body
浮動小数点は「仮数 × 基数^指数」の形で数を表し、指数を変えることで小数点の位置を動かせます。固定小数点が小数点位置を固定するのに対し、浮動小数点は非常に広い範囲の数を扱えます。ただし仮数部に使えるビット数には限りがあるため、細かい小数を正確に表せないことがあり、`0.1 + 0.2` が `0.30000000000000004` になるような誤差が生じます。
