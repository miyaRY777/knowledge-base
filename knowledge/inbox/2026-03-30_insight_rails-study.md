# 3月30日 学習メモ

**日時**: 2026-03-30
**情報源**: Raycast学習メモ

---

- [ ] `dependent: :restrict_with_error`とは？

👉 

**関連レコードがあるなら**
1. **親レコードの削除を止めて**
2. **親レコードのerrorsにエラーを追加する 動きをする**

**解説：**
`has_many` などの関連で使うオプションです。関連先のデータが残っている場合、親レコードの削除を止め、親オブジェクトの `errors` にエラーを追加します。

例外を発生させて止めるのではなく、バリデーションに近い形で安全に削除を防ぎたいときに使います。

具体例：

```ruby
class User < ApplicationRecord
  has_many :posts, dependent: :restrict_with_error
end

user = User.find(1)
user.destroy
user.errors.full_messages
```

このコードでは、`posts` が存在する `user` を削除できないようにするために `dependent: :restrict_with_error` を使っています。

参考:
- Rails Guides: https://guides.rubyonrails.org/association_basics.html
- Rails API: https://api.rubyonrails.org/classes/ActiveRecord/Associations/ClassMethods.html

---

- [ ] `冪等（べきとう）`とは？

👉 **同じ操作を何回しても、結果が変わらない性質のこと**

**解説：**
冪等（べきとう・べき等）は、同じ操作を1回行っても複数回行っても、最終的な状態が同じになる性質です。

HTTP では `PUT` や `DELETE` が代表例として説明されることが多いです。初心者向けには「同じ命令をもう一度送っても、結果が増えたり壊れたりしにくい性質」と考えると分かりやすいです。

具体例：

```ruby
# １回目
user.update(admin: true)

# ２回目
user.update(admin: true)
```

このコードでは、同じ更新を2回行っても `admin` が `true` のままなので、冪等な操作の例として使っています。

参考:
- MDN: https://developer.mozilla.org/en-US/docs/Glossary/Idempotent

---

- [ ] `UNIQUE制約でNULLが重複扱いされない理由`とは？

👉 

NULLは、「値がない」のではなく「値が不明」という扱い

「値が不明」だと、比較結果も不明になるから
NULL同士で比較しても、「等しい」と判定できない、

そのため、UNIQUE制約は「同じ値」を禁止するけど
NULLはそもそも比較ができないため、NULLは重複扱いはされない

**解説：**
PostgreSQLでは、NULLは「値がない」ではなく「値が不明」という扱いです。そのため、NULL同士は「等しい」と比較できず、UNIQUE制約でも重複とは判定されません。
つまり、UNIQUE制約は「同じ値」を禁止しますが、NULLはそもそも比較できないため対象外になります。

具体例：

```sql
CREATE TABLE users (
  email TEXT UNIQUE
);

INSERT INTO users (email) VALUES (NULL);
INSERT INTO users (email) VALUES (NULL); -- エラーにならない
```

このコードでは、email に UNIQUE 制約があっても、NULL は同じ値として扱われないため、複数登録できる仕組みを理解するために使っています。

---

- [ ] `slug`とは？

👉 

slug は、URLに使うための「人が読める識別子（文字列）」のことです。
IDの代わりにスラッグを使うことで、URLがわかりやすくなります
（例：`/posts/1` → `/posts/rails-basics`）。

**解説：**
`slug` は、URL の一部として使う、人が読みやすい文字列を指すことが多いです。
たとえば記事タイトルから `hello-world` のような形で作られます。Railsの特別な機能名ではなく、アプリ側でどう作るか・どう使うかを決める名前です。

具体例：

```ruby
post = Post.create!(title: "Hello World", slug: "hello-world")

Post.find_by(slug: "hello-world")
```

このコードでは、ID ではなく `slug` を使って記事を見つけられるようにするために `slug` を使っています。
