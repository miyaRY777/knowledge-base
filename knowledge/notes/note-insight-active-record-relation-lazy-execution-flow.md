---
id: note-insight-active-record-relation-lazy-execution-flow
title: ActiveRecord::RelationはSQL実行前の検索条件を表す
created: 2026-05-27
source: [[復習中の補足]]
quiz_fail_log: []
---

## Summary
- `where.not` は、指定した条件に一致しないレコードを探すための否定条件を追加します。
- `where` 系メソッドは、すぐにDBへ問い合わせるというより、SQLの条件を組み立てます。
- `ActiveRecord::Relation` は、SQL実行前の検索条件を保持するオブジェクトです。
- `each`、`to_a`、`first` などで結果が必要になったタイミングでSQLが実行されます。

## Tags
#rails #activerecord #query #relation #lazy-execution

## Links
- [[note-insight-where-not]]
- [[note-insight-active-record-relation]]
- [[note-insight-database-query]]
- [[note-insight-sql]]

## Body
`where.not` と `ActiveRecord::Relation` は、Rails がSQLをどう組み立てるかを理解すると分かりやすくなります。

たとえば次のコードを書いたとします。

```ruby
users = User.where.not(role: "admin")
```

この時点で Rails は、まだデータベースへ問い合わせていません。`User` モデルを起点にして、`users` テーブルに対して「`role` が `admin` ではない」という検索条件を組み立てます。

SQLにすると、次のような条件に近い形です。

```sql
SELECT *
FROM users
WHERE role != 'admin';
```

ただし、このSQLは代入した瞬間に実行されるわけではありません。`User.where.not(role: "admin")` の戻り値は、検索条件を保持した `ActiveRecord::Relation` です。これは「SQLになる前の検索条件の設計図」のようなものです。

そのため、次のようにさらに条件をつなげられます。

```ruby
users = User
  .where.not(role: "admin")
  .where(active: true)
  .order(created_at: :desc)
```

内部的には、次のように条件を積み重ねているイメージです。

```text
ActiveRecord::Relation
├─ role != "admin"
├─ active = true
└─ ORDER BY created_at DESC
```

実際にSQLが実行されるのは、結果の中身が必要になったタイミングです。

```ruby
users.each do |user|
  puts user.name
end
```

このように `each` でレコードを使おうとしたとき、Rails は組み立てていた条件をSQLへ変換し、DBからデータを取得します。`to_a` や `first` などでも同じように、必要になったタイミングでSQLが実行されます。

この仕組みは Lazy Load、または遅延実行として理解できます。`where` のたびに毎回DBへ問い合わせるのではなく、条件を最後まで組み立ててからまとめてSQLを実行するため、効率よくクエリを作れます。

## Flow
```text
User
↓
usersテーブルを検索する起点になる
↓
where.not(role: "admin")
↓
adminではないという否定条件を追加する
↓
ActiveRecord::Relation
↓
まだSQLは実行されていない
↓
where / order / limit などをさらに追加できる
↓
each / to_a / first などで結果が必要になる
↓
SQLを実行する
↓
DBからデータを取得する
```

## Example
```ruby
users = User.where.not(role: "admin")
# この時点ではSQLはまだ実行されない

users = users.where(active: true)
# さらに条件を追加できる

users.each do |user|
  puts user.name
end
# ここでSQLが実行される
```

実行されるSQLのイメージ:

```sql
SELECT *
FROM users
WHERE role != 'admin'
  AND active = true;
```

## Key Point
Rails の `where` 系メソッドは、「すぐにデータを取得するメソッド」というより、「SQLを組み立てるメソッド」として見ると分かりやすいです。

この考え方を押さえると、`where`、`where.not`、`joins`、`includes`、`order`、`limit`、`select` などのクエリメソッドをつなげて理解しやすくなります。

## References
- [Rails Guides Active Record Query Interface](https://guides.rubyonrails.org/active_record_querying.html)
