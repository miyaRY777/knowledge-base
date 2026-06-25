---
id: note-insight-mojibake
title: "文字化けは保存時と読み取り時の文字コードがずれて文字が正しく表示されない現象"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- 文字化けは、保存時と読み取り時の文字エンコーディングが一致しない場合に起こります。
- 本来の文字ではなく意味不明な文字列として表示されます。
- HTMLでは保存エンコーディングと `<meta charset>` を揃えることで防げます。

## Tags
#character-encoding #web #html

## Links
- [[note-insight-character-encoding]]
- [[note-insight-encoding-save-vs-read]]
- [[note-insight-meta-charset-utf8]]
- [[note-insight-html-utf8-save]]

## Body
文字化けは、バイト列を異なるエンコーディングで解釈したときに発生します。例えばUTF-8で保存したファイルをShift_JISとして読み込むと、バイト列の意味が変わり、本来の文字と異なる文字が表示されます。HTMLでは、ファイルの保存エンコーディングとブラウザへの `<meta charset>` 宣言の両方をUTF-8に統一することが予防策です。

参考: [MDN - Character encoding](https://developer.mozilla.org/ja/docs/Glossary/Character_encoding)

## Example
- HTMLファイルを UTF-8 で保存する
- しかしブラウザが Shift_JIS として解釈する
- 「こんにちは」が「繧薙s縺ォ縺。縺ッ」のように表示される

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
