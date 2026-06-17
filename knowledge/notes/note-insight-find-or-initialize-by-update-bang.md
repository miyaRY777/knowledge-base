---
id: note-insight-find-or-initialize-by-update-bang
title: "find_or_initialize_byとupdate!を組み合わせると見つからない場合もメモリ上で作成してから保存できる"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **見つけるか、なければメモリ上で作ってから、保存まで明示的に行う書き方**
- `find_or_initialize_by` は、見つかればそのレコードを返し、なければ未保存の新しいオブジェクトを返します。
- そのあと `update!` を使うと、属性を代入して保存まで行い、失敗時は例外になります。

## Tags
#rails #activerecord #database

## Links

## Body
**見つけるか、なければメモリ上で作ってから、保存まで明示的に行う書き方**

**解説：**
`find_or_initialize_by` は、見つかればそのレコードを返し、なければ未保存の新しいオブジェクトを返します。

そのあと `update!` を使うと、属性を代入して保存まで行い、失敗時は例外になります。
新規作成か既存更新かを同じ流れで扱いたいときに便利です。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/v7.0.2/active_record_querying.html "Active Record Query Interface — Ruby on Rails Guides"))

## Example

```ruby
tag = ParentTag.find_or_initialize_by(name: "ゲーム")
tag.update!(description: "遊びに関する親タグ")
```

このコードでは、既存レコードがあれば更新し、なければ新しいオブジェクトを作って保存するために `find_or_initialize_by + update!` を使っています。
