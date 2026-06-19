---
id: note-insight-boolean-default-false-null-false
title: "boolean, default: false, null: falseは真偽値カラムに初期値と空禁止を同時に設定する書き方"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- **真偽値カラムに「初期値」と「未設定禁止」を付ける指定**
- `boolean` は `true / false` を入れる型です。`default: false` は何も指定しなかったときの初期値を `false` にし、`null: false` は `nil`を保存できないようにします。3値状態を避けて、判定をわかりやすくしたいときによく使います。`default` はDBの既存データへの反映がDB依存になることがある点に注意が必要です。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_migrations.html "Active Record Migrations — Ruby on Rails Guides"))
- add_column :users, :admin, :boolean, default: false, null: false

## Tags
#rails #activerecord #database

## Links

## Body
`boolean` カラムに `null: false` を付けないと、値が `true / false / nil` の3種類になり、`nil.!` などの判定でバグが起きやすくなります。
`default: false` と組み合わせることで「未設定のまま保存される」ことを防ぎ、常に `true` か `false` だけを保証できます。
既存テーブルへの追加では、`default` の値がDBに即座に反映されるかはDBの実装によって異なるため、マイグレーション後の動作確認が必要です。

## Example

```ruby
add_column :users, :admin, :boolean, default: false, null: false
```

このコードでは、`admin` を true / false で管理しつつ、未設定の `nil` を防ぐために `default: false, null: false` を使っています。
