---
id: note-insight-room-membership-find
title: "RoomMembership.findはIDだけで検索するため他人のデータも取得できる危険がある"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **IDだけでレコードを取得する方法（危険な場合あり）**
- 単純にIDで検索するため、他人のデータも取得できてしまう可能性があります。
- 認可チェックが必要です。

## Tags
#security

## Links

## Body
`RoomMembership.find(params[:id])` のようにIDだけで検索すると、URLのIDを書き換えるだけで他人のデータにアクセスできる IDOR 脆弱性につながります。
`find` はテーブル全体を対象にするため、認可チェックなしに使うのは危険です。
安全にするには、`current_user.room_memberships.find(params[:id])` のように関連をたどって検索範囲を限定する必要があります。


## Example
```ruby
RoomMembership.find(params[:id])
```

このコードでは、IDだけでデータを取得するために find を使っています。
