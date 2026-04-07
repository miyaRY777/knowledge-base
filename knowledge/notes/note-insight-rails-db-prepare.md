---
id: note-insight-rails-db-prepare
title: db:prepareの要点
created: 2026-04-07
source: [[2026-04-07_insight_rails-ruby-terms.md]]
---

## Summary
- `db:prepare` は DB を使える状態にまとめて整えるコマンドです。
- 必要に応じて DB 作成、schema の読み込み、migration の実行を行います。
- clone 直後など、最初の環境準備で使いやすいコマンドです。

## Tags
#rails #database #setup

## Links
- [[note-insight-db-create]]
- [[note-insight-db-migrate]]
- [[note-insight-db-seed]]

## Body
`bin/rails db:prepare` は、DB がなければ作成し、必要に応じて schema の読み込みや migration の実行を行って、DB を使える状態に整えるコマンドです。Rails Guides では、`db:setup` に近いが idempotent で、必要な処理だけを行うコマンドとして説明されています。

clone 直後や開発環境を整えたいときに便利ですが、内部でどの条件で `db:create`、schema 読み込み、`db:migrate` を使い分けているかは別途整理すると理解が深まります。

## Example
```bash
bin/rails db:prepare
```

このコードでは、DB をまとめて使える状態に整えるために `db:prepare` を使っています。

## Action
- [ ] `db:prepare` の内部動作を Rails Guides ベースで確認する
