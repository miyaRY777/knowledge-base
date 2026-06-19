---
id: note-insight-float-division
title: 浮動小数点数を含む除算では小数部分を含む結果が得られる
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
---

## Summary
- 少なくとも一方のオペランドを浮動小数点型にすると小数部分を含む除算になります。
- Java・C++ で整数除算を避けたいときに使うテクニックです。

## Tags
#programming #java #data-type

## Links
- [[note-insight-integer-division-truncation]]
- [[note-insight-division-type-cast]]
- [[note-insight-type-promotion]]

## Body
`2 / 5` は整数除算で `0` になりますが、`2.0 / 5` にすると `5` が `double` へ昇格し `0.4` が得られます。どちらのオペランドを浮動小数点型にしてもよく、キャストで変換する方法もあります。

## Example
```java
System.out.println(2 / 5);   // 0（整数除算）
System.out.println(2.0 / 5); // 0.4（float除算）
System.out.println(2 / 5.0); // 0.4（float除算）
```
