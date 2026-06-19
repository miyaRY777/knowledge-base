---
id: note-insight-unicode
title: "Unicodeは世界中の文字を統一的に扱うための文字コード規格"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- Unicodeは日本語・英語・中国語・絵文字など世界中の文字を共通の仕組みで扱う規格です。
- 各文字にはコードポイント（U+xxxx形式）が割り当てられています。
- 現在のWebやアプリでは事実上の標準で、UTF-8がよく使われます。

## Tags
#character-encoding #web #programming

## Links
- [[note-insight-ascii-code]]
- [[note-insight-character-encoding]]
- [[note-insight-html-utf8-save]]
- [[note-insight-meta-charset-utf8]]

## Body
Unicodeは、世界中で使われる文字を一つの規格で管理するための文字コード標準です。ASCIIが英語圏のみを対象としていたのに対し、Unicodeは100万以上のコードポイントを定義し、あらゆる言語や絵文字をカバーします。実際のバイト列への変換方式（エンコーディング）はUTF-8やUTF-16などがあります。

## Example
- A → U+0041
- あ → U+3042
- 😀 → U+1F600
- 日 → U+65E5
