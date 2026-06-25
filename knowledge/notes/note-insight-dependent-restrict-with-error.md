---
id: note-insight-dependent-restrict-with-error
title: "dependent: :restrict_with_errorは子レコードが残っている親を削除するとエラーを返すオプション"
created: 2026-03-30
source: [[2026-03-30_insight_rails-study.md]]
quiz_fail_log: []
---

## Summary
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


## Example
```ruby
class User < ApplicationRecord
  has_many :posts, dependent: :restrict_with_error
end
```

このコードでは、子レコードが残っている間は親レコードを削除できないように `dependent: :restrict_with_error` を設定しています。

参考:
- https://guides.rubyonrails.org/association_basics.html
- https://api.rubyonrails.org/classes/ActiveRecord/Associations/ClassMethods.html

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
