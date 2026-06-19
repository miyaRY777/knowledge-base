---
id: note-insight-floating-point-type
title: 浮動小数点型は小数を扱うプログラミングのデータ型
created: 2026-06-03
source: [[2026-06-03_insight_floating-point-and-scientific-notation]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- 浮動小数点型は、小数や非常に大きい・小さい数を扱うためのデータ型です。
- 「仮数 × 基数^指数」の形で数を表し、指数を変えることで小数点の位置を動かせます。
- JavaScriptの `Number` 型はIEEE 754の倍精度64ビット浮動小数点数として実装されています。
- 精度の限界から `0.1 + 0.2` が `0.30000000000000004` になるような誤差が生じます。

## Tags
#programming #javascript #data-type #floating-point #binary

## Links
- [[note-insight-fixed-point-type]]
- [[note-insight-repeating-binary-fraction]]
- [[note-insight-ieee754]]
- [[note-insight-significant-figures]]
- [[note-insight-integer-vs-string]]

## Body
浮動小数点は「仮数 × 基数^指数」の形で数を表し、指数を変えることで小数点の位置を動かせます。固定小数点が小数点位置を固定するのに対し、非常に大きい数から非常に小さい数まで幅広く扱えるのが特徴です。

プログラミング言語では、この方式をデータ型として実装したものが浮動小数点型です。JavaScriptでは整数も小数も `Number` 型として浮動小数点で扱われ、Pythonでは `float`、Javaでは `float`（32ビット）と `double`（64ビット）があります。仮数部に使えるビット数には限りがあるため細かい小数を正確に表せないことがあり、金額計算などで誤差が許容できない場合は整数（最小単位の「銭」で管理するなど）や専用ライブラリを使う設計が必要です。

## Example
```js
console.log(0.1 + 0.2); // 0.30000000000000004
console.log(0.1 + 0.2 === 0.3); // false
```
