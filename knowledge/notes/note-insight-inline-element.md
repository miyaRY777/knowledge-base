---
id: note-insight-inline-element
title: インライン要素は文章の一部として横に並ぶ
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- インライン要素は、文章の流れの中に入り込んで横に並ぶ要素です。
- 前後に改行が入らず、コンテンツの幅だけを占めます。
- 代表例は `span`、`a`、`strong`、`em` などです。

## Tags
#html #css #layout

## Links
- [[note-insight-block-level-element]]
- [[note-insight-span-element]]

## Body
インライン要素は、段落や見出しの中に部分的に挿入して使う要素です。`<p>今日は<strong>重要</strong>な日です</p>` のように、文章を壊さずに一部だけ強調したりリンクにしたりできます。現代のHTMLではCSSの `display: inline` の挙動として捉えるのが正確ですが、「文章の途中に使う」という感覚で覚えておくと実践的です。

## Example
```html
<p>これは <span>大事な部分</span> です。</p>
```
