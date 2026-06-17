---
id: note-insight-operand-type-result-diff
title: オペランドのデータ型によって演算結果が変わる
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
---

## Summary
- 同じ演算子でもオペランドの型が異なると結果が変わります。
- 特に除算では整数型か浮動小数点型かで結果が大きく異なります。

## Tags
#programming #java #data-type

## Links
- [[note-insight-operand-type]]
- [[note-insight-integer-division-truncation]]
- [[note-insight-float-division]]
- [[note-insight-type-conversion-bug]]

## Body
`2 / 5` と `2.0 / 5` は演算子は同じ `/` ですが、Javaでは前者が `0`（整数除算）、後者が `0.4`（浮動小数点除算）と結果が異なります。
これはオペランドの型が演算の種類を決定するためです。型を変えるには明示的キャスト `(double) 2 / 5` が必要です。
「演算子が同じなら結果も同じ」という思い込みが典型的なバグの原因になるため、除算では特に注意が必要です。

## Example
```java
System.out.println(2 / 5);   // 0
System.out.println(2.0 / 5); // 0.4
```
