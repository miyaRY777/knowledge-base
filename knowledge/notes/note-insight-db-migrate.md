---
id: note-insight-db-migrate
title: "db:migrateは未反映のマイグレーションをデータベースに適用するRailsコマンド"
created: 2026-04-07
source: [[2026-04-07_insight_rails-ruby-terms.md]]
quiz_fail_log: []
---

## Summary
- `db:migrate` は未反映の migration を DB に適用するコマンドです。
- テーブル作成やカラム追加などの構造変更に使います。
- migration ファイルを取得したあとによく使います。

## Tags
#rails #database #migration

## Links
- [[note-insight-git-branch-switch-does-not-switch-db]]
- [[note-insight-db-create]]
- [[note-insight-rails-db-prepare]]

## Body
`bin/rails db:migrate` は、まだ実行していない migration を DB に反映するコマンドです。テーブルを作る、カラムを追加する、カラム名を変えるといった DB の構造変更を適用するときに使います。

Git で新しい migration ファイルを取得したあとや、ローカルで migration を作成したあとに実行して、コードと DB 構造を一致させます。

## Example
```bash
bin/rails db:migrate
```

このコードでは、migration に書かれた DB 構造の変更を反映するために `db:migrate` を使っています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] `db:migrate` と `db:rollback` の使い分けも整理する
