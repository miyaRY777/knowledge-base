---
id: note-insight-kaminari-gap-and-render
title: "Kaminariではgap表示とrenderでページネーション部品を組み立てる"
created: 2026-04-24
source: [[2026-04-24_insight_kaminari-pagination-partials.md]]
quiz_fail_log: []
---

## Summary
- `_gap.html.erb` はページ数が多いときの省略記号を表示する。
- `render` はパーシャルを組み合わせて最終的なHTMLを作る。
- Kaminari では全体テンプレートと個別パーシャルを `render` によって組み立てる理解が重要。

## Tags
#insight #rails #kaminari #render #view

## Links
- [[note-insight-kaminari-paginator-partial-role]]
- [[note-insight-format-html-redirect-notice]]

## Body
`_gap.html.erb` は、ページ番号をすべて並べると長くなりすぎる場面で、途中を `...` と省略表示するための補助パーツです。これは移動リンクではなく、ページネーションを見やすく保つための表示要素です。

また、Kaminari のページネーションは 1 つのテンプレートだけで完結しているわけではありません。`render` によって `_paginator.html.erb` の中に各種パーシャルが組み合わされ、最終的なHTMLになります。今回の理解では、コントローラの `render` 一般論よりも、「ビューの部品を組み立てる仕組み」として捉えるのが実用的です。

## Example
```erb
<span class="gap">...</span>
<%= render "shared/header" %>
```

このコードでは、`gap` は省略表示の見た目を担当し、`render` は別のビュー部品を呼び出して画面を組み立てています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
