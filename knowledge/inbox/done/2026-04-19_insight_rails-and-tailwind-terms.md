{
- [ ] `md:grid-cols-2 lg:grid-cols-4`とは？

👉 **画面サイズに応じて Grid の列数を切り替える Tailwind CSS のクラス指定**

**解説：**
`grid-cols-2` は 2 列、`grid-cols-4` は 4 列の Grid を作るクラスです。
`md:` と `lg:` はレスポンシブ指定で、中サイズ以上では 2 列、大サイズ以上では 4 列に切り替わります。 ([Tailwind CSS](https://tailwindcss.com/docs/grid-template-columns?utm_source=chatgpt.com "grid-template-columns - Flexbox & Grid"))

具体例：

```erb
<div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div>4</div>
</div>
```

このコードでは、画面幅に応じて Grid の列数を切り替えるために `md:grid-cols-2 lg:grid-cols-4` を使っています。

---

- [ ] `フォールバックURL`とは？

👉 **本来使いたい URL が使えないときに代わりに使う URL**

**解説：**
`フォールバックURL` は Rails の特別な機能名ではありません。
一般に「優先して使う URL がない・使えない場合に、代わりに返す URL」という意味で使われることがあります。
どの URL を本命にして、どれを代わりにするかは、アプリ側の実装で意味が決まります。Rails では通常の URL 生成に `url_for` やルーティングヘルパーを使います。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_querying.html?utm_source=chatgpt.com "Active Record Query Interface"))

具体例：

```ruby
def avatar_url(user)
  user.avatar_url.presence || "/images/default-avatar.png"
end
```

このコードでは、ユーザー画像のURLがないときに、代わりの画像URLを返すために フォールバックURL という考え方を使っています。

---

- [ ] `eager_load`とは？

👉 **関連データを LEFT OUTER JOIN でまとめて読み込むための Active Record のメソッド**

**解説：**
`eager_load` は、関連先も含めて 1 回の JOIN クエリで読み込みたいときに使います。
関連先の条件や並び替えを扱いたい場面で使われることがあります。
`includes` と似ていますが、SQL の組み立て方が違います。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_querying.html?utm_source=chatgpt.com "Active Record Query Interface"))

具体例：

```ruby
memberships = RoomMembership.eager_load(room: :share_link)

memberships.each do |membership|
  puts membership.room.share_link&.token
end
```

このコードでは、`room` と `share_link` をまとめて読み込んで追加クエリを減らすために `eager_load` を使っています。

---

- [ ] `ヘルパーテスト`とは？

👉 **Helper メソッドの戻り値や表示内容を確認するテスト**

**解説：**
ヘルパーテストは、ビューで使う Helper メソッドが正しく動くかを確かめるテストです。
Rails では `ActionView::TestCase` を使って、文字列や HTML の出力を確認できます。
ビュー全体ではなく、表示用の小さなロジックだけを切り出して確かめたいときに便利です。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/testing.html?utm_source=chatgpt.com "Testing Rails Applications"))

具体例：

```ruby
require "test_helper"

class UsersHelperTest < ActionView::TestCase
  test "full_name を返す" do
    user = User.new(first_name: "Taro", last_name: "Yamada")

    assert_equal "Yamada Taro", full_name(user)
  end
end
```

このコードでは、Helper メソッドが期待した値を返すか確認するために ヘルパーテスト を使っています。

---

- [ ] `&.`とは？

👉 **nil のときにエラーを出さずに nil を返す safe navigation operator**

**解説：**
`&.` は Ruby の safe navigation operator で、左側の値が `nil` ならメソッドを呼ばずに `nil` を返します。
`NoMethodError` を防ぎたいときに便利ですが、何でも `&.` でつなぐと、本来気づくべき `nil` を見逃すことがあるので注意が必要です。 ([Rubyドキュメント](https://docs.ruby-lang.org/ja/latest/doc/news%3D2f2_3_0.html?utm_source=chatgpt.com "NEWS for Ruby 2.3.0 (Ruby 4.0 リファレンスマニュアル)"))

具体例：

```ruby
token = current_user.profile&.share_link&.token
```

このコードでは、`profile` や `share_link` が `nil` の可能性があるときにエラーを防ぐために `&.` を使っています。}
