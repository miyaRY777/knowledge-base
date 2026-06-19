---
id: note-insight-activerecord-preload
title: "`preload` は関連データを別クエリで先に読む"
created: 2026-04-26
source: [[2026-04-26_insight_active-record-loading-and-joins.md]]
quiz_fail_log: []
---

## Summary
- `preload` は関連データを関連ごとに別クエリで先に読む。
- N+1 問題を減らしたいときに使う。
- 関連先に直接条件を書いて絞り込む用途には向かない。

## Tags
#rails #activerecord #query #n-plus-one

## Links
- [[note-insight-activerecord-eager-load]]

## Body
`preload` は、関連データを親クエリとは別にまとめて読み込むための Active Record のメソッドです。関連ごとに別の SQL を発行して関連先を先に集めるので、ループ内で関連を参照したときの N+1 問題を減らせます。一方で、関連先テーブルに対する条件をそのままクエリへ書きたいときには向かず、その場合は別の読み込み方法や JOIN ベースの考え方が必要になります。

## Example
```ruby
books = Book.preload(:author).limit(10)

books.each do |book|
  puts book.author.name
end
```

このコードでは、著者を別クエリで先にまとめて読み込んで、`book.author` 参照時の N+1 を防いでいます。

## Action
- [ ] `preload` と `includes` の使い分けを比較ノートにまとめる
