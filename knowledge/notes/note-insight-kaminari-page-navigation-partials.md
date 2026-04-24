---
id: note-insight-kaminari-page-navigation-partials
title: Kaminariの個別パーシャルはページ番号や前後移動の見た目を担当する
created: 2026-04-24
source: [[2026-04-24_insight_kaminari-pagination-partials.md]]
---

## Summary
- `_page.html.erb` はページ番号リンク1件分を描画する。
- `_prev_page.html.erb` と `_next_page.html.erb` は前後移動を担当する。
- `_first_page.html.erb` と `_last_page.html.erb` は先頭・末尾へのジャンプ用に使う。

## Tags
#insight #rails #kaminari #view

## Links
- [[note-insight-kaminari-paginator-partial-role]]
- [[2026-04-24-pagination]]

## Body
Kaminari のページネーションでは、全体レイアウトとは別に、各リンクの役割ごとにパーシャルが分かれています。`_page.html.erb` は「1」「2」「3」のようなページ番号1件分を表し、現在ページかどうかでCSSや見た目を変えるのもここで行います。

`_prev_page.html.erb` と `_next_page.html.erb` は前後移動のリンク、`_first_page.html.erb` と `_last_page.html.erb` は先頭ページや末尾ページへのジャンプを担当します。つまり、どのボタンを出すかは `_paginator.html.erb`、各ボタンの具体的なHTMLは個別パーシャル、という分担です。

## Example
```erb
<%= link_to page, url, class: "page-link" %>
<%= link_to "←", url, class: "prev" %>
<%= link_to "→", url, class: "next" %>
```

このコードでは、ページ番号や前後移動リンクをそれぞれの役割ごとに描画しています。

## Action
- [ ] ページ番号だけ見た目を変えたいときは `_page.html.erb` を編集対象にする
