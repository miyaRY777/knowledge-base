---
id: note-insight-span-element
title: spanは文章の一部を囲む汎用インライン要素
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
---

## Summary
- `span` はそれ自体に意味を持たない汎用のインライン要素です。
- CSSでスタイルを当てたり、JavaScriptで操作する対象にするために使います。
- 意味を持たせたい場合は `strong`・`em` など適切な要素を優先すべきです。

## Tags
#html #css

## Links
- [[note-insight-inline-element]]
- [[note-insight-html-class-attribute]]

## Body
`span` は「この部分だけ色を変えたい」「ここだけJSで書き換えたい」という場面で使う入れ物です。`div` のブロック版に対してインライン版の汎用コンテナと考えると覚えやすいです。意味的なマークアップ（強調・引用など）が必要な場合は `strong` や `em` を使うべきで、`span` は純粋にスタイルや操作の目印として使うのが適切です。

## Example
```html
<p>今日は <span class="important">重要</span> な日です。</p>
```
