---
id: note-insight-type-promotion
title: 型の昇格は狭い範囲の型をより広い範囲の型へ変換すること
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
---

## Summary
- 型の昇格は情報を失いにくい型への変換で、整数→浮動小数点数がその代表例です。
- 多くの場合は暗黙的に行われます。

## Tags
#programming #java #data-type

## Links
- [[note-insight-implicit-type-conversion]]
- [[note-insight-mixed-type-arithmetic]]

## Body
`int` → `long` → `float` → `double` のように、表現できる範囲が広い型へ変換することを型の昇格（widening conversion）と言います。逆方向（`double` → `int`）は情報が失われる可能性があるため、明示的なキャストが必要です。

## Example
```java
int count = 5;
double result = 2.0 * count; // countがdoubleへ昇格
System.out.println(result); // 10.0
```
