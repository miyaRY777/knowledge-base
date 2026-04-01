---
id: note-insight-dependent-restrict-with-error
title: "dependent: :restrict_with_error の仕組み"
created: 2026-03-30
source: [[2026-03-30_insight_rails-study.md]]
---

## Summary（3行）
- has_manyの関連で、子レコードが残っている親の削除を安全にブロックするオプション
- 例外を投げるのではなく、親オブジェクトのerrorsにエラーメッセージを追加する方式
- バリデーションエラーと同じ感覚で扱えるため、UIでのハンドリングがしやすい

## Tags
#rails #activerecord #association

## Links
- [[note-insight-slug]]
- [[note-insight-idempotent]]

## Body
`dependent: :restrict_with_error` は、関連レコードが存在する状態で親を削除しようとした時に、削除を中止してerrorsにメッセージを追加する仕組み。似たオプションの `:restrict_with_exception` は例外を発生させるが、こちらはバリデーションエラーに近い挙動をするため、コントローラやビューでの処理が自然に書ける。「うっかり子レコードごと消してしまう」事故を防ぎつつ、ユーザーにわかりやすくフィードバックを返したい場面で使う。

```ruby
class User < ApplicationRecord
  has_many :posts, dependent: :restrict_with_error
end
```

参考:
- https://guides.rubyonrails.org/association_basics.html
- https://api.rubyonrails.org/classes/ActiveRecord/Associations/ClassMethods.html
