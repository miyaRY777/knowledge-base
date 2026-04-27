---
title: last30days skill
type: resource
source: https://github.com/mvanhorn/last30days-skill
status: candidate
created: 2026-04-27
---

# last30days skill

## 概要

`last30days` は、あるトピックについて直近30日ほどの動きを調べるためのCodex/AIエージェント向けスキル。

通常のWeb記事検索だけでなく、Reddit、Hacker News、GitHub、YouTube、TikTok、X、Polymarketなどの反応を横断して、最近の話題や関心の集まり方を整理する用途に向いている。

## knowledge-baseでの位置づけ

このリポジトリでは、atomic note としてではなく、外部調査ツールの `resource` として扱う。

主な用途は CODE サイクルの `Collect` 段階。新しい技術、企業、プロダクト、人物、論点について、最近の外部動向を把握するための材料集めに使う。

`last30days` の出力や調査ログは、`knowledge/notes/` に直接保存しない。

保存する場合は `knowledge/resources/last30days/` に置く。note 化したい場合は、後で `distill` し、既存ノートとの重複を確認したうえで、自分の言葉で再構成する。

## 使いどころ

- 新しい技術やツールについて、直近の評判や論点を調べる
- Reddit、HN、GitHubなどで何が注目されているかを把握する
- 月次レビューやMOC更新の前に、外部トレンドを確認する
- 比較テーマの材料を集める
- 学習前に、そのテーマが今どの文脈で語られているかを見る
- 日本語圏ではQiitaやZennも確認し、国内での受け止め方や実装例を補う

## 日本語圏の補助確認先

日本語圏の技術トピックを調べる場合は、`last30days` の結果だけでなく、以下も補助的に確認する。

- Qiita: 日本語の実装メモ、入門記事、現場寄りのTipsを確認する
- Zenn: 比較的新しい技術記事、設計・学習ログ・個人の検証記事を確認する

QiitaやZennの内容は、SNSやGitHub上の反応とは性質が違うため、恒久的な知識として扱う前に、公式ドキュメントや一次情報と照合する。

## 注意点

- 出力をそのまま `knowledge/notes/` に保存しない
- 調査ログは `knowledge/resources/last30days/` に保存する
- ノート化するときは、自分の言葉で要約する
- SNSやWeb上の反応は一時的なものなので、恒久的な知識と区別する
- 重複ノートを増やすより、既存ノートやMOCへの接続を優先する
- 実行にはAPIキーやネットワーク権限が必要になる可能性がある

## Codexでの導入候補

このスキルはCodex向けに扱える構造を持っている。

リポジトリ内に `.codex-plugin/plugin.json` があり、`skills/last30days` をスキルとして公開する構成になっている。

導入候補コマンド:

```bash
python3 /Users/miyary777/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo mvanhorn/last30days-skill --path skills/last30days
```

導入後はCodexの再起動が必要。

## 導入判断

現時点では、まず `resource` として管理する。

実際に直近30日の外部動向調査を何度も行うようになったら、Codex skill としてインストールする。
