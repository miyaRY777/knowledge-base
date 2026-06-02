---
id: note-insight-block-level-element
title: ブロックレベル要素は横幅いっぱいを使い前後で改行される
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
---

## Summary
- ブロックレベル要素は、ページの大きな構造を作る要素で、横幅いっぱいに広がります。
- 前後に改行が入るため、要素が縦に積み重なって表示されます。
- 代表例は `div`、`p`、`h1`〜`h6` などです。

## Tags
#html #css #layout

## Links
- [[note-insight-inline-element]]
- [[note-insight-span-element]]

## Body
ブロックレベル要素は、見出し・段落・セクションのようにページの骨格を作る要素です。デフォルトで親要素の横幅いっぱいを占め、前後に改行が入ります。現代のHTMLでは「ブロックレベル要素」という分類よりもコンテンツカテゴリー（フロー・ヘディング・フレージングなど）という考え方が使われますが、CSSの `display: block` の挙動として理解しておくと実用的です。

## Example
```html
<div>
  <p>これは段落です</p>
</div>
```
