`Null`とは？

👉 **データが入っていないことを表す特別な値**

**解説：**
`Null` は、「値がない」「不明」「まだ入力されていない」ことを表す特別な値です。
`0` や空文字 `""` とは別物なので、SQLで調べるときは `=` ではなく `IS NULL` を使います。
参考: [PostgreSQL Documentation - Comparison Functions and Operators](https://www.postgresql.org/docs/current/functions-comparison.html)

```sql
SELECT * FROM users WHERE nickname IS NULL;
```

このコードでは、`nickname` に値が入っていないユーザーを探すために `Null` を使っています。

---

- [ ] `キー`とは？

👉 **テーブルのデータを識別したり、テーブル同士をつなげたりするための目印**

**解説：**
`キー` は、データベースでレコードを見分けたり、別のテーブルと関連づけたりするために使います。
代表的なキーには、レコードを一意に識別する `主キー` と、別テーブルを参照する `外部キー` があります。

**具体例：**
- ユーザーを見分けるために `users.id` を使う
- 投稿が誰のものかを表すために `posts.user_id` を使う
- 注文がどの顧客のものかを表すために `orders.customer_id` を使う

この例では、データを識別したり関連づけたりするために `キー` が関係しています。

---

- [ ] `主キー（Primary Key）`とは？

👉 **テーブル内の1件のレコードを一意に識別するためのキー**

**解説：**
`主キー（Primary Key）` は、テーブルの中で各レコードを区別するためのカラムです。
主キーには重複する値を入れられず、`null` も入れられません。
Railsでは多くの場合、`id` カラムが主キーとして自動的に使われます。参考: [Rails Guides - Active Record Basics](https://guides.rubyonrails.org/active_record_basics.html)

```sql
CREATE TABLE users (
  id bigserial PRIMARY KEY,
  name varchar(255)
);
```

このコードでは、各ユーザーを一意に識別するために `主キー（Primary Key）` を使っています。

---

- [ ] `外部キー（Foreign Key）`とは？

👉 **別のテーブルの主キーを参照して、テーブル同士をつなげるためのキー**

**解説：**
`外部キー（Foreign Key）` は、あるテーブルのカラムから、別のテーブルの主キーを参照するために使います。
Railsでは、たとえば `posts.user_id` が `users.id` を参照することで、「この投稿はどのユーザーのものか」を表せます。
外部キー制約を使うと、存在しないユーザーIDを投稿に入れるような不整合を防ぎやすくなります。参考: [PostgreSQL Documentation - Foreign Keys](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-FK)

```ruby
class CreatePosts < ActiveRecord::Migration[7.1]
  def change
    create_table :posts do |t|
      t.references :user, null: false, foreign_key: true
      t.string :title

      t.timestamps
    end
  end
end
```

このコードでは、`posts.user_id` が `users.id` を参照できるようにするために `外部キー（Foreign Key）` を使っています。
