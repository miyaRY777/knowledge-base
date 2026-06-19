---
id: note-insight-active-record-relation
title: "ActiveRecord::Relationはクエリ条件だけを持ち実際のデータ取得を遅延するオブジェクト"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
review_streak: 0
last_reviewed_on: 2026-05-27
quiz_fail_log: []
---

## Summary
- **クエリ結果を表すオブジェクト（まだ実行されていない状態）**
- `where` などはすぐにデータを取得せず、クエリの条件だけを持つオブジェクトを返します。
- 実際にデータが取得されるのは `each` や `to_a` のときです。

## Tags
#activerecord

## Links

## Body
`ActiveRecord::Relation` は、SQLクエリの条件だけを保持するオブジェクトで、この時点ではデータベースにアクセスしていません。
`where`・`order`・`limit` などを重ねてもすぐには実行されず、`each` や `to_a` など実際に値を取り出す操作が呼ばれたタイミングで初めてSQLが発行されます（遅延評価）。
この仕組みのおかげでスコープのチェーンや条件の組み合わせが柔軟にできますが、意図せずループ内でクエリが発行される N+1 にもつながるため注意が必要です。


## Example
```ruby
users = User.where(active: true)
```

このコードでは、まだ実行されていない検索条件を持つオブジェクトとして Relation を使っています。
