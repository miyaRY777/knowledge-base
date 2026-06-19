---
id: note-insight-cast
title: キャストは値を指定したデータ型として扱う明示的な型変換
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
---

## Summary
- キャストは変換先の型をコード上で明示的に指定する型変換です。
- 情報が失われる変換（`double` → `int`）も強制的に行えますが注意が必要です。

## Tags
#java #programming #data-type

## Links
- [[note-insight-explicit-type-conversion]]
- [[note-insight-division-type-cast]]
- [[note-insight-type-promotion]]

## Body
Javaでは `(型名)` を値の前に書くことでキャストできます。広い型→狭い型（`double` → `int`）のキャストは小数部分が切り捨てられます。JavaScriptでは `Number()` / `parseInt()` などの関数がキャストに相当します。

## Example
```java
double pi = 3.14;
int truncated = (int) pi;
System.out.println(truncated); // 3（小数部分が切り捨て）

int total = 2;
double result = (double) total / 5;
System.out.println(result); // 0.4
```
