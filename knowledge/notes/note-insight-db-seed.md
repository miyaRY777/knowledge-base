---
id: note-insight-db-seed
title: db:seedの要点
created: 2026-04-07
source: [[2026-04-07_insight_rails-ruby-terms.md]]
---

## Summary
- `db:seed` は `db/seeds.rb` の初期データを DB に投入するコマンドです。
- 管理者ユーザーやマスターデータの投入でよく使います。
- 何度も実行される前提で、重複しにくい書き方が大切です。

## Tags
#rails #database #seed

## Links
- [[note-insight-db-create]]
- [[note-insight-rails-db-prepare]]

## Body
`bin/rails db:seed` は、`db/seeds.rb` に書いたデータを DB に投入するコマンドです。管理者ユーザー、都道府県、カテゴリ一覧のように、最初に入れておきたい初期データや参照データを登録するときによく使います。

seed は一度だけでなく複数回実行されることもあるため、重複しにくい書き方にしておくことが重要です。たとえば `find_or_create_by!` を使うと、同じデータを二重に作りにくくできます。

## Action
- [ ] `db/seeds.rb` を idempotent に書く代表例を別ノートにする
