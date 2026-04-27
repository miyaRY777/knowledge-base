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

## resource-inbox テンプレート

NotebookLM、YouTube、Qiita、Zenn などの外部資料まとめは、以下の形式を基本にして `knowledge/resources/inbox/` に保存する。

保存時は、記事タイプに合う見出しだけを残す。空の見出しは残さない。

```markdown
---
title: ""
type: resource-inbox
category: ""
resource_kind: "" # tool / library / article / news / comparison / postmortem / essay / video / course
topics:
  -
source_type: notebooklm
source_author: ""
source_url: ""
related_sources:
  -
created: YYYY-MM-DD
status: inbox
---

# タイトル

## 背景

## 課題

## 後で取り出したい価値

-
-
-

## 要点

-
-
-

## 導入の流れ

1.
2.
3.

## 具体的な使い方

-
-

## 使える場面

-
-

## 比較軸

-
-

## 判断基準

-
-

## 原因

-
-

## 対策

-
-

## 自分への問い

-
-

## 注意点

-
-

## distill候補

-
-

## 元ソース

- 著者:
- URL:

## 保存判断

これは外部資料の整理なので、`knowledge/notes/` には直接保存しない。
必要になったら後で `distill` して atomic note 化を検討する。
```

### 任意セクションの使い分け

- `導入の流れ`: ツール、ライブラリ、サービスの場合に使う
- `具体的な使い方`: ツール、ライブラリ、実践記事の場合に使う
- `使える場面`: ユースケースが明確な場合に使う
- `比較軸`: 比較記事の場合に使う
- `判断基準`: 選定、比較、意思決定に使える資料の場合に使う
- `原因`: 失敗談、障害報告、ポストモーテムの場合に使う
- `対策`: 失敗談、障害報告、ポストモーテムの場合に使う
- `自分への問い`: 思想、エッセイ、学習方針の記事の場合に使う

### 保存時ルール

- 空の見出しは残さない
- 記事タイプに合う任意セクションだけを選ぶ
- NotebookLMの文章はそのまま貼らず、自分の言葉で要約する
- 外部資料や調査ログは `knowledge/notes/` に直接保存しない
- note 化したい内容は、後で `distill` して atomic note 化を検討する
