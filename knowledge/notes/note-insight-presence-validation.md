---
id: note-insight-presence-validation
title: "presenceバリデーションは値が空でないことを確認する"
created: 2026-05-04
source: [[2026-05-04_insight_rails-model-basics]]
review_streak: 0
last_reviewed_on: 2026-05-25
quiz_fail_log: []
---

## Summary
- `presence` バリデーションは、値が空ではないことを保存前に確認する仕組みです。
- 名前やメールアドレスのように必ず入力してほしい項目で使います。
- 空文字や `nil` のまま保存されるのを防ぐために役立ちます。

## Tags
#rails #validation #model

## Links
- [[note-insight-rails-presence]]
- [[note-insight-ruby-rails-presence-predicate-comparison]]

## Body
`presence` バリデーションは、Rails の Model で「この値は空のまま保存してはいけない」というルールを表す仕組みです。ユーザー名、メールアドレス、プロフィール名のように、アプリの動作や表示に必要な項目でよく使います。

Rails の `presence` メソッドは「空なら `nil` にする」用途ですが、`presence: true` のバリデーションは「空なら保存を止める」用途です。名前は似ていますが、前者は値を扱うメソッド、後者は保存時の検証ルールとして考えると区別しやすいです。

## Example
```ruby
class Profile < ApplicationRecord
  validates :adventurer_name, presence: true
end
```

このコードでは、`adventurer_name` が空のまま保存されないようにしています。

## Action
- [ ] `blank?` 判定との関係を整理する
