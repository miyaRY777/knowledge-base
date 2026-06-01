---
id: note-insight-encoding-save-vs-read
title: "保存時の文字コードと読み取り時の文字コードを揃えることで文字化けを防ぐ"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
---

## Summary
- 保存時の文字コードはファイルへ書き込むときに使うルールです。
- 読み取り時の文字コードはブラウザやエディタがバイト列を解釈するときに使うルールです。
- 2つを一致させることで文字化けを防げます。

## Tags
#character-encoding #web #html

## Links
- [[note-insight-mojibake]]
- [[note-insight-html-utf8-save]]
- [[note-insight-meta-charset-utf8]]
- [[note-insight-character-encoding]]

## Body
文字化けを防ぐには「どのルールで保存したか」と「どのルールで読み取るか」を一致させる必要があります。HTMLの場合、エディタでUTF-8として保存し、かつ `<meta charset="UTF-8">` でブラウザへ宣言することで、両者が揃います。どちらか片方だけでは不十分なケースがあります。

## Example
- 保存時：エディタで UTF-8 として保存
- 宣言：`<meta charset="UTF-8">` を記述
- 読み取り時：ブラウザが UTF-8 として解釈
- 結果：日本語が正しく表示される
