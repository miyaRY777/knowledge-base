---
id: note-insight-character-encoding
title: "文字エンコーディングは文字を2進数へ変換するルール"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- 文字エンコーディングは、文字と数値（ビット列）を対応付けるルールです。
- 主な規格に UTF-8、UTF-16、Shift_JIS があります。
- 保存時と読み取り時のエンコーディングが一致しないと文字化けが起きます。

## Tags
#programming #character-encoding #web

## Links
- [[note-insight-ascii-code]]
- [[note-insight-unicode]]
- [[note-insight-mojibake]]
- [[note-insight-char-type]]

## Body
コンピュータは文字を直接扱えないため、文字を数値に変換するルールが必要です。そのルールを文字エンコーディングと呼びます。どの文字にどの数値を割り当てるかは規格によって異なり、規格が合わないと文字化けが発生します。現在のWebでは UTF-8 が事実上の標準です。

## Example
- UTF-8: 世界中の文字を可変長バイトで表現
- UTF-16: 主にJavaやWindowsの内部処理で使用
- Shift_JIS: 日本語向けの古い規格、レガシーシステムで使われることがある
