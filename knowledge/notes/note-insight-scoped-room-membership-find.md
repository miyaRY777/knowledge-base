---
id: note-insight-scoped-room-membership-find
title: "current_userの関連をたどって検索することで自分のデータだけを安全に取得できる"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **ログインユーザーに紐づくデータだけを安全に取得する方法**
- 関連をたどって検索することで、自分のデータ以外にアクセスできないようにします。
- セキュリティ対策として重要です。

## Tags
#insight

## Links

## Body
`current_user.room_memberships.find(params[:id])` のように関連をたどって検索すると、Rails が自動的に `WHERE user_id = ?` の条件を付けます。
他人のIDをパラメータに渡しても、その `room_membership` が自分のものでなければ `RecordNotFound` になるため、IDOR を防げます。
「自分のデータだけを取得する」という意図がコードに直接現れるので、可読性とセキュリティの両方が上がります。


## Example
```ruby
current_user.posts.find(params[:id])
```

このコードでは、自分の投稿だけを取得して他人のデータを防ぐために関連経由の find を使っています。
