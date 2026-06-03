---
id: note-insight-floating-point-type
title: 浮動小数点型は小数を扱うプログラミングのデータ型
created: 2026-06-03
source: [[2026-06-03_insight_floating-point-and-scientific-notation]]
---

## Summary
- 浮動小数点型は、小数や非常に大きい・小さい数を扱うためのデータ型です。
- JavaScriptの `Number` 型はIEEE 754の倍精度64ビット浮動小数点数として実装されています。
- 精度の限界から `0.1 + 0.2` が `0.30000000000000004` になるような誤差が生じます。

## Tags
#programming #javascript #data-type #floating-point

## Links
- [[note-insight-floating-point]]
- [[note-insight-significant-figures]]
- [[note-insight-fixed-point-type]]
- [[note-insight-integer-vs-string]]

## Body
浮動小数点型はプログラミング言語で小数を扱う標準的な型です。JavaScriptでは整数も小数も `Number` 型として浮動小数点で扱われ、Pythonでは `float`、Javaでは `float`（32ビット）と `double`（64ビット）があります。精度の限界は実務でも影響があり、金額計算などで誤差が許容できない場合は整数（最小単位の「銭」で管理するなど）や専用ライブラリを使う設計が必要です。

## Example
```js
console.log(0.1 + 0.2); // 0.30000000000000004
console.log(0.1 + 0.2 === 0.3); // false
```
