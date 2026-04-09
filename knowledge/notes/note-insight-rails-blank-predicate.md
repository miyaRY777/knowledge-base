---
id: note-insight-rails-blank-predicate
title: Railsの`blank?`は空っぽをまとめて判定できる
created: 2026-04-08
source: [[2026-04-08_insight-ruby-nil-empty-blank-present-presence.md]]
---

## Summary
- `blank?` は Rails の Active Support が追加するメソッドです。
- `nil`、空文字、空白だけの文字列、空配列、空ハッシュ、`false` などをまとめて空扱いできます。
- `nil` の可能性がある値でも使いやすく、Rails ではよく使われます。

## Tags
#rails #activesupport #predicate #要復習

## Links
- [[note-insight-rails-blank-is-safe]]
- [[note-insight-rails-present-predicate]]

## Body
`blank?` は「実質的に中身がない」と言えるかをまとめて判定できる Rails のメソッドです。`nil` と空文字を別々に扱う必要がないため、フォーム値や表示用データの存在確認を短く書きたいときに便利です。

## Example
```ruby
nil.blank?      # => true
"".blank?       # => true
"   ".blank?    # => true
[].blank?       # => true
false.blank?    # => true
0.blank?        # => false
```

このコードでは、実質的に中身がない値かどうかをまとめて確認するために `blank?` を使っています。

## Action
- [ ] `blank?` が `false` になる代表例も追加する


<!-- review_log: 2026-04-09 -->
