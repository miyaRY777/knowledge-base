---
id: note-insight-boolean-default-false-null-false
title: boolean, default: false, null: falseの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **真偽値カラムに「初期値」と「未設定禁止」を付ける指定**
- `boolean` は `true / false` を入れる型です。`default: false` は何も指定しなかったときの初期値を `false` にし、`null: false` は `nil`を保存できないようにします。3値状態を避けて、判定をわかりやすくしたいときによく使います。`default` はDBの既存データへの反映がDB依存になることがある点に注意が必要です。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_migrations.html "Active Record Migrations — Ruby on Rails Guides"))
- add_column :users, :admin, :boolean, default: false, null: false

## Tags
#rails #activerecord #http #database

## Links
- [[関連ノート]]

## Body
**真偽値カラムに「初期値」と「未設定禁止」を付ける指定**

**解説：**
`boolean` は `true / false` を入れる型です。`default: false` は何も指定しなかったときの初期値を `false` にし、`null: false` は `nil`を保存できないようにします。3値状態を避けて、判定をわかりやすくしたいときによく使います。`default` はDBの既存データへの反映がDB依存になることがある点に注意が必要です。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_migrations.html "Active Record Migrations — Ruby on Rails Guides"))

## Example

```ruby
add_column :users, :admin, :boolean, default: false, null: false
```

このコードでは、`admin` を true / false で管理しつつ、未設定の `nil` を防ぐために `default: false, null: false` を使っています。
