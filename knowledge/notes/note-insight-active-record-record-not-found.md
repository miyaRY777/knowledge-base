---
id: note-insight-active-record-record-not-found
title: "ActiveRecord::RecordNotFoundはfindでレコードが見つからないときに発生する例外"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
quiz_fail_log: []
---

## Summary
- **レコードが見つからなかったときに発生する例外**
- `find` でデータが存在しない場合に発生します。
- rescueしてリダイレクトなどに使います。

## Tags
#activerecord

## Links

## Body
ActiveRecord::RecordNotFoundは、`find` が指定IDのレコードを見つけられなかったときに発生する例外です。
`find_by` と違い、`find` はレコードが存在しない場合に nil を返さず必ず例外を発生させます。
この例外は `rescue` でキャッチしてリダイレクトする使い方が典型的で、`rescue_from` をコントローラに書くことでアクション横断的に対応することもできます。


## Example
```ruby
Room.find(999)
```

このコードでは、存在しないIDを指定したときに RecordNotFound が発生します。

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
