# Kaminariページネーション基礎マップ

> **このMOCで分かること**: Kaminari のページネーションを、全体テンプレート・個別パーシャル・省略表示の役割から整理できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | paginator partial | ページネーション全体の構造を決める | [[note-insight-kaminari-paginator-partial-role]] |
| 2 | page navigation partials | ページ番号や前後移動の見た目を担当する | [[note-insight-kaminari-page-navigation-partials]] |
| 3 | gap と render | 省略表示と部品の組み立てを理解する | [[note-insight-kaminari-gap-and-render]] |

---

## セクション1: 全体構造

[[note-insight-kaminari-paginator-partial-role]]

**ポイント**:
- `_paginator.html.erb` は、ページネーション全体をどう並べるかを見る入口になる
- 個別リンクの細かい見た目とは責務を分けて理解する

---

## セクション2: 個別パーツ

[[note-insight-kaminari-page-navigation-partials]]
[[note-insight-kaminari-gap-and-render]]

**ポイント**:
- ページ番号、前へ、次へ、先頭、末尾はそれぞれ役割ごとにパーシャルが分かれる
- gap はページ数が多いときの省略表示で、移動リンクではない
- `render` はビュー部品を組み合わせて画面を作る入口として読む

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| Kaminari のカスタムビュー生成手順を実コードで確認する | - | - | [[note-insight-kaminari-paginator-partial-role]] |
| gap 表示が出るページ数条件を具体例で確認する | - | - | [[note-insight-kaminari-gap-and-render]] |

---

## 関連リンク

- [[note-insight-kaminari-paginator-partial-role]]
- [[note-insight-kaminari-page-navigation-partials]]
- [[note-insight-kaminari-gap-and-render]]
- [[2026-04-24-pagination]]
