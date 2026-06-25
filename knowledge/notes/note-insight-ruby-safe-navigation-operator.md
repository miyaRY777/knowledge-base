---
id: note-insight-ruby-safe-navigation-operator
title: "`&.`とは？"
created: 2026-04-19
source: [[2026-04-19_insight_rails-and-tailwind-terms.md]]
quiz_fail_log: []
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
`&.` は、左側の値が `nil` かもしれない場面で安全にメソッドを呼び出すための Ruby の演算子です。左側が `nil` の場合はメソッドを呼ばず、そのまま `nil` を返すため、`NoMethodError` を避けられます。

ただし、多用すると本来気づくべき `nil` を見逃しやすくなるので、必要な箇所だけに絞って使うのが大切です。

## Example
```ruby
token = current_user.profile&.share_link&.token
```

このコードでは、`profile` や `share_link` が存在しない場合でも例外を出さずに `nil` を返します。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] `dig` や明示的な nil チェックとの使い分けも整理する
