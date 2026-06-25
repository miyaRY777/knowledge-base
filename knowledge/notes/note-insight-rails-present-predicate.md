---
id: note-insight-rails-present-predicate
title: "Railsの`present?`は中身があるかを見る"
created: 2026-04-08
source: [[2026-04-08_insight-ruby-nil-empty-blank-present-presence.md]]
review_streak: 0
last_reviewed_on: 2026-05-26
quiz_fail_log: []
---

## Summary
- `present?` は `blank?` の反対を表す Rails のメソッドです。
- 空ではないなら処理したい、という条件を自然に書けます。
- `blank?` を否定するより読みやすくなることがあります。

## Tags
#rails #activesupport #predicate

## Links
- [[note-insight-rails-blank-predicate]]
- [[note-insight-rails-presence]]

## Body
`present?` は `blank?` の反対で、値が「使える中身を持っている」かどうかを返します。
`blank?` は `nil`・空文字・空白のみ・空配列・空ハッシュをすべてカバーするため、`!value.nil? && !value.empty?` と書くより `value.present?` の方が安全で読みやすいです。
ビューで「表示できる値があるときだけ表示する」、コントローラで「フィルタ条件が入力されたときだけ適用する」などの条件分岐によく使われます。

## Example
```ruby
name = "Ruby"

name.present?   # => true
"".present?     # => false
nil.present?    # => false
```

このコードでは、値が空ではなく、使える中身を持っているかどうかを確認するために `present?` を使っています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] `if value.present?` が読みやすい場面の例を増やす
