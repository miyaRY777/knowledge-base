{
- [ ] `preload`とは？

👉 **関連データを別クエリで先に読み込むためのメソッド**

**解説：**
`preload` は、関連データを **関連ごとに別のSQL** でまとめて取得し、N+1問題を減らすために使います。
Rails Guides では、`preload` は「指定した関連ごとに1クエリずつ読み込む」と説明されています。
注意点として、`preload` では **関連先に対する条件を直接指定することはできません**。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_querying.html "Active Record Query Interface — Ruby on Rails Guides"))

具体例：

```ruby
books = Book.preload(:author).limit(10)

books.each do |book|
  puts book.author.name
end
```

このコードでは、著者データを別クエリでまとめて先に読み込んで、N+1問題を防ぐために `preload` を使っています。

---

- [ ] `eager_load`とは？

👉 **関連データを LEFT OUTER JOIN で一度に読み込むためのメソッド**

**解説：**
`eager_load` は、関連データを `LEFT OUTER JOIN`** を使った1つのSQL** で取得します。
Rails API でも、`eager_load` は `LEFT OUTER JOIN` を使うと明記されています。
ただし、JOIN で読み込むと **同じ親データが重複した行として増えやすく、大きなデータでは重くなることがあります**。 ([Ruby on Rails API](https://api.rubyonrails.org/classes/ActiveRecord/QueryMethods.html "ActiveRecord::QueryMethods"))

具体例：

```ruby
books = Book.eager_load(:author).limit(10)
```

このコードでは、本と著者を `LEFT OUTER JOIN` でまとめて取得するために `eager_load` を使っています。

---

- [ ] `includes`とは？

👉 **状況に応じて関連データの読み込み方法を切り替えるメソッド**

**解説：**
`includes` は、関連データをできるだけ少ないクエリ数で読み込むためのメソッドです。
通常は別クエリで読み込みますが、関連先に `where` 条件を付けると、`LEFT OUTER JOIN` を使う形に変わることがあります。
Rails Guides では、関連先に条件を書く用途では `joins`** を使う方法が推奨** されています。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_querying.html "Active Record Query Interface — Ruby on Rails Guides"))

具体例：

```ruby
users = User.includes(:posts)
```

このコードでは、投稿データをあわせて読み込んで、あとで `user.posts` を使うときのN+1問題を防ぐために `includes` を使っています。

**注意点：**
関連先に条件を書くと、内部でJOINベースのSQLになることがあります。 ([Ruby on Rails API](https://api.rubyonrails.org/classes/ActiveRecord/QueryMethods.html "ActiveRecord::QueryMethods"))

```ruby
users = User.includes(:posts).where(posts: { published: true })
```

このコードでは、投稿に条件を付けたため、関連テーブルを参照できるように `includes` を使っています。

---

- [ ] `APIエンドポイント`とは？

👉 **APIにリクエストを送る先のURLや入口のこと**

**解説：**
APIエンドポイントは、クライアントがAPIへアクセスするときの **具体的なURLやURI** を指します。
たとえば `/users` や `/api/v1/posts/1` のような形です。
これはRails特有の名前ではなく、Web API全般で使われる一般的な用語です。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_querying.html "Active Record Query Interface — Ruby on Rails Guides"))

具体例：

```ruby
# config/routes.rb
namespace :api do
  namespace :v1 do
    resources :posts, only: [:index]
  end
end
```

このコードでは、`/api/v1/posts` という API の入口を作るためにルーティングを書いています。

**注意点：**
`APIエンドポイント` はRailsの特別な機能名ではありません。
どのURLをAPIとして使うかは、ルーティング設計で決まります。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_querying.html "Active Record Query Interface — Ruby on Rails Guides"))

---

- [ ] `LEFT OUTER JOIN`とは？

👉 **左側の表を必ず残しながら、右側の表を結び付けるSQLの結合方法のこと**

**解説：**
`LEFT OUTER JOIN` は、左側のテーブルの行を必ず結果に残し、右側に一致する行がなければ **右側の列を **`NULL`**にして返す** JOINです。
PostgreSQLの公式ドキュメントでも、左側の行は少なくとも1回出力され、右側に一致しないときは空値（`null`）が入ると説明されています。
Railsでは `eager_load` や、一部の `includes` の内部で使われることがあります。 ([PostgreSQL](https://www.postgresql.org/docs/current/tutorial-join.html "PostgreSQL: Documentation: 18: 2.6. Joins Between Tables"))

```sql
SELECT users.*, posts.*
FROM users
LEFT OUTER JOIN posts
  ON posts.user_id = users.id;
```

このコードでは、投稿がないユーザーも結果に残したまま、投稿情報を結び付けるために `LEFT OUTER JOIN`を使っています。

**注意点：**
右側に一致するデータがない場合でも、左側のデータは消えません。
そのため、「関連がなくても親データは取得したい」ときによく使われます。 ([PostgreSQL](https://www.postgresql.org/docs/current/tutorial-join.html "PostgreSQL: Documentation: 18: 2.6. Joins Between Tables"))

参考: Rails API ([Ruby on Rails API](https://api.rubyonrails.org/classes/ActiveRecord/QueryMethods.html "ActiveRecord::QueryMethods")) / Rails Guides ([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_querying.html "Active Record Query Interface — Ruby on Rails Guides")) / PostgreSQL Docs ([PostgreSQL](https://www.postgresql.org/docs/current/tutorial-join.html "PostgreSQL: Documentation: 18: 2.6. Joins Between Tables"))}
