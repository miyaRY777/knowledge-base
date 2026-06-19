---
id: note-insight-integer-division-truncation
title: 整数除算では小数部分が切り捨てられて整数の結果になる
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
quiz_phase: 1
quiz_streak: 0
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- Java・C++ の整数型同士の除算では小数部分が保持されず切り捨てられます。
- 四捨五入ではなくゼロ方向への切り捨てです。

## Tags
#programming #java #data-type

## Links
- [[note-insight-integer-division]]
- [[note-insight-float-division]]
- [[note-insight-type-conversion-bug]]

## Body
`7 / 2` の数学的な答えは `3.5` ですが、Java の `int` 型同士では `3` になります。小数部分は単純に除去されます（`-7 / 2` は `-3`、ゼロ方向）。正確な小数結果が必要なら少なくとも一方を `double` にする必要があります。

## Example
```java
int result = 7 / 2;
System.out.println(result); // 3（3.5の小数部分が切り捨て）
```
