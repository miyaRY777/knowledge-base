---
id: note-insight-db-create
title: db:createの要点
created: 2026-04-07
source: [[2026-04-07_insight_rails-ruby-terms.md]]
---

## Summary
- `db:create` はデータベース自体を作るコマンドです。
- テーブル作成やデータ投入までは行いません。
- その後に `db:migrate` や `db:seed` が必要になることがあります。

## Tags
#rails #database

## Links
- [[note-insight-db-migrate]]
- [[note-insight-db-seed]]
- [[note-insight-rails-db-prepare]]

## Body
`bin/rails db:create` は、`config/database.yml` の設定をもとにデータベース自体を作るコマンドです。まだ DB が存在しないときに使います。

このコマンドは空の DB を作るところまでが役割で、テーブル作成や seed データの投入までは行いません。そのため、必要に応じてこのあとに `db:migrate` や `db:seed` を実行します。

## Example
```bash
bin/rails db:create
```

このコードでは、空のデータベース自体を作るために `db:create` を使っています。

## Action
- [ ] `db:create` と `db:prepare` の違いを表で整理する
