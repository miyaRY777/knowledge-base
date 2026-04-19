---
id: note-insight-ruby-safe-navigation-operator
title: `&.` は nil なら呼び出さずに nil を返す
created: 2026-04-19
source: [[2026-04-19_insight_rails-and-tailwind-terms.md]]
---

## Summary
- `&.` は Ruby の safe navigation operator です。
- 左側が `nil` のときはメソッド呼び出しをせず、そのまま `nil` を返します。
- 便利ですが、多用すると本来気づくべき `nil` を見逃すことがあります。

## Tags
#ruby #nil #safe-navigation #error-handling

## Links
- [[note-insight-ruby-empty-predicate-nil-risk]]
- [[note-insight-rails-presence]]

## Body
`&.` は、値が `nil` かもしれない場面で `NoMethodError` を防ぐための演算子です。安全に呼べる反面、どこで `nil` になったのかが見えにくくなることもあるので、必要な箇所だけに絞って使うのが大切です。

## Example
```ruby
token = current_user.profile&.share_link&.token
```

このコードでは、`profile` や `share_link` が存在しない場合でも例外を出さずに `nil` を返します。

## Action
- [ ] `dig` や明示的な nil チェックとの使い分けも整理する
