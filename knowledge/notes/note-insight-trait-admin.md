---
id: note-insight-trait-admin
title: "trait :adminはFactoryBotで管理者ユーザー用の追加設定をまとめる書き方"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
quiz_fail_log: []
---

## Summary
- **FactoryBotで「管理者ユーザー用の追加設定」をまとめる書き方**
- `trait` は、FactoryBotで属性のまとまりを名前付きで再利用するための機能です。`trait :admin` は Rails の特別な機能名ではなく、FactoryBot の機能です。
- テストで `create(:user, :admin)` のように使うと、管理者用の値を持つデータを作りやすくなります。 ([Thoughtbot](https://thoughtbot.github.io/factory_bot/traits/summary.html "Traits - factory_bot"))

## Tags
#rails #testing #factorybot

## Links

## Body
FactoryBot の `trait` はファクトリに「オプションの属性セット」を名前付きで追加する機能で、`create(:user, :admin)` のように組み合わせて使えます。
複数の `trait` を同時に適用することも可能で（`create(:user, :admin, :verified)`）、テストデータのバリエーションを個別のファクトリを増やさずに表現できます。
`trait` と通常の属性上書きの違いは、トレイトがファクトリ定義の再利用可能な名前付きまとまりであるのに対し、`create(:user, admin: true)` は1回限りの上書きという点です。

## Example

```ruby
FactoryBot.define do
  factory :user do
    name { "Taro" }

    trait :admin do
      admin { true }
    end
  end
end
```

このコードでは、通常の `user` に管理者用の設定を追加できるようにするために `trait :admin` を使っています。

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
