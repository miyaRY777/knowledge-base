---
id: note-insight-subject-request-bang
title: subject(:request!)の要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **テストで呼び出す処理に名前をつける仕組み**
- RSpecで、繰り返し使う処理を `subject` にまとめて、`request!` という名前で呼び出せるようにします。
- テストコードをスッキリさせるために使います。

## Tags
#testing

## Links
- [[関連ノート]]

## Body
**テストで呼び出す処理に名前をつける仕組み**

**解説：**
RSpecで、繰り返し使う処理を `subject` にまとめて、`request!` という名前で呼び出せるようにします。
テストコードをスッキリさせるために使います。

```ruby
subject(:request!) { delete room_membership_path(membership) }

it "削除される" do
  expect { request! }.to change(RoomMembership, :count).by(-1)
end
```

このコードでは、削除リクエスト処理を request! としてまとめて再利用するために subject を使っています。
