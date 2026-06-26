---
id: note-insight-disk-storage
title: "ディスクはデータを長期保存するストレージ"
created: 2026-06-24
source: [[2026-06-24_insight_ruby-memory-and-gc-basics.md]]
quiz_fail_log: []
---

## Summary
- ディスクは、ファイルやデータベースのデータを長期保存する場所です。
- メモリより多くのデータを保存できますが、読み書き速度はメモリより遅いです。
- RailsはSQLでディスクのDBからデータを取り出し、メモリに載せて処理します。

## Tags
#computer #memory #storage

## Links
- [[note-insight-memory-as-workspace]]
- [[note-insight-swap]]
- [[note-insight-secondary-storage]]

## Body
ディスク（HDD・SSD）は、データを長期的に保存するストレージです。電源を切っても内容が消えない不揮発性の記憶装置です。

メモリより容量は大きいですが速度は遅く、処理中のデータはメモリで扱い、必要なときだけディスクから読み込むのが基本です。

## Example
```ruby
# SQLでディスク上のDBからデータを取り出し、メモリに載せる
users = User.where(active: true)
```


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
