---
id: note-insight-kaminari-paginator-partial-role
title: Kaminariの_paginator.html.erbはページネーション全体の構造を決める
created: 2026-04-24
source: [[2026-04-24_insight_kaminari-pagination-partials.md]]
---

## Summary
- `_paginator.html.erb` はページネーション全体の枠組みを定義する。
- 前へ、ページ番号、次へをどの順で並べるかをここで決める。
- 各ボタンの見た目そのものは個別パーシャルに分かれている。

## Tags
#insight #rails #kaminari #view #要復習

## Links
- [[2026-04-24-pagination]]

## Body
`_paginator.html.erb` は、Kaminari が描画するページネーション全体のレイアウトを担当するビューです。どのパーツをどの順番で表示するかを決める土台で、個々のリンクのHTMLを細かく書く場所というより、全体の骨組みを組み立てる役割を持ちます。

そのため、前へボタン、各ページ番号、次へボタンをどう並べるかを調整したいときは `_paginator.html.erb` を見るのが起点になります。逆に、ページ番号1個だけの見た目を変えたい場合は別のパーシャルを編集します。

## Example
```erb
<nav>
  <%= paginator.render do %>
    <%= prev_page_tag %>
    <%= each_page do |page| %>
      <%= page_tag page %>
    <% end %>
    <%= next_page_tag %>
  <% end %>
</nav>
```

このコードでは、ページネーション全体の構造を `_paginator.html.erb` 側で定義し、その中に各パーツを並べています。

## Action
- [ ] Kaminari カスタムビューを読むときは、まず `_paginator.html.erb` と個別パーシャルの責務を分けて確認する

<!-- review_log: 2026-04-25 -->
