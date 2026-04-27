---
title: Resources
type: resource-index
created: 2026-04-27
---

# Resources

## 目的

`knowledge/resources/` は、外部資料、リンク集、調査ログ、ツール運用メモを置く場所。

YouTube、Qiita、Zenn、GitHub、Reddit、Hacker News、last30days の調査結果など、外部から集めた材料はまずここに保存する。

## notes には保存しない

外部資料や調査ログは、`knowledge/notes/` に直接保存しない。

`knowledge/notes/` は、自分の言葉で抽出した atomic note を置く場所。外部記事の要約、動画メモ、last30days の出力、リンク集は、そのまま note にしない。

note 化したい場合は、後で `distill` し、既存ノートとの重複を確認したうえで、自分の理解として再構成する。

## ディレクトリ

- `inbox/`: 未整理の外部資料、リンク、調査候補
- `last30days/`: last30days skill の運用メモと調査ログ
- `ruby-on-rails/`: Ruby on Rails 関連の外部資料
- `computer-science/`: コンピュータサイエンス関連の外部資料
- `react/`: React 関連の外部資料

## 運用ルール

- 保存前に案を確認する
- 外部資料は `resources` に保存する
- `resources/inbox` は外部資料専用にする
- `knowledge/inbox` は自分の気づきや学習メモ用に残す
- ノート本文はコピペせず、自分の言葉で要約する
- 重要な学びだけを後で `notes` に distill する
