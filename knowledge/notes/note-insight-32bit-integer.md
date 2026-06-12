---
id: note-insight-32bit-integer
title: 32ビット整数は2³²通りのビットパターンで整数を表す
created: 2026-06-12
source: [[2026-06-12_insight_js-number-types-and-floating-point]]
---

## Summary
- 32ビット整数は32個の0と1を使い、`2³² = 4,294,967,296` 通りの値を表現します。
- 符号付きの場合は負の数と正の数に分け、一般的に `-2³¹` 〜 `2³¹ - 1` の範囲になります。
- Javaの `int` は32ビット符号付き整数として定義されています。

## Tags
#programming #data-type #integer #java

## Links
- [[note-insight-integer-range]]
- [[note-insight-signed-integer-type]]
- [[note-insight-int-vs-long-type]]

## Body
32ビットで表現できるビットパターンは `2³² = 約43億` 通りです。符号付きとして使う場合は、半分を負の数に割り当てるため、`-2,147,483,648` 〜 `2,147,483,647` の範囲になります。Javaの `int` 型はこの仕様に従います。

## Example
```java
int max = 2147483647;   // Integer.MAX_VALUE
int min = -2147483648;  // Integer.MIN_VALUE
```
