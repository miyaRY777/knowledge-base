---
id: note-insight-division-type-cast
title: 除算時の型変換で整数除算を避けて小数結果を得る
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
---

## Summary
- Javaで整数除算を避けるには、オペランドの少なくとも一方を浮動小数点型にキャストします。
- `(double) total / count` のように変換先の型を指定します。

## Tags
#java #data-type

## Links
- [[note-insight-cast]]
- [[note-insight-float-division]]
- [[note-insight-integer-division-truncation]]

## Body
整数変数同士の除算では自動的に整数除算になります。`(double)` キャストで一方を `double` へ変換することで小数結果が得られます。キャストは `/` より優先度が高いため `(double) total / count` で意図通りに動作します。

## Example
```java
int total = 2;
int count = 5;
double result = (double) total / count;
System.out.println(result); // 0.4
```
