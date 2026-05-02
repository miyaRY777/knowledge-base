---
id: note-insight-from-now-and-ago
title: "`.from_now` と `.ago` は現在時刻から Time を作る"
created: 2026-04-11
source: [[2026-04-11_insight_action-policy-and-duration-review]]
---

## Summary
- `.from_now` は現在時刻に Duration を足して未来の Time を作ります。
- `.ago` は現在時刻から Duration を引いて過去の Time を作ります。
- どちらも `Time.current` を基準に時刻を返します。

## Tags
#rails #activesupport #time

## Links
- [[note-insight-activesupport-duration]]
- [[2026-04-11-action-policy-shares-controller]]

## Body
`.from_now` と `.ago` は、Duration を現在時刻に適用して具体的な時刻を作るためのメソッドです。`1.day` だけでは時間の長さにすぎませんが、`1.day.from_now` にすると「今から1日後」という Time になります。時間量と時刻を区別して理解すると、期限計算の意図が分かりやすくなります。

## Example
```ruby
expires_at = 3.days.from_now
started_at = 1.hour.ago

puts expires_at
puts started_at
```

このコードでは、Duration を使って未来と過去の Time を作っています。

## Action
- [ ] `.from_now` と `.since` の違いも確認する
- [ ] 期限切れ判定の実装例を追加する
