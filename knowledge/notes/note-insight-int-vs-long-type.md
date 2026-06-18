---
id: note-insight-int-vs-long-type
title: "int型とlong型は扱える整数の大きさが異なる"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 2
last_reviewed_on: 2026-06-18
---

## Summary
- `long型` は `int型` より大きな整数を扱えます。
- 実際のビット数は言語や環境によって異なります。
- Javaでは `int` が32ビット、`long` が64ビットです。

## Tags
#programming #data-type #computer

## Links
- [[note-insight-signed-integer-type]]
- [[note-insight-integer-overflow]]

## Body
int型とlong型はどちらも整数を扱いますが、保持できる値の範囲が異なります。Javaでは `int` は32ビット（約±21億）、`long` は64ビット（約±922京）です。人口や金額など int の範囲を超える大きな数値には long を使います。long 型のリテラルには末尾に `L` を付けます。

## Example
```java
int count = 100;
long population = 8000000000L;  // 80億 → int では表現できない
```
