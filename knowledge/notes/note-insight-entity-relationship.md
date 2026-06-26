---
id: note-insight-entity-relationship
title: リレーションはエンティティ同士の関係
created: 2026-05-18
source: [[2026-05-18_insight_er-diagram-basics]]
review_streak: 0
last_reviewed_on: 2026-05-22
quiz_fail_log: []
---

## Summary
- リレーションは、エンティティ同士がどのようにつながるかを表します。
- `User` が複数の `Post` を持つ、`Post` が1人の `User` に属する、といった関係です。
- Rails では `has_many` や `belongs_to` で表現することが多いです。

## Tags
#database #database-design #entity #relationship #rails

## Links
- [[note-insight-er-diagram]]
- [[note-insight-entity]]
- [[note-insight-foreign-key]]

## Body
リレーションは、エンティティ同士のつながりを表す設計上の概念です。どの対象がどの対象と結びつくかを整理することで、必要な外部キーや関連の持ち方を考えやすくなります。

たとえば `User` と `Post` の間に「1人のユーザーは複数の投稿を持つ」という関係があるなら、Rails では `has_many :posts` と `belongs_to :user` のように実装することが多いです。

## Example
```ruby
class User < ApplicationRecord
  has_many :posts
end

class Post < ApplicationRecord
  belongs_to :user
end
```


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
