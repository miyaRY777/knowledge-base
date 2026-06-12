---
id: note-insight-integer-range
title: 整数型の値の範囲はビット数によって決まる
created: 2026-06-12
source: [[2026-06-12_insight_js-number-types-and-floating-point]]
---

## Summary
- 整数型で扱える値には上限と下限があり、使用するビット数によって決まります。
- 範囲を超えるとエラーや意図しない値になる場合があります。
- 広い範囲が必要なら64ビット整数など、より大きい型を使います。

## Tags
#programming #data-type #integer

## Links
- [[note-insight-integer-data-type]]
- [[note-insight-32bit-integer]]
- [[note-insight-int-vs-long-type]]
- [[note-insight-integer-overflow]]

## Body
コンピュータのメモリは有限なので、整数型には必ず表現できる範囲があります。符号付き32ビット整数では一般的に `-2,147,483,648` から `2,147,483,647` まで。その範囲を超える値が必要な場合は、64ビット整数型などを選択します。

## Example
- 符号付き32ビット：`-2³¹` 〜 `2³¹ - 1`（約±21億）
- 符号付き64ビット：`-2⁶³` 〜 `2⁶³ - 1`（約±922京）
