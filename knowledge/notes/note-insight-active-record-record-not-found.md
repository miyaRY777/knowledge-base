---
id: note-insight-active-record-record-not-found
title: ActiveRecord::RecordNotFoundの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **レコードが見つからなかったときに発生する例外**
- `find` でデータが存在しない場合に発生します。
- rescueしてリダイレクトなどに使います。

## Tags
#activerecord

## Links

## Body
**レコードが見つからなかったときに発生する例外**

**解説：**
`find` でデータが存在しない場合に発生します。
rescueしてリダイレクトなどに使います。


## Example
```ruby
Room.find(999)
```

このコードでは、存在しないIDを指定したときに RecordNotFound が発生します。
