---
id: note-insight-where-not
title: "where.notの要点"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **条件に一致しないレコードを取得するメソッド**
- 指定した条件を除外して検索したいときに使います。
- SQLの NOT に相当します。

## Tags
#insight

## Links

## Body
**条件に一致しないレコードを取得するメソッド**

**解説：**
指定した条件を除外して検索したいときに使います。
SQLの NOT に相当します。


## Example
```ruby
User.where.not(role: "admin")
```

このコードでは、admin以外のユーザーを取得するために where.not を使っています。
