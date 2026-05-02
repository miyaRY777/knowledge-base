---
id: note-insight-db-seed
title: "db:seedの要点"
created: 2026-04-07
source: [[2026-04-07_insight_rails-ruby-terms.md]]
---

## Summary
- `db:seed` は `db/seeds.rb` の初期データを DB に投入するコマンドです。
- 管理者ユーザーやマスターデータの投入でよく使います。
- 何度も実行される前提で、重複しにくい書き方が大切です。
- テスト DB に seed を入れると、前提データが混ざって再現性を崩しやすいです。

## Tags
#rails #database #seed

## Links
- [[note-insight-db-create]]
- [[note-insight-rails-db-prepare]]

## Body
`bin/rails db:seed` は、`db/seeds.rb` に書いたデータを DB に投入するコマンドです。管理者ユーザー、都道府県、カテゴリ一覧のように、最初に入れておきたい初期データや参照データを登録するときによく使います。

seed は一度だけでなく複数回実行されることもあるため、重複しにくい書き方にしておくことが重要です。たとえば `find_or_create_by!` を使うと、同じデータを二重に作りにくくできます。

一方で、テスト DB に seed をそのまま入れるのは注意が必要です。テストは毎回同じ前提で実行できることが大切ですが、seed 済みのデータが最初から入っていると「何もない状態」を前提にしたテストが崩れたり、実行順によって結果が変わる不安定なテストになったりします。テストでは seed に依存せず、必要なデータだけをテスト内で明示的に作るのが基本です。

## Example
```ruby
User.find_or_create_by!(email: "admin@example.com") do |user|
  user.password = "password"
  user.admin = true
end
```

このコードでは、初期ユーザーを DB に投入するときに、重複しにくい形で seed データを作っています。

## Action
- [ ] `db/seeds.rb` を idempotent に書く代表例を別ノートにする
