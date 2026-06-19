---
id: note-insight-unsigned-integer-type
title: "符号なし整数型は0以上の整数だけを扱うデータ型"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- 符号なし整数型は負の数を持たず、0以上の整数のみを扱います。
- 符号ビットが不要な分、同じビット数でより大きな正の数を表現できます。
- 8ビット符号なし整数の範囲は 0 〜 255です。

## Tags
#programming #data-type #computer

## Links
- [[note-insight-signed-integer-type]]
- [[note-insight-integer-overflow]]

## Body
符号なし整数型（unsigned int）は、負の数を扱わないため全ビットを値の表現に使えます。その結果、同じビット数の符号付き整数より2倍の正の値を表現できます。カウンタや配列の添字など、負の値が不要な場面で使われます。

## Example
```c
unsigned int score = 100;  // 0以上の整数のみ
// unsigned int の8ビット版: 0〜255
// signed int の8ビット版: -128〜127
```
