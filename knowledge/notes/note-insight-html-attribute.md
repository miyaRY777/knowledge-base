---
id: note-insight-html-attribute
title: HTMLの属性は要素に追加設定を与える属性名="値"の形
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
quiz_streak: 1
---

## Summary
- HTML属性は `属性名="値"` の形でHTML要素の開始タグに書き、動作や設定を追加します。
- `href`（リンク先）、`src`（画像パス）、`class`（分類）、`id`（識別子）などが代表例です。
- 属性によって使える要素や意味が異なるため、適切な属性を選ぶことが重要です。

## Tags
#html

## Links
- [[note-insight-html-class-attribute]]
- [[note-insight-form-action-attribute]]
- [[note-insight-html-label]]

## Body
HTML属性は要素に追加の情報や設定を与えるための仕組みです。`<a href="https://example.com">` の `href` や、`<input type="text" name="username">` の `type`・`name` がその例です。属性名と値はイコールで結び、値はダブルクォートで囲みます。グローバル属性（`class`・`id`・`style` など）はほぼすべての要素で使えますが、`href` は `<a>` や `<link>` など特定の要素にしか使えない属性もあります。

## Example
```html
<a href="https://example.com">リンク</a>
<input type="text" name="username">
<p class="highlight" id="intro">紹介文</p>
```
