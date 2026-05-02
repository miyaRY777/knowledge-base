---
id: note-insight-active-record-relation
title: "ActiveRecord::Relationの要点"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **クエリ結果を表すオブジェクト（まだ実行されていない状態）**
- `where` などはすぐにデータを取得せず、クエリの条件だけを持つオブジェクトを返します。
- 実際にデータが取得されるのは `each` や `to_a` のときです。

## Tags
#activerecord

## Links

## Body
**クエリ結果を表すオブジェクト（まだ実行されていない状態）**

**解説：**
`where` などはすぐにデータを取得せず、クエリの条件だけを持つオブジェクトを返します。
実際にデータが取得されるのは `each` や `to_a` のときです。


## Example
```ruby
users = User.where(active: true)
```

このコードでは、まだ実行されていない検索条件を持つオブジェクトとして Relation を使っています。
