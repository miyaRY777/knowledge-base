---
id: note-insight-trait-admin
title: trait :adminの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **FactoryBotで「管理者ユーザー用の追加設定」をまとめる書き方**
- `trait` は、FactoryBotで属性のまとまりを名前付きで再利用するための機能です。`trait :admin` は Rails の特別な機能名ではなく、FactoryBot の機能です。
- テストで `create(:user, :admin)` のように使うと、管理者用の値を持つデータを作りやすくなります。 ([Thoughtbot](https://thoughtbot.github.io/factory_bot/traits/summary.html?utm_source=chatgpt.com "Traits - factory_bot"))

## Tags
#rails #http #testing

## Links
- [[関連ノート]]

## Body
**FactoryBotで「管理者ユーザー用の追加設定」をまとめる書き方**

**解説：**
`trait` は、FactoryBotで属性のまとまりを名前付きで再利用するための機能です。`trait :admin` は Rails の特別な機能名ではなく、FactoryBot の機能です。

テストで `create(:user, :admin)` のように使うと、管理者用の値を持つデータを作りやすくなります。 ([Thoughtbot](https://thoughtbot.github.io/factory_bot/traits/summary.html?utm_source=chatgpt.com "Traits - factory_bot"))

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
