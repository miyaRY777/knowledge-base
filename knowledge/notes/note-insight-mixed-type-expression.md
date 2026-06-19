---
id: note-insight-mixed-type-expression
title: 混合型演算は異なるデータ型の値を含む演算
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
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
混合型演算は、整数と浮動小数点数など異なる型のオペランドが1つの式に混在している状態です。
多くの言語では「より広い型」へ自動変換（型の昇格）が起きるため、`2 * 5.0` は `int` と `double` の混在により `double` として計算され `10.0` になります。
意図しない型変換によるバグを防ぐには、計算前にオペランドの型を統一するか、明示的キャストを行います。

## Example
```java
double result = 2 * 5.0;
System.out.println(result); // 10.0
```
