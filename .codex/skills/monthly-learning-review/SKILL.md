---
name: monthly-learning-review
description: Use when creating or updating a monthly learning map in the local knowledge-base repository, reviewing the month's inbox/notes/maps, grouping themes, summarizing key concepts, and preparing the next month's carry-over items.
---

# Monthly Learning Review Skill

対象リポジトリ:
- `/Users/miyary777/workspace/miyaRY777/knowledge-base`

このスキルの役割:
- 月次の入口 MOC を新規作成または更新する
- 今月の主要テーマを整理する
- 関連するテーマ別 MOC を洗い出す
- 今月の重要概念、未決事項、次月への持ち越しをまとめる

まず読むもの:
- 手順は `references/checklist.md`
- 月次 MOC の形は `references/monthly-template.md`

## 使う場面

- `map-YYYY-MM-learning.md` を作りたい
- 今月学んだ内容をまとめ直したい
- テーマ別 MOC を月次の入口からたどれるようにしたい
- 来月の課題や未決事項を整理したい

## 前提

- 日常の取り込みやノート化は `knowledge-base` スキル側で行う
- 月次レビューは、その結果できた `inbox / notes / maps` をまとめる

## 実行ルール

- 月次 MOC は「入口」であり、個別の詳細はテーマ別 MOC やノートに委譲する
- 今月のテーマは 3〜6 個程度にまとめる
- 重要概念は 5〜8 件程度に絞る
- 未決事項は来月に持ち越すものだけ残す
- 既存の月次 MOC がある場合は追記・更新を優先する

## 成果物

- `knowledge/maps/map-YYYY-MM-learning.md`
- 必要に応じたテーマ別 MOC へのリンク整理

## 実行例

- `2026年4月学習マップを作る`
- `2026-04 の月次 MOC を更新する`
- `今月の notes と maps を見て月次レビューを作る`
