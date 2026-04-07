---
id: note-insight-git-branch-switch-does-not-switch-db
title: Gitでブランチを切り替えてもDBは自動で切り替わらない
created: 2026-04-07
source: [[2026-04-07_insight_rails-ruby-terms.md]]
---

## Summary
- Git のブランチ切り替えで変わるのは主にコードや migration ファイルです。
- ローカルの DB 本体は自動では切り替わりません。
- そのため、コードが期待する DB 構造と実際の DB 構造がズレることがあります。

## Tags
#git #rails #database

## Links
- [[note-insight-db-migrate]]
- [[note-insight-db-create]]
- [[note-insight-rails-db-prepare]]

## Body
Git でブランチを切り替えると、リポジトリで管理されているコードや migration ファイルは切り替わります。一方で、開発環境の DB はローカルにある実体なので、自動で元に戻ったり別ブランチ用に切り替わったりはしません。

そのため、今のコードが前提にしているテーブル構造やカラム構成と、実際の DB の状態が一致しないことがあります。Rails では migration を実行して DB 構造をそろえる必要があります。

## Action
- [ ] ブランチ切り替え後に DB 構造がズレたときの確認手順を整理する
