---
id: note-insight-active-record-scope
title: "Active Recordのscopeは検索条件に名前を付けて再利用する仕組み"
created: 2026-05-04
source: [[2026-05-04_insight_rails-model-basics]]
---

## Summary
- `scope` は、よく使う検索条件や並び替えに名前を付けて Model に定義する仕組みです。
- 同じ `where` や `order` を何度も書かずに、意図が分かる名前で呼び出せます。
- Active Record のクエリメソッドと組み合わせて、読みやすい検索処理を作れます。

## Tags
#rails #activerecord #model #query

## Links
- [[note-insight-active-record-relation]]
- [[note-insight-sql-where]]

## Body
Active Record の `scope` は、アプリ内で繰り返し使う検索条件に名前を付けるための仕組みです。たとえば「公開中だけ取得する」「新しい順に並べる」のような条件を Model にまとめておくと、呼び出し側では `Project.active` のように意図が分かる形で書けます。

検索条件をその場ごとに直接書くよりも、条件の意味を名前として残せるので、一覧画面や絞り込み処理の見通しがよくなります。Active Record のクエリはメソッドチェーンで組み合わせられるため、scope も他の `where` や `order` とつなげて扱えます。

## Example
```ruby
class Project < ApplicationRecord
  scope :active, -> { where(status: "active") }
end

Project.active
```

このコードでは、`status` が `"active"` のプロジェクトだけを取得する条件に `active` という名前を付けています。

## Action
- [ ] class method で定義する場合との使い分けも整理する
