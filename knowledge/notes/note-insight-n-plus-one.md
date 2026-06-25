---
id: note-insight-n-plus-one
title: "N+1は関連データ取得でSQLが増えすぎる問題"
created: 2026-04-28
source: [[2026-04-28_insight_n-plus-one-oop-database.md]]
review_streak: 1
last_reviewed_on: 2026-04-30
quiz_fail_log: []
---

## Summary
- N+1 は一覧取得後に関連データを1件ずつ追加取得してしまう問題。
- 件数が増えるほど SQL の回数も増え、画面表示が遅くなりやすい。
- Rails では `includes`、`preload`、`eager_load` などで関連を先読みして対策する。

## Tags
#rails #activerecord #database #query #n-plus-one

## Links
- [[note-insight-activerecord-includes]]
- [[note-insight-activerecord-preload]]
- [[note-insight-activerecord-eager-load]]

## Body
N+1 は、親データの一覧を取得したあと、ループの中で関連データを参照するたびに追加 SQL が発生してしまう状態です。最初の1回に加えて、一覧の件数ぶん関連取得が走るため、データが増えるほど処理が重くなります。

Rails では、関連データを先にまとめて読み込むことで N+1 を減らせます。代表的な方法として `includes`、`preload`、`eager_load` があり、SQL の組み立て方や JOIN の有無が異なります。

## Example
```ruby
books = Book.includes(:author).limit(10)

books.each do |book|
  puts book.author.name
end
```

このコードでは、各書籍の著者をループ内で1件ずつ取りに行かないように、`author` を先に読み込んで N+1 を防いでいます。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] `includes`、`preload`、`eager_load` の使い分けを復習する

<!-- review_log: 2026-05-02 -->
