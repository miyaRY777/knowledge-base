---
id: note-insight-integer-data-type
title: "integerは整数を保存するためのデータ型"
created: 2026-05-04
source: [[2026-05-04_insight_rails-model-basics]]
review_streak: 0
last_reviewed_on: 2026-05-27
quiz_fail_log: []
---

## Summary
- `integer` は、小数ではない整数を保存するためのデータ型です。
- 年齢、順番、件数、ステータス番号のような数値項目で使います。
- Rails のマイグレーションでは、カラム追加時に整数型として指定できます。

## Tags
#rails #database #migration #data-type

## Links
- [[note-insight-database-column]]
- [[note-insight-bigint-data-type]]

## Body
`integer` は、データベースに整数を保存するための型です。小数を含まない数値を扱いたいときに使います。Rails のマイグレーションでは、年齢、表示順、件数、ステータス番号などのカラムを作るときに指定できます。

文字列として保存するよりも、数値として比較したり並び替えたりしやすくなります。たとえばタスクの表示順を `position` として持たせる場合、`integer` 型にしておくと順番の比較や更新が自然にできます。

## Example
```ruby
class AddPositionToTasks < ActiveRecord::Migration[7.1]
  def change
    add_column :tasks, :position, :integer
  end
end
```

このコードでは、タスクの表示順を整数で保存するために `position` カラムを追加しています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
