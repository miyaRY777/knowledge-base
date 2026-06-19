---
id: note-insight-meta-charset-utf8
title: "<meta charset=\"UTF-8\">はブラウザにHTML文書をUTF-8として読んでもらうための宣言"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- `<meta charset="UTF-8">` はHTMLの文字エンコーディングをブラウザへ伝える宣言です。
- ファイル自体をUTF-8に変換する命令ではありません。
- `<head>` の先頭付近に記述するのが推奨されます。

## Tags
#html #character-encoding #web

## Links
- [[note-insight-html-utf8-save]]
- [[note-insight-unicode]]
- [[note-insight-mojibake]]

## Body
`<meta charset="UTF-8">` は、ブラウザに対して「この文書はUTF-8で読んでください」と伝えるための宣言です。ファイルの保存エンコーディングを変える効果はありません。ブラウザはこの宣言を見てバイト列の解釈方法を決めます。ファイルをUTF-8で保存しつつこの宣言も書くことで、文字化けを防げます。

参考: [MDN - meta charset](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#charset)

## Example
```html
<head>
  <meta charset="UTF-8">
  <title>ページタイトル</title>
</head>
```
