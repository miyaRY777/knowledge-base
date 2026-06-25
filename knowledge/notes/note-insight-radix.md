---
id: note-insight-radix
title: 基数は何進数かを示す土台の数
created: 2026-06-03
source: [[2026-06-03_insight_floating-point-and-scientific-notation]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- 基数は `3.4 × 10^38` の `10` にあたる部分で、何進数を使っているかを示します。
- 10進数なら基数は `10`、2進数なら基数は `2` です。
- コンピュータ内部の浮動小数点では基数2（2進数）が使われます。

## Tags
#math #binary #floating-point #programming

## Links
- [[note-insight-scientific-notation]]
- [[note-insight-floating-point]]
- [[note-insight-binary-data]]

## Body
基数は数の進法を決める土台の数です。日常で使う10進数は基数10、コンピュータが扱う2進数は基数2、16進数は基数16です。浮動小数点の文脈では「`仮数 × 基数^指数`」の基数を指し、IEEE 754では基数2（2進数）を採用しています。基数が変わると同じビット列でも解釈が変わるため、プログラミングで進数変換を行う際に意識する概念です。

## Example
- `3.4 × 10^38`：基数は `10`（10進数）
- `1.01 × 2^3`：基数は `2`（2進数）

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
