---
id: note-insight-current-attributes
title: "CurrentAttributesでリクエスト単位の共有値を管理する"
created: 2026-03-31
source: [[2026-03-31_insight_rails-study.md]]
quiz_fail_log: []
---

## Summary
- リクエストごとにログインユーザーなどの値をグローバルに保持する仕組み
- コントローラ・モデルどこからでもアクセス可能
- 便利だが暗黙の依存が生まれやすいため使いすぎ注意

## Tags
#rails #activesupport #design-pattern

## Links
- [[note-insight-active-record-callbacks]]
- [[note-insight-dependent-restrict-with-error]]

## Body
CurrentAttributesはActiveSupportが提供するリクエストスコープのグローバル変数的な仕組み。`Current.user` のように書くだけでどこからでもログインユーザーにアクセスできる。リクエストが終わると自動でリセットされるためスレッドセーフ。ただしモデル内で `Current.user` を参照すると、モデルがリクエストコンテキストに暗黙に依存することになり、テストやバッチ処理で使いにくくなる。引数で渡す設計と使い分けが重要。


## Example
```ruby
class Current < ActiveSupport::CurrentAttributes
  attribute :user
end

# コントローラで設定
Current.user = current_user

# モデルやどこからでも参照可能
Current.user
```

このコードでは、`Current.user` に現在のユーザーを入れて、リクエスト中のどこからでも参照できるようにしています。
