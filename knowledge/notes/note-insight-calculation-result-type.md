---
id: note-insight-calculation-result-type
title: 計算結果のデータ型はオペランドの型と演算子と言語の規則で決まる
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
---

## Summary
- 計算結果の型は代入先ではなく、演算時点のオペランドの型と言語の規則で決まります。
- 代入先を `double` にしても除算が整数同士なら整数結果になります。

## Tags
#programming #java #data-type

## Links
- [[note-insight-operator-result-type]]
- [[note-insight-type-conversion-bug]]
- [[note-insight-operand-type-result-diff]]

## Body
`double result = 2 / 5;` は `2 / 5` が先に整数除算で `0` になり、その後 `double` の `0.0` として代入されます。計算結果の型を決めるのは代入先ではなく演算時点のオペランドです。

## Example
```java
double result = 2 / 5;    // 0.0（整数除算→代入）
double fixed = 2.0 / 5;   // 0.4（float除算）
```
