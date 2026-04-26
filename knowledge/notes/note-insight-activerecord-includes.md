---
id: note-insight-activerecord-includes
title: `includes` は状況に応じて関連の読み込み方法を切り替える
created: 2026-04-26
source: [[2026-04-26_insight_active-record-loading-and-joins.md]]
---

## Summary
- `includes` は関連データを少ないクエリ数で読むためのメソッド。
- 通常は別クエリ寄りで動くが、条件によって JOIN ベースになることがある。
- 関連先に条件を書くときは SQL の変化を意識する必要がある。

## Tags
#rails #activerecord #query #n-plus-one

## Links
- [[note-insight-activerecord-preload]]
- [[note-insight-activerecord-eager-load]]

## Body
`includes` は、関連データを効率よく読み込んで N+1 問題を減らすための Active Record のメソッドです。基本的には関連先をまとめて読み込む方向で動きますが、関連先テーブルに対する条件を加えたときは、内部で `LEFT OUTER JOIN` を使う形へ変わることがあります。見た目は同じ `includes` でも SQL の組み立てが変わるので、関連先に条件を付けるときは挙動を意識するのが大切です。

## Example
```ruby
users = User.includes(:posts)
users = User.includes(:posts).where(posts: { published: true })
```

このコードでは、後者は関連先 `posts` に条件を付けたため、関連テーブルを参照できる形で SQL が組み立てられます。

## Action
- [ ] `joins` を使う場合との違いも整理する
