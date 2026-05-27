---
id: note-insight-bigint-data-type
title: "bigintはintegerより大きな整数を保存できるデータ型"
created: 2026-05-04
source: [[2026-05-04_insight_rails-model-basics]]
review_streak: 0
last_reviewed_on: 2026-05-27
---

## Summary
- `bigint` は、`integer` より大きな整数を保存できるデータ型です。
- Rails では主キーの `id` や外部キーの `user_id` などでよく使われます。
- ID のように件数が増え続ける値では、大きな範囲を扱える型が向いています。

## Tags
#rails #database #migration #data-type #要復習

## Links
- [[note-insight-integer-data-type]]
- [[note-insight-foreign-key-constraint]]

## Body
`bigint` は、通常の `integer` より大きな整数を保存できるデータ型です。Rails では、主キーの `id` や外部キーの `user_id` のように、レコード数が増えるほど大きな値になりやすい項目でよく使われます。

外部キーとして `user_id` を持つ場合、その値は参照先テーブルの `id` と対応します。参照先の主キーが `bigint` なら、外部キー側も `bigint` にして型を合わせるのが自然です。

## Example
```ruby
class CreateProfiles < ActiveRecord::Migration[7.1]
  def change
    create_table :profiles do |t|
      t.bigint :user_id, null: false

      t.timestamps
    end
  end
end
```

このコードでは、`users` テーブルの `id` と対応させるために `user_id` を `bigint` として保存しています。

## Action
- [ ] `references` や `foreign_key` 指定との関係を整理する
