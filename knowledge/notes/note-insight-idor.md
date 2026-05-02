---
id: note-insight-idor
title: "IDOR (Insecure Direct Object Reference)の要点"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **他人のデータに不正アクセスできてしまう脆弱性**
- IDを直接指定して他人のデータにアクセスできる状態のことです。
- 関連を使った取得や認可チェックで防ぎます。

## Tags
#security

## Links

## Body
**他人のデータに不正アクセスできてしまう脆弱性**

**解説：**
IDを直接指定して他人のデータにアクセスできる状態のことです。
関連を使った取得や認可チェックで防ぎます。


## Example
```ruby
Room.find(params[:id]) # 認可なし
```

このコードでは、他人のデータにもアクセスできる可能性があり、IDORの原因になる書き方です。
