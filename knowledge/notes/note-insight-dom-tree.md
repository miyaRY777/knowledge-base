---
id: note-insight-dom-tree
title: DOMツリーはHTMLを木構造として表現したもの
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
---

## Summary
- DOMツリーは、HTMLの要素間の親子関係を木構造で表したものです。
- ブラウザはHTMLを読み込むとDOMツリーを構築し、JavaScriptから操作できるようにします。
- 要素の追加・変更・削除はすべてDOMツリーへの操作として行われます。

## Tags
#javascript #html #browser #dom

## Links
- [[note-insight-js-object]]
- [[note-insight-block-level-element]]

## Body
ブラウザはHTMLを受け取るとDOMツリーというデータ構造を内部で作ります。`<body>` の中に `<h1>` と `<p>` があれば、bodyが親・h1とpが子という親子関係のツリーになります。JavaScriptは `document.querySelector()` などでこのツリーにアクセスし、テキストの書き換えや要素の追加・削除ができます。ReactやVueのような現代のフレームワークも、DOMツリーの操作を効率よく行うために仮想DOMという仕組みを使っています。

## Example
```html
<body>
  <h1>タイトル</h1>
  <p>本文</p>
</body>
```
```
body
├── h1 → "タイトル"
└── p  → "本文"
```
