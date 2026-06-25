---
id: note-insight-database-index
title: "インデックスは検索を速くするための目印"
created: 2026-04-30
source: [[2026-04-30_insight_database-fundamentals.md]]
review_streak: 0
last_reviewed_on: 2026-05-01
quiz_fail_log: []
---

## Summary
- インデックスは、特定のカラムでデータを探しやすくする仕組み。
- よく検索するカラムに使うと、取得処理を速くできる。
- ただし、追加や更新のコストも増えるため、必要な場所に貼る。

## Tags
#database #sql #performance #rails

## Links
- [[note-insight-database-query]]
- [[note-insight-sql-where]]
- [[note-insight-n-plus-one]]

## Body
インデックスは、データベース内の行を速く探すための目印です。本の索引のように、条件に合うデータへたどり着きやすくします。

検索が多いカラムにインデックスを付けると効果がありますが、書き込み時にはインデックスの更新も必要になります。そのため、何でも付けるのではなく、検索条件や並び替えでよく使うカラムに絞るのが基本です。

## Example
```ruby
add_index :users, :email
```

<!-- review_log: 2026-05-02 -->

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
