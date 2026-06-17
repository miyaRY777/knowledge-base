---
id: note-insight-subject-request-bang
title: "subject(:request!)はRSpecでテスト対象の処理に名前をつける書き方"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **テストで呼び出す処理に名前をつける仕組み**
- RSpecで、繰り返し使う処理を `subject` にまとめて、`request!` という名前で呼び出せるようにします。
- テストコードをスッキリさせるために使います。

## Tags
#testing

## Links

## Body
RSpec の `subject` は「このテストで操作する主体」を定義するもので、名前付きにすることで複数の `it` ブロックから `request!` のように呼び出せます。
`!` はメソッド名の一部（任意の名前）で、「呼び出すと副作用が起きる」という慣習的な意味合いで使われます。
`expect { request! }.to change(Model, :count)` のように副作用を検証するマッチャと相性がよく、テストの意図を「何を実行すると何が変わるか」という形で読みやすく書けます。


## Example
```ruby
subject(:request!) { delete room_membership_path(membership) }

it "削除される" do
  expect { request! }.to change(RoomMembership, :count).by(-1)
end
```

このコードでは、削除リクエスト処理を request! としてまとめて再利用するために subject を使っています。
