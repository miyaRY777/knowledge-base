---
id: note-insight-css-property-value
title: CSSのプロパティ:値は見た目の設定を書く基本構文
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- CSS宣言は `プロパティ: 値;` の形で書き、どの見た目をどう変えるかを指定します。
- `color: red;` なら `color` がプロパティ、`red` が値です。
- セレクタ＋中括弧の中に複数の宣言をまとめてルールセットを作ります。

## Tags
#css #frontend

## Links
- [[note-insight-html-class-attribute]]
- [[note-insight-html-attribute]]

## Body
CSSの宣言は「何を（プロパティ）どのように（値）」を指定するペアです。`font-size: 16px;` や `background-color: #fff;` のように書きます。複数の宣言はセレクタと中括弧でまとめてルールセットにします。HTMLの `属性名="値"` と混同しやすいですが、CSSはコロン区切り・セミコロン終端、HTMLはイコールとダブルクォートという違いがあります。

## Example
```css
p {
  color: red;
  font-size: 16px;
}
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
