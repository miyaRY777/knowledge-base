---
id: note-insight-room-membership-find
title: RoomMembership.find(params[:id])の要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **IDだけでレコードを取得する方法（危険な場合あり）**
- 単純にIDで検索するため、他人のデータも取得できてしまう可能性があります。
- 認可チェックが必要です。

## Tags
#security

## Links
- [[関連ノート]]

## Body
**IDだけでレコードを取得する方法（危険な場合あり）**

**解説：**
単純にIDで検索するため、他人のデータも取得できてしまう可能性があります。
認可チェックが必要です。

```ruby
RoomMembership.find(params[:id])
```

このコードでは、IDだけでデータを取得するために find を使っています。
