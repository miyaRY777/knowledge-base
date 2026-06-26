---
id: note-insight-soft-delete-flag
title: "論理削除フラグは削除済み扱いを表す目印"
created: 2026-05-02
source: [[2026-05-02_insight_samesite-csrf-soft-delete.md]]
quiz_fail_log: []
---

## Summary
- 論理削除フラグは、レコードを物理削除せずに削除済みとして扱うための目印です。
- `deleted` や `is_deleted` のような真偽値カラムで表すことがあります。
- 一覧や検索で削除済みデータを除外し忘れると、消したはずのデータが見えてしまいます。

## Tags
#rails #database #soft-delete #activerecord

## Links
- [[note-insight-soft-delete]]
- [[note-insight-destroy-vs-destroy-bang]]
- [[note-insight-database-record]]

## Body
論理削除フラグは、データベース上のレコードを残したまま、「アプリ上では削除済み」と判断するための目印です。たとえば `deleted: true` のような真偽値カラムを持たせ、通常の一覧では `deleted: false` のデータだけを表示します。

この方法は単純で分かりやすい一方、検索条件に削除済み除外を入れ忘れると、ユーザーには消したように見えるデータが再び表示されることがあります。そのため、スコープや共通クエリで扱いを揃えることが重要です。

## Example
```ruby
class User < ApplicationRecord
  scope :active, -> { where(deleted: false) }
end
```

このコードでは、削除済みではないユーザーだけを取得するために論理削除フラグを使っています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
