---
id: note-insight-memory-overuse-risk
title: "メモリを使いすぎるとGC多発・スワップ・OOMにつながる"
created: 2026-06-24
source: [[2026-06-24_insight_ruby-memory-and-gc-basics.md]]
quiz_fail_log: []
---

## Summary
- メモリを使いすぎると、処理が重くなる・スワップが発生する・OOMでプロセスが落ちるリスクがあります。
- Railsで大量データを一度に読み込むとメモリを圧迫しやすくなります。
- 一度に読み込む量を減らすことで対策できます。

## Tags
#ruby #rails #memory #performance

## Links
- [[note-insight-memory-as-workspace]]
- [[note-insight-gc]]
- [[note-insight-swap]]
- [[note-insight-oom]]

## Body
メモリを使いすぎると次の問題が連鎖します。

1. GCが頻繁に動いて処理が遅くなる
2. 物理メモリが足りなくなるとスワップが発生し、さらに遅くなる
3. それでも足りなければOOMでプロセスが強制終了される

Railsでは `User.all` のような全件取得で大量のオブジェクトがヒープに乗り、メモリを圧迫しやすいです。`find_each` などで分割して処理するのが基本的な対策です。

## Example
```ruby
# NG: 100万件が一度にメモリに乗る
User.all.each { |u| process(u) }

# OK: 1000件ずつ処理してメモリを抑える
User.find_each(batch_size: 1000) { |u| process(u) }
```


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
