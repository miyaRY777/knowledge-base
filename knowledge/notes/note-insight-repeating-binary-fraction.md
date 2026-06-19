---
id: note-insight-repeating-binary-fraction
title: 循環小数は同じ数字の並びが無限に繰り返される小数
created: 2026-06-12
source: [[2026-06-12_insight_js-number-types-and-floating-point]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
---

## Summary
- 循環小数は、小数部分が同じパターンを無限に繰り返す数です。
- 10進数では有限小数でも、2進数に変換すると循環小数になる場合があります（例：`0.1`）。
- 浮動小数点誤差の根本的な原因です。

## Tags
#programming #binary #floating-point

## Links
- [[note-insight-binary-fraction]]
- [[note-insight-decimal-to-binary-fraction]]
- [[note-insight-rounding-error]]
- [[note-insight-binary-exact-decimal]]

## Body
`0.1` を2進数に変換すると `0.00011001100110011...` となり、`0011` が永遠に繰り返されます。有限のビット数しか持てないコンピュータは途中で打ち切るしかなく、これが浮動小数点誤差の原因になります。

## Example
```js
console.log(0.1 + 0.2); // 0.30000000000000004
// 0.1も0.2も2進数で正確に表せないため誤差が生じる
```
