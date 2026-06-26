---
id: note-insight-hard-block-and-soft-block
title: "ハードブロックとソフトブロックは止め方が違う"
created: 2026-04-11
source: [[2026-04-11_insight_action-policy-and-duration-review]]
quiz_fail_log: []
---

## Summary
- ハードブロックは処理そのものを止める認可の考え方です。
- ソフトブロックはページ表示などを続けつつ、見せ方や操作だけを制御する考え方です。
- 実装上は、ハードブロックはコントローラで扱われやすく、ソフトブロックはビューや画面分岐で扱われやすいです。
- どこまで止めるべきかで使い分けます。

## Tags
#rails #authorization #actionpolicy

## Links
- [[2026-04-11-action-policy-shares-controller]]
- [[note-insight-authorize-and-allowed-to-difference]]

## Body
ハードブロックとソフトブロックの違いは、認可違反のときにどこまで処理を止めるかにあります。ハードブロックは「見せてはいけない」「進ませてはいけない」ときに処理全体を止めます。実装ではコントローラで `authorize!` を使って止める形になりやすいです。ソフトブロックはページは表示しつつ、ボタンを出さない、案内を出すなど、見せ方で制御する考え方です。こちらはビューや画面内分岐で `allowed_to?` を使って表現されやすいです。認可の厳しさと UX のバランスを考えるときの軸になります。

## Example
```ruby
authorize! share_link, to: :show?

unless allowed_to?(:join?, share_link)
  flash.now[:alert] = "参加できません"
end
```

このコードでは、`show?` はハードブロック、`join?` はソフトブロックとして扱っています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
