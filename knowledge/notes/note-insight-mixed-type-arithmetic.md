---
id: note-insight-mixed-type-arithmetic
title: 異なるデータ型同士の演算では一方の型が変換されることがある
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
---

## Summary
- 型の異なる値を組み合わせた計算では、多くの言語で一方が自動変換されます。
- 結果の型や変換ルールは言語によって異なります。

## Tags
#programming #java #data-type

## Links
- [[note-insight-implicit-type-conversion]]
- [[note-insight-type-promotion]]
- [[note-insight-mixed-type-expression]]

## Body
JavaやC++では整数と浮動小数点数を一緒に計算すると、整数が浮動小数点数へ昇格して計算されます。これを理解していないと除算で意図しない整数結果になるバグが起きます。

## Example
```java
double result = 2.0 + 5; // 5がdoubleへ変換されて7.0
System.out.println(result); // 7.0
```
