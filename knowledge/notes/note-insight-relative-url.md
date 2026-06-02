---
id: note-insight-relative-url
title: 相対URLは現在の場所を基準に指定するURL
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
---

## Summary
- 相対URLは、現在のHTMLファイルのURLを基準にして別の場所を指定する書き方です。
- `https://` から始まらず、`about.html` や `../images/logo.png` のように書きます。
- 同じサイト内のリンクや画像の参照に使われることが多いです。

## Tags
#html #web #url

## Links
- [[note-insight-absolute-url]]
- [[note-insight-html-attribute]]

## Body
相対URLはドメインやプロトコルを省略して書くURLです。ブラウザが「現在のページのURL＋相対パス」で完全なURLを補完します。同じサイト内のページにリンクを張るとき、絶対URLより短く書けて管理しやすい利点があります。ただし、ページの場所が変わると相対URLが指す先も変わるため注意が必要です。

## Example
```html
<!-- 同じディレクトリのページへ -->
<a href="about.html">このサイトについて</a>

<!-- 上のディレクトリの画像 -->
<img src="../images/logo.png" alt="ロゴ">
```
