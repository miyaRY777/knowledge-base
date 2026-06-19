---
id: note-insight-rounding-error
title: 丸め誤差は有限ビットで数値を表すときに生じる誤差
created: 2026-06-04
source: [[2026-06-04_insight_floating-point-type-basics]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- 丸め誤差は、コンピュータが有限のビット数で数値を表すときに発生する誤差です。
- `0.1` のような10進数の小数は2進数では正確に表せないため、近似値になります。
- `0.1 + 0.2 === 0.3` が `false` になるのは丸め誤差が原因です。

## Tags
#computer-architecture #floating-point

## Links
- [[note-insight-floating-point-type]]
- [[note-insight-ieee754]]

## Body
丸め誤差は、コンピュータが有限のビット数で実数を表す際に避けられない誤差です。10進数で `0.1` は有限小数ですが、2進数では `0.000110011...` と無限に続く循環小数になるため、近い値に丸めて保存されます。金額計算など精度が重要な場面では、浮動小数点型を避けて整数型や専用ライブラリを使うのが定石です。

## Example
```js
console.log(0.1 + 0.2);           // 0.30000000000000004
console.log(0.1 + 0.2 === 0.3);   // false
