---
id: note-insight-uniqueness-validation
title: "uniquenessバリデーションは同じ値の重複を保存前に確認する"
created: 2026-05-04
source: [[2026-05-04_insight_rails-model-basics]]
review_streak: 0
last_reviewed_on: 2026-05-25
quiz_fail_log: []
---

## Summary
- `uniqueness` バリデーションは、同じ値がすでに存在しないかを保存前に確認します。
- メールアドレスやユーザー名のように重複させたくない項目で使います。
- Rails 側だけでは完全ではないため、重要な項目は DB のユニーク制約と併用します。

## Tags
#rails #validation #database #constraint

## Links
- [[note-insight-unique-constraint]]
- [[note-insight-database-constraint]]

## Body
`uniqueness` バリデーションは、保存しようとしている値が既存レコードと重複していないかを Rails 側で確認する仕組みです。メールアドレスやユーザー名のように、同じ値を複数登録したくない項目で使います。

ただし、Rails のバリデーションは保存前にアプリ側で確認するものなので、同時に複数のリクエストが来ると完全には守れない場合があります。重複すると困る重要な値は、DB 側のユニーク制約も併用すると安全です。

## Example
```ruby
class User < ApplicationRecord
  validates :email, uniqueness: true
end
```

このコードでは、同じメールアドレスを持つユーザーを重複登録しにくくしています。

## Action
- [ ] `add_index unique: true` との併用例を整理する
