---
id: note-insight-ascii-code
title: "ASCIIコードは英数字や記号を数値へ対応付ける文字コード"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
---

## Summary
- ASCIIは英語圏向けの文字コード規格で、128文字を定義しています。
- 「A」は65、「B」は66のように、文字と数値が1対1で対応しています。
- Unicodeの登場以前は主流でしたが、日本語などは扱えません。

## Tags
#character-encoding #computer #programming

## Links
- [[note-insight-unicode]]
- [[note-insight-character-encoding]]
- [[note-insight-char-type]]

## Body
ASCIIは American Standard Code for Information Interchange の略で、英数字・記号・制御文字を7ビット（128種類）で表す規格です。コンピュータ同士が文字データをやりとりする共通ルールとして普及しました。日本語などのマルチバイト文字は含まれないため、現在は Unicodeが主流です。

## Example
```
A → 65 → 01000001
B → 66 → 01000010
a → 97 → 01100001
0 → 48 → 00110000
```
