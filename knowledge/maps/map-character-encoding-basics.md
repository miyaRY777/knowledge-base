# 文字エンコーディング基礎マップ

> **このMOCで分かること**: 文字コードの仕組み（ASCII・Unicode・UTF-8）から、HTMLでの文字化け防止まで一連の流れを俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | char型 | 1文字を文字コードとして保存するデータ型 | [[note-insight-char-type]] |
| 2 | 文字エンコーディング | 文字を2進数へ変換するルール | [[note-insight-character-encoding]] |
| 3 | ASCIIコード | 英数字・記号を数値に対応付ける文字コード | [[note-insight-ascii-code]] |
| 4 | Unicode | 世界中の文字を統一的に扱うための文字コード規格 | [[note-insight-unicode]] |
| 5 | HTMLをUTF-8で保存する | ファイルの文字をUTF-8バイト列として記録すること | [[note-insight-html-utf8-save]] |
| 6 | `<meta charset="UTF-8">` | ブラウザにHTML文書をUTF-8として読ませる宣言 | [[note-insight-meta-charset-utf8]] |
| 7 | 文字化け | 保存と読み取りの文字コードがずれて正しく表示されない現象 | [[note-insight-mojibake]] |
| 8 | 保存時と読み取り時の文字コード | 両方を揃えることで文字化けを防ぐ | [[note-insight-encoding-save-vs-read]] |

---

## 文字コードの仕組み

[[note-insight-char-type]]
[[note-insight-character-encoding]]
[[note-insight-ascii-code]]
[[note-insight-unicode]]

**ポイント**:
- コンピュータは文字を直接扱えないため、文字 → 数値 → ビット列の変換が必要
- `char型` は1文字分の文字コード（数値）を格納する型
- ASCIIは英語圏向けの128文字規格。`A = 65` のように文字と数値が対応
- Unicodeはあらゆる言語・絵文字を統一管理する規格。`A = U+0041`、`あ = U+3042`
- UTF-8はUnicodeの文字をバイト列に変換するエンコーディング方式

---

## HTMLと文字コードの実践

[[note-insight-html-utf8-save]]
[[note-insight-meta-charset-utf8]]
[[note-insight-encoding-save-vs-read]]
[[note-insight-mojibake]]

**ポイント**:
- 「ファイルをUTF-8で保存」はエディタが行う操作。`<meta charset>` とは別
- `<meta charset="UTF-8">` はブラウザへの宣言。ファイルの保存形式を変える命令ではない
- 文字化けは「保存したエンコーディング」と「読み取るエンコーディング」がずれて起きる
- 両方をUTF-8に揃えること（保存 + meta charset宣言）が基本の対策

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| UTF-8とUTF-16のバイト構造の違いを整理する | - | - | [[note-insight-unicode]] |
| Shift_JISが今でも使われるケースを整理する | - | - | [[note-insight-character-encoding]] |

---

## 関連リンク

- [[map-data-types-and-binary-basics]]
- [[map-web-security-basics]]
