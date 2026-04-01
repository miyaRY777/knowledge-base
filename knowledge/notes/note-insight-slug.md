---
id: note-insight-slug
title: slugとは何か
created: 2026-03-30
source: [[2026-03-30_insight_rails-study.md]]
---

## Summary（3行）
- URLに使うための「人が読める識別子」で、数値IDの代わりに使う
- 記事タイトルなどから生成し、URLをわかりやすく・SEOにも有利にする
- Rails固有の機能ではなく、アプリケーション側で設計・実装する汎用的な概念

## Tags
#web #rails #url

## Links
- [[note-insight-unique-constraint-null]]
- [[note-insight-dependent-restrict-with-error]]

## Body
slugは `/posts/1` のようなID直打ちURLを `/posts/rails-basics` のように人間が読める形にするための文字列。SEO的にもURLに意味のある単語が入る方が有利とされる。Railsでは `friendly_id` gemを使って自動生成する方法が定番だが、gem無しでも `to_param` をオーバーライドして実装できる。slugカラムにはUNIQUE制約をつけるのが基本。

```ruby
post = Post.create!(title: "Hello World", slug: "hello-world")
Post.find_by(slug: "hello-world")
```
