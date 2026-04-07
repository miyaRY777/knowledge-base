---
id: note-insight-idempotent
title: 冪等性（べきとう）の要点
created: 2026-03-30
source: [[2026-03-30_insight_rails-study.md]]
---

## Summary（3行）
- 同じ操作を1回やっても複数回やっても、最終的な結果が変わらない性質のこと
- HTTPではPUTやDELETEが冪等、POSTは冪等ではない
- API設計やデータ更新処理で「再実行しても壊れない」安心感を作る基本概念

## Tags
#cs-basics #http #api

## Links
- [[note-insight-unique-constraint-null]]
- [[note-insight-dependent-restrict-with-error]]

## Body
冪等性は「何度繰り返しても同じ状態になる」という性質。たとえば `user.update(admin: true)` を2回実行しても結果は同じだが、`Post.create(title: "Hello")` を2回実行すると2件できてしまう。前者は冪等、後者は非冪等。HTTPメソッドでは GET/PUT/DELETE が冪等、POST は非冪等として設計されている。リトライ処理やジョブのリラン時に「もう一度実行しても安全か？」を判断する基準になる。


## Example
```ruby
# 冪等な操作
user.update(admin: true)

# 非冪等な操作
Post.create(title: "Hello")
```

このコードでは、同じ更新を繰り返しても結果が変わらない操作と、実行回数で結果が変わる操作を対比しています。

参考:
- https://developer.mozilla.org/en-US/docs/Glossary/Idempotent
