---
id: note-insight-swap
title: "スワップはメモリ不足時にディスクを一時的にメモリ代わりに使う仕組み"
created: 2026-06-24
source: [[2026-06-24_insight_ruby-memory-and-gc-basics.md]]
quiz_fail_log: []
---

## Summary
- スワップは、物理メモリが足りなくなったときにOSがディスクをメモリ代わりに使う仕組みです。
- ディスクはメモリより遅いため、スワップが増えると処理が大幅に遅くなります。
- Railsの大量データ処理でメモリを使いすぎると、スワップが問題になります。

## Tags
#memory #os #performance

## Links
- [[note-insight-memory-as-workspace]]
- [[note-insight-disk-storage]]
- [[note-insight-memory-overuse-risk]]
- [[note-insight-oom]]

## Body
スワップは、物理メモリ（RAM）が不足したときにOSがディスクの一部をメモリの代わりに使う仕組みです。アプリはメモリが増えたように動けますが、ディスクアクセスはメモリより大幅に遅いため、スワップが増えると処理速度が激しく低下します。

Railsのバッチ処理などで一度に大量のデータを読み込むと、物理メモリを使い切ってスワップが発生する場合があります。

## Example
```ruby
# 大量データを一括処理するとスワップが発生しやすい
User.all.each { |u| process(u) }

# find_eachで分割してスワップを防ぐ
User.find_each(batch_size: 1000) { |u| process(u) }
```

## Action
