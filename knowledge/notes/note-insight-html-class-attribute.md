---
id: note-insight-html-class-attribute
title: HTML class属性は要素に目印をつける属性
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
---

## Summary
- `class属性` はHTML要素を分類するための目印で、CSSやJavaScriptから要素を選ぶために使います。
- 同じ `class` を複数の要素に使え、1つの要素に複数の `class` をスペース区切りで付けられます。
- `id` と違い、同じ値を複数要素で共有できる点が特徴です。

## Tags
#html #css #javascript

## Links
- [[note-insight-html-attribute]]
- [[note-insight-span-element]]
- [[note-insight-css-property-value]]

## Body
`class属性` は `<p class="text-red important">` のように書き、CSSの `.text-red` セレクタや `document.querySelectorAll(".text-red")` でその要素を一括選択できます。`id` は同一ページで一意であるべきなのに対し、`class` は同じ名前を何度でも使えます。CSSフレームワーク（TailwindやBootstrapなど）は `class` に付ける名前でスタイルを決める仕組みを採用しています。

## Example
```html
<p class="text-red">重要なお知らせです</p>
<p class="text-red">もう一つの重要事項</p>
```
