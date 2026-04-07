---
id: note-insight-find-or-create-by-bang
title: find_or_create_by!の要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **見つけるか、なければ作るメソッド（失敗時は例外）**
- `find_or_create_by!` は、条件に合うレコードを探して、なければ新しく作ります。新規作成時にバリデーションで失敗すると例外を出すのが `!` 付きの特徴です。seedやマスターデータ投入でよく使われます。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/v7.0.2/active_record_querying.html "Active Record Query Interface — Ruby on Rails Guides"))
- ParentTag.find_or_create_by!(name: "ゲーム")

## Tags
#rails #activerecord #http

## Links
- [[関連ノート]]

## Body
**見つけるか、なければ作るメソッド（失敗時は例外）**

**解説：**
`find_or_create_by!` は、条件に合うレコードを探して、なければ新しく作ります。新規作成時にバリデーションで失敗すると例外を出すのが `!` 付きの特徴です。seedやマスターデータ投入でよく使われます。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/v7.0.2/active_record_querying.html "Active Record Query Interface — Ruby on Rails Guides"))

## Example

```ruby
ParentTag.find_or_create_by!(name: "ゲーム")
```

このコードでは、`name` が `ゲーム` の `ParentTag` を探し、なければ新しく作るために `find_or_create_by!` を使っています。
