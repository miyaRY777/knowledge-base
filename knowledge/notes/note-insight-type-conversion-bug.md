---
id: note-insight-type-conversion-bug
title: 型変換によるバグは想定外の型変換で発生するプログラムの不具合
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
quiz_phase: 1
quiz_streak: 0
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- 整数除算の結果が代入先の `double` 変数に入ると `0.0` になるなど、意図しない結果が起きます。
- 代入先の型ではなく、計算時点のオペランドの型が結果を決めます。

## Tags
#programming #java #data-type

## Links
- [[note-insight-integer-division-truncation]]
- [[note-insight-operand-type-result-diff]]
- [[note-insight-division-type-cast]]

## Body
`double rate = correctAnswers / totalQuestions;` では、除算は `int` 同士で行われるため整数除算になり結果は `0`。それが `double` に代入されて `0.0` になります。代入先が `double` でも計算時点の型を変換しないと意図した結果になりません。

## Example
```java
int correctAnswers = 2;
int totalQuestions = 5;
double rate = correctAnswers / totalQuestions; // 0.0（バグ）
double fixed = (double) correctAnswers / totalQuestions; // 0.4（正しい）
```
