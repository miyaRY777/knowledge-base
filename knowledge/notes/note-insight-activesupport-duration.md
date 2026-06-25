---
id: note-insight-activesupport-duration
title: "`ActiveSupport::Duration` は時間量を表すオブジェクト"
created: 2026-04-11
source: [[2026-04-11_insight_action-policy-and-duration-review]]
quiz_fail_log: []
---

## Summary
- `1.day` のような値は数値ではなく `ActiveSupport::Duration` オブジェクトです。
- Duration は時間の長さを表すために使います。
- そのまま時刻ではなく、時刻計算の材料になる値です。

## Tags
#rails #activesupport #time

## Links
- [[note-insight-from-now-and-ago]]
- [[2026-04-11-action-policy-shares-controller]]

## Body
`ActiveSupport::Duration` は、「1日」「3時間」のような時間量を表すためのオブジェクトです。見た目は数値のように使えますが、実際には時刻そのものではありません。現在時刻や別の時刻に足したり引いたりして、未来や過去の時刻を求めるための部品として使われます。

## Example
```ruby
duration = 1.day

puts duration.class
```

このコードでは、`1.day` が単なる数値ではなく Duration オブジェクトであることを確認できます。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] Duration の内部構造を後で調べる
