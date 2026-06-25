---
id: note-insight-mixed-type-arithmetic
title: 異なるデータ型同士の演算では一方の型が変換されることがある
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
quiz_phase: 1
quiz_streak: 0
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- 型の異なる値を組み合わせた計算では、多くの言語で一方が自動変換されます。
- 結果の型や変換ルールは言語によって異なります。

## Tags
#programming #java #data-type

## Links
- [[note-insight-implicit-type-conversion]]
- [[note-insight-type-promotion]]
- [[note-insight-mixed-type-expression]]

## Body
JavaやC++で整数と浮動小数点数を混在させると、整数が浮動小数点数へ自動昇格（型の昇格）して計算されます。
この昇格は暗黙的に行われるため、`int / int` を意図していたのに浮動小数点除算になるバグや逆に整数除算になるバグが起きやすいです。
意図を明確にするため、計算前に明示的にキャスト（`(double) 2 / 5`）するのが安全です。

## Example
```java
double result = 2.0 + 5; // 5がdoubleへ変換されて7.0
System.out.println(result); // 7.0
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
