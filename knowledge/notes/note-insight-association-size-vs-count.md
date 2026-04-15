---
id: note-insight-association-size-vs-count
title: 関連データ件数確認で size を使う要点
created: 2026-04-13
source: [[2026-04-13_insight_test-db-seeds-destroy-size-slug.md]]review_streak: 0review_streak: 1
---

## Summary（3行）
- 関連データの件数確認では `count` より `size` の方が意図に合うことがある
- `count` は毎回 DB に問い合わせるが、`size` は読み込み済みならメモリ上の状態も使う
- `destroy` 後の確認では、関連の読み込み状態とのズレを避けたいときに `size` が自然

## Tags
#rails #activerecord #association #test #要復習

## Links
- [[note-insight-active-record-relation]]
- [[note-insight-destroy-vs-destroy-bang]]

## Body
関連データの件数確認では、`count` より `size` の方が意図に合うことがあります。`count` は毎回 DB に問い合わせますが、`size` はすでに読み込まれている関連であればメモリ上の状態を使います。`destroy` 後のテストでは、関連の読み込み済み状態とのズレを減らしながら件数を確かめたい場面があるため、`size` の方が自然なことがあります。

## Example
```ruby
user.posts.destroy_all
user.posts.size
```

このコードでは、削除後の関連データ件数を、関連の保持している状態も含めて確認するために `size` を使っています。
