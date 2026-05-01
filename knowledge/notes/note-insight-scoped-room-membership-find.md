---
id: note-insight-scoped-room-membership-find
title: current_user.profile.room_memberships.find(params[:id])の要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **ログインユーザーに紐づくデータだけを安全に取得する方法**
- 関連をたどって検索することで、自分のデータ以外にアクセスできないようにします。
- セキュリティ対策として重要です。

## Tags
#insight

## Links

## Body
**ログインユーザーに紐づくデータだけを安全に取得する方法**

**解説：**
関連をたどって検索することで、自分のデータ以外にアクセスできないようにします。
セキュリティ対策として重要です。


## Example
```ruby
current_user.posts.find(params[:id])
```

このコードでは、自分の投稿だけを取得して他人のデータを防ぐために関連経由の find を使っています。
