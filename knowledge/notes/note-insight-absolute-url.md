---
id: note-insight-absolute-url
title: 絶対URLは通信方式からパスまで省略なく書くURL
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- 絶対URLは `https://` から始まり、スキーム・ドメイン・パスをすべて含むURLです。
- どのページから参照しても同じ場所を指すため、外部サイトへのリンクに使います。
- 相対URLに対して「場所を省略せず完全に書いたURL」と覚えると区別しやすいです。

## Tags
#html #web #url

## Links
- [[note-insight-relative-url]]
- [[note-insight-html-attribute]]
- [[note-insight-domain-name]]

## Body
絶対URLは `https://example.com/about.html` のように、通信方式（スキーム）・ドメイン・パスをすべて含む完全なURLです。どのHTMLファイルに書いても必ず同じ場所を指すため、別サイトへのリンクや画像のCDN参照などに使われます。相対URLと違って参照元の場所に影響されません。

## Example
```html
<a href="https://example.com/about.html">このサイトについて</a>
<img src="https://cdn.example.com/images/logo.png" alt="ロゴ">
```
