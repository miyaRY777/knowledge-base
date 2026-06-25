---
id: note-insight-significant-figures
title: 有効数字は数値の中で信頼できる桁数
created: 2026-06-03
source: [[2026-06-03_insight_floating-point-and-scientific-notation]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- 有効数字は、測定や計算結果のうち意味を持つ（信頼できる）桁の数です。
- 浮動小数点では仮数部のビット数が有効数字の桁数を決めます。
- 有効数字を超えた桁は丸められるため、精度の限界として現れます。

## Tags
#math #floating-point #programming

## Links
- [[note-insight-mantissa]]
- [[note-insight-floating-point]]
- [[note-insight-floating-point-type]]

## Body
`3.40282 × 10^38` の仮数 `3.40282` は6桁の有効数字を持ちます。浮動小数点型では仮数部に割り当てるビット数が有効数字の桁数を決め、IEEE 754の単精度（32ビット）では約7桁、倍精度（64ビット）では約15〜17桁です。有効数字を超えた精度が必要な計算では、Rubyの `BigDecimal` やJavaScriptの `BigInt` のような専用の型を使う必要があります。

## Example
```
3.40282 × 10^38
  └── 有効数字6桁：3, 4, 0, 2, 8, 2
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
