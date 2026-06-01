---
id: note-insight-signed-integer-type
title: "int型（符号付き整数型）は正と負の整数を扱えるデータ型"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
---

## Summary
- `int型` は正の数・負の数を含む整数を保存するデータ型です。
- 符号付きのため、ビットの一部を符号（+/-）の表現に使います。
- 32ビットintの範囲は −2,147,483,648 〜 2,147,483,647です。

## Tags
#programming #data-type #computer

## Links
- [[note-insight-unsigned-integer-type]]
- [[note-insight-integer-overflow]]
- [[note-insight-int-vs-long-type]]

## Body
符号付き整数型（int型）は、負の数も含む整数を扱うデータ型です。最上位ビットを符号ビットとして使うことで、正負の両方を表現します。符号付きにした分、同じビット数では符号なし整数より最大値が小さくなります。

## Example
```c
int score = -10;  // 負の値も保存できる
int count = 100;  // 正の値も保存できる
```
