---
id: note-insight-ruby-check-nil-before-empty
title: "`empty?`の前に`nil?`を確認する書き方"
created: 2026-04-08
source: [[2026-04-08_insight-ruby-nil-empty-blank-present-presence.md]]
quiz_fail_log: []
---

## Summary
- `empty?` は `nil` に使えないため、先に `nil?` で確認する書き方があります。
- 素の Ruby では安全性を確保するための基本的な対応です。
- Rails では同じ目的なら `blank?` のほうが短く書けることがあります。

## Tags
#ruby #rails #defensive-programming

## Links
- [[note-insight-ruby-empty-predicate-nil-risk]]
- [[note-insight-rails-blank-predicate]]

## Body
値が `nil` かもしれないときに `empty?` を使いたいなら、先に `nil?` で `nil` ではないことを確認してから呼ぶ必要があります。この書き方は安全ですが、Rails では `blank?` を使うと同じ意図をより短く表現できます。

## Example
```ruby
value = nil

if !value.nil? && value.empty?
  puts "空文字です"
end
```

このコードでは、`nil` に `empty?` を呼んでエラーにならないように、先に `nil?` を確認しています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
