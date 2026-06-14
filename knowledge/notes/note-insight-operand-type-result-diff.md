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
`2 / 5` と `2.0 / 5` は演算子は同じ `/` ですが結果は `0` と `0.4` で異なります。除算前にオペランドの型を確認する習慣が、バグ防止につながります。

## Example
```java
System.out.println(2 / 5);   // 0
System.out.println(2.0 / 5); // 0.4
```
