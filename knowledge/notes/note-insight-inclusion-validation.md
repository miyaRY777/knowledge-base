---
id: note-insight-inclusion-validation
title: "inclusionバリデーションの要点"
created: 2026-04-07
source: [[2026-04-07_insight_rails-ruby-terms.md]]
---

## Summary
- `inclusion` は値が許可した候補に含まれるかを確認するバリデーションです。
- 想定外の値が保存されるのを防ぐために使います。
- フォーム選択肢や許可値が決まっている項目でよく使います。

## Tags
#rails #validation #model

## Links
- [[note-insight-allow-nil]]

## Body
`inclusion` は、ある値が指定した配列や範囲に含まれているかを検証するときに使うバリデーションです。保存できる値を限定したいときに役立ちます。

たとえば、期限の候補が `1h`、`24h`、`3d` のように決まっている場合に、想定外の値を保存しないように制御できます。

## Example
```ruby
validates :expires_in, inclusion: { in: %w[1h 24h 3d 7d] }
```

このコードでは、`expires_in` に許可した候補だけを保存できるようにしています。

## Action
- [ ] enum や定数との組み合わせ方も整理する
