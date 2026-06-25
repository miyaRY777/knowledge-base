---
id: note-insight-char-type
title: "char型は1文字を文字コードとして保存するデータ型"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- `char型` は1文字を保存するためのデータ型です。
- 内部的には文字コード（数値）として保存されます。
- 言語によって `char`（C/Java）、`String`（Java）などがあります。

## Tags
#programming #data-type #character-encoding

## Links
- [[note-insight-character-encoding]]
- [[note-insight-ascii-code]]
- [[note-insight-unicode]]

## Body
コンピュータは文字を直接扱えないため、文字をいったん数値（文字コード）に変換して保存します。`char型` はその1文字分の文字コードを格納するための型です。C言語では1バイト（ASCIIコード）、Javaでは2バイト（Unicode）として扱われます。複数の文字をまとめた型が `String`（文字列型）です。

## Example
```c
char grade = 'A';  // 内部では 65 として保存される
```

```java
char grade = 'A';   // Unicodeの U+0041 = 65
String name = "Alice";
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
