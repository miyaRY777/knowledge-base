---
id: note-insight-association-size-vs-count
title: 関連データ件数確認で size を使う要点
created: 2026-04-13
source: [[2026-04-13_insight_test-db-seeds-destroy-size-slug.md]]
review_streak: 1
last_reviewed_on: 2026-04-30
---

## Summary（3行）
- 関連データの件数確認では `count` より `size` の方が意図に合うことがある
- `count` は毎回 DB に問い合わせるが、`size` は読み込み済みならメモリ上の状態も使う
- `destroy` 後の確認では、DBへ毎回問い合わせる `count` より、関連が読み込み済みならその状態を使える `size` の方が自然なことがある

## Tags
#rails #activerecord #association #test #要復習 #要復習 #要復習

## Links
- [[note-insight-active-record-relation]]
- [[note-insight-destroy-vs-destroy-bang]]

## Body
関連データの件数確認では、`count` より `size` の方が意図に合うことがあります。`count` は毎回 DB に問い合わせますが、`size` はすでに読み込まれている関連であればメモリ上の状態を使います。`destroy` 後のテストでは、DB 上の件数を確認したいなら `count` でも問題ありません。一方で、関連が読み込み済みの場合はその状態を使えるため、関連オブジェクトとしての状態や不要な SQL を避ける意図があるときは `size` の方が自然なことがあります。

## Example
```ruby
user.posts.destroy_all
user.posts.size
```

このコードでは、削除後の関連データ件数を、関連の保持している状態も含めて確認するために `size` を使っています。

<!-- review_log: 2026-04-13,2026-04-25,2026-05-02 -->
