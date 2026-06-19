---
id: note-insight-where-not
title: "where.notは指定した条件に一致しないレコードを取得するActiveRecordメソッド"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
review_streak: 0
last_reviewed_on: 2026-05-27
quiz_fail_log: []
---

## Summary
- **条件に一致しないレコードを取得するメソッド**
- 指定した条件を除外して検索したいときに使います。
- SQLの NOT に相当します。

## Tags
#insight

## Links

## Body
`where.not` は SQL の `NOT` 条件をActiveRecordで書く方法です。
ハッシュで条件を指定すると `WHERE column != value` に変換され、配列を渡せば `NOT IN` になります。
他の `where` と組み合わせてチェーンできるため、「退会済みを除く」「特定ロールを除外する」など除外条件をスコープとして再利用しやすいです。


## Example
```ruby
User.where.not(role: "admin")
```

このコードでは、admin以外のユーザーを取得するために where.not を使っています。
