---
id: note-insight-authorize-and-allowed-to-difference
title: `authorize!` と `allowed_to?` は認可の止め方が違う
created: 2026-04-11
source: [[2026-04-11_insight_action-policy-and-duration-review]]
---

## Summary
- `authorize!` は認可 NG のときに例外で止めるため、ハードブロック向きです。
- `allowed_to?` は真偽値で判定できるため、ソフトブロック向きです。
- 認可結果をどう扱いたいかで使い分けます。

## Tags
#rails #authorization #actionpolicy

## Links
- [[2026-04-11-action-policy-shares-controller]]
- [[note-insight-hard-block-and-soft-block]]
- [[note-insight-action-policy-responsibility-separation]]

## Body
`authorize!` と `allowed_to?` の大きな違いは、認可に失敗したときの扱いです。`authorize!` は失敗時に例外を発生させるので、その場で処理を止めたいケースに向いています。一方の `allowed_to?` は `true` / `false` を返すため、画面表示を続けながら操作制御やメッセージ表示を行いたいケースに向いています。

## Example
```ruby
authorize! share_link, to: :show?

if allowed_to?(:join?, share_link)
  # 参加ボタンを表示
end
```

このコードでは、`authorize!` は表示可否を強く制御し、`allowed_to?` は画面内の振る舞い制御に使っています。

## Action
- [ ] `authorize!` の内部でどのように例外が流れるかを調べる
