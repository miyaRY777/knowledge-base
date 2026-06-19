---
id: note-insight-find-or-create-by-bang
title: "find_or_create_by!は条件に一致するレコードを探しなければ作成する失敗時は例外を出すメソッド"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
quiz_fail_log: []
---

## Summary
- **見つけるか、なければ作るメソッド（失敗時は例外）**
- `find_or_create_by!` は、条件に合うレコードを探して、なければ新しく作ります。新規作成時にバリデーションで失敗すると例外を出すのが `!` 付きの特徴です。seedやマスターデータ投入でよく使われます。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/v7.0.2/active_record_querying.html "Active Record Query Interface — Ruby on Rails Guides"))
- ParentTag.find_or_create_by!(name: "ゲーム")

## Tags
#rails #activerecord #database

## Links

## Body
`find_or_create_by!` は、条件に一致するレコードがあれば取得し、なければ新規作成するメソッドです。
`!` 付きのため、新規作成時にバリデーションが失敗すると `ActiveRecord::RecordInvalid` 例外が発生します（`!` なしは失敗しても例外を出さず `false` を返す）。
seed データや一意にしたいマスタデータの投入でよく使われますが、並行リクエストが重なると同じレコードを2回作成しようとするレースコンディションが起きる場合があるため、ユニーク制約との組み合わせが重要です。

## Example

```ruby
ParentTag.find_or_create_by!(name: "ゲーム")
```

このコードでは、`name` が `ゲーム` の `ParentTag` を探し、なければ新しく作るために `find_or_create_by!` を使っています。
