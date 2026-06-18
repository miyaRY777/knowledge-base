---
id: note-insight-division-type-cast
title: 除算時の型変換で整数除算を避けて小数結果を得る
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
quiz_streak: 0
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
Javaでは整数 ÷ 整数 の計算は「整数除算」として扱われ、小数点以下が切り捨てられます。たとえば `2 / 5` は `0` になります。

小数の結果を得るには、どちらか一方を浮動小数点型に変換（キャスト）します。`(double) total` と書くと `total` だけが `double` に変換され、その後の `/` は浮動小数点除算として計算されます。

キャストの優先度は `/` より高いため、`(double) total / count` は `(double)(total / count)` ではなく `((double) total) / count` として動作します。

## Example
```java
int total = 2;
int count = 5;
double result = (double) total / count;
System.out.println(result); // 0.4
```
