---
id: note-insight-db-seed
title: db:seedの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- `db/seeds.rb`** の初期データをDBに入れるコマンド**
- `db:seed` は `db/seeds.rb` を読み込んで、初期データや参照データを投入するときに使います。新しい環境を作ったときや、開発環境をそろえたいときによく使います。何度も実行する可能性があるので、重複しにくい書き方にすることが大切です。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/command_line.html "The Rails Command Line — Ruby on Rails Guides"))
- bin/rails db:seed

## Tags
#rails #http #database

## Links
- [[関連ノート]]

## Body
`db/seeds.rb`** の初期データをDBに入れるコマンド**

**解説：**
`db:seed` は `db/seeds.rb` を読み込んで、初期データや参照データを投入するときに使います。新しい環境を作ったときや、開発環境をそろえたいときによく使います。何度も実行する可能性があるので、重複しにくい書き方にすることが大切です。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/command_line.html "The Rails Command Line — Ruby on Rails Guides"))

具体例：

```bash
bin/rails db:seed
```

このコードでは、`db/seeds.rb` に書いた初期データをデータベースへ投入するために `db:seed` を使っています。
