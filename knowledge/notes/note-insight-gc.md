---
id: note-insight-gc
title: "GCは使われなくなったオブジェクトを自動回収する仕組み"
created: 2026-06-24
source: [[2026-06-24_insight_ruby-memory-and-gc-basics.md]]
quiz_fail_log: []
---

## Summary
- GC（ガベージコレクション）は、不要になったメモリ上のオブジェクトを自動で回収する仕組みです。
- RubyではGCがあるため、開発者が手動でメモリ解放を書く場面は少ないです。
- メモリを大量に使うとGCが頻繁に走り、処理が遅くなります。

## Tags
#ruby #memory #gc #performance

## Links
- [[note-insight-memory-heap]]
- [[note-insight-memory-overuse-risk]]

## Body
GC（ガベージコレクション）は、参照されなくなったオブジェクトをヒープから回収し、メモリを再利用可能にする仕組みです。RubyはGCを持つ言語なので、開発者が `free()` のような手動解放を書く必要はありません。

ただし、GCが動いている間はアプリの処理が一時的に止まることがあります。大量のオブジェクトを短時間で作ると、GCが頻繁に起動して全体のパフォーマンスが落ちます。

## Example
```ruby
# 大量のActiveRecordオブジェクトを作ると不要オブジェクトが増え、GCが頻繁に動く
User.all.each do |user|
  # userが次のループで不要になるたびにGC対象が増える
end
```


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
