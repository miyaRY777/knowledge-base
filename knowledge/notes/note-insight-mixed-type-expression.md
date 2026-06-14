---
id: note-insight-mixed-type-expression
title: 混合型演算は異なるデータ型の値を含む演算
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
---

## Summary
- 混合型演算は整数と浮動小数点数など異なる型を組み合わせた計算の総称です。
- 特定の言語機能名ではなく、一般的な概念として使われます。

## Tags
#programming #java #data-type

## Links
- [[note-insight-mixed-type-arithmetic]]
- [[note-insight-type-promotion]]
- [[note-insight-operand-type-result-diff]]

## Body
`2 * 5.0` のように整数と浮動小数点数が混在する式が混合型演算です。多くの言語では型の昇格により浮動小数点数として計算されます。

## Example
```java
double result = 2 * 5.0;
System.out.println(result); // 10.0
```
