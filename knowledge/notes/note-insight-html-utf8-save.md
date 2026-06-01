---
id: note-insight-html-utf8-save
title: "HTMLファイルをUTF-8で保存するとは文字をUTF-8のバイト列として記録すること"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
---

## Summary
- エディタでHTMLを保存する際、ファイルの文字をUTF-8のバイト列として記録することです。
- `<meta charset="UTF-8">` を書くこととは別の操作です。
- VS Codeでは右下のステータスバーでエンコーディングを確認・変更できます。

## Tags
#html #character-encoding #web

## Links
- [[note-insight-unicode]]
- [[note-insight-meta-charset-utf8]]
- [[note-insight-mojibake]]
- [[note-insight-character-encoding]]

## Body
HTMLファイルをUTF-8で保存するとは、エディタが文字をディスクに書き込む際にUTF-8の変換ルールを使ってバイト列にすることです。`<meta charset="UTF-8">` はブラウザへの宣言であり、ファイルの保存形式を変える命令ではありません。ファイルの保存エンコーディングとmeta charsetの両方をUTF-8に揃えることで、文字化けを防げます。

## Example
- VS Codeでファイルを開く
- 右下の「UTF-8」表示でエンコーディングを確認
- 「エンコード付きで保存」からUTF-8を選択して保存
