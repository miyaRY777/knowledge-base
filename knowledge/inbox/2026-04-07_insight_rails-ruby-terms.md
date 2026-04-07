- [ ]  `gitでブランチを切り替えてもDBは自動で切り替わらない`とは？

👉 **切り替わるのは主にコードで、手元のデータベース本体は自動では変わらないということ**

**解説：**
Git でブランチを切り替えると、ファイルとして管理されているコードや migration ファイルは切り替わります。
一方で、開発環境の DB はローカルにある実体なので、自動では元に戻ったり切り替わったりしません。
そのため、今のコードが期待するDB構造と、実際のDB構造がズレることがあります。Rails では migration でDBの構造を変更していく仕組みです。 

具体例：

```
# feature ブランチでは admin カラムを追加している
class AddAdminToUsers < ActiveRecord::Migration[7.0]
  def change
    add_column :users, :admin, :boolean, default: false, null: false
  end
end
```

このコードでは、`users` テーブルに `admin` カラムを追加するために migration を使っています。
この migration を実行していない状態で、そのカラムを使うコードに切り替えるとズレが起きます。 
- [ ] `db:migrate`は何をするコマンド？

👉 **DBの構造を変更するときに使う**

**解説：**
`bin/rails db:migrate` は、まだ実行していない migration をDBに反映するコマンドです。
テーブルを作る、カラムを追加する、カラム名を変える、などの「構造変更」に使います。
migration ファイルを pull したあとによく使います。 

具体例：

```
bin/rails db:migrate
```

このコードでは、migration に書かれたDB構造の変更を反映するために `db:migrate` を使っています。

---

-  `db:seed`は何をするコマンド？

👉 **初期データを入れるときに使う**

**解説：**
`bin/rails db:seed` は、`db/seeds.rb` に書いたデータをDBへ投入するコマンドです。
管理者ユーザー、都道府県、カテゴリ一覧など、最初に入れておきたいデータでよく使います。
何度も実行することがあるので、重複しにくい書き方にするのが大切です。 

具体例：

```
# db/seeds.rb
User.find_or_create_by!(email: "admin@example.com") do |user|
  user.password = "password"
  user.admin = true
end
```

このコードでは、初期ユーザーをDBに入れるために seed データを書いています。

---

-  `db:prepare`は何をするコマンド？

👉 **DBを使える状態にまとめて準備するときに使う**

**解説：**
`bin/rails db:prepare` は、必要に応じてDBを作成し、schema の読み込みまたは migration の実行を行って、DBを使える状態に整えるコマンドです。
Rails Guides では、`db:setup` に近いが idempotent で、必要な処理だけを行うコマンドとして説明されています。
clone 直後や、開発環境を整えたいときに使いやすいです。 

具体例：

```
bin/rails db:prepare
```

このコードでは、DBをまとめて使える状態に整えるために `db:prepare` を使っています。

---

-  `db:create`は何をするコマンド？

👉 **DBそのものを作成するときに使う**

**解説：**
`bin/rails db:create` は、`config/database.yml` の設定をもとに、データベース自体を作るコマンドです。
まだDBが存在していないときに使います。
テーブル作成やデータ投入までは行わないので、そのあとに `db:migrate` や `db:seed` が必要になることがあります。 

具体例：

```
bin/rails db:create
```

このコードでは、まず空のデータベースを作るために `db:create` を使っています。
- [ ] `turbo_confirm`とは？

👉 **Turboでリンクやボタンを押したときに確認ダイアログを出すための指定**

**解説：**
`turbo_confirm` は、Turbo を使ったリンクやフォーム送信の前に「本当に実行しますか？」と確認したいときに使います。
削除や再発行のように、間違って押すと困る操作でよく使います。
Turbo の data 属性として指定し、OK を押したときだけ処理が続きます。

```erb
<%= link_to "再発行",
            regenerate_share_link_mypage_room_path(room),
            data: { turbo_method: :patch, turbo_confirm: "招待リンクを再発行しますか？" } %>
```

このコードでは、招待リンクの再発行を実行する前に、確認ダイアログを表示するために `turbo_confirm` を使っています。

---

- [ ] `オーケストレーション`とは？

👉 **複数の処理や役割を、全体としてうまく連携させる考え方**

**解説：**
オーケストレーションは、1つの処理だけではなく、複数の処理を順番や役割に沿ってまとめて動かすことを指します。
Railsの特別な機能名ではありません。設計や処理の流れを説明するときによく使う言葉です。
たとえば「コントローラがモデルやサービスを呼び分けて全体を進める」ときに使われます。

```ruby
class SignupService
  def call(user_params)
    user = User.create!(user_params)
    Profile.create!(user: user)
    WelcomeMailer.welcome(user).deliver_later
    user
  end
end
```

このコードでは、ユーザー作成・プロフィール作成・メール送信という複数の処理を順番にまとめて進めるために オーケストレーション という考え方が使われています。

---

- [ ] `定数`とは？

👉 **あとから変えない前提で、名前をつけて持たせる値**

**解説：**
Ruby では、**先頭が大文字の名前**は定数として扱われます。
`EXPIRES_IN_MAP` も大文字で始まっているので、Rubyでは定数です。
ただし、Rubyの定数は「絶対に変更できない値」ではなく、**変更しない前提で使う名前**です。

具体例：

```
EXPIRES_IN_MAP = {
  "1h" => 1.hour,
  "24h" => 24.hours,
  "3d" => 3.days
}.freeze
```

このコードでは、有効期限の対応表を、あとから何度も書き換えない前提の値としてまとめるために 定数 を使っています。

あなたの例でいうと、ここが定数名です。

```
EXPIRES_IN_MAP
```

右側の

```
{
  "1h" => 1.hour,
  "24h" => 24.hours,
  "3d" => 3.days
}
```

が、その定数に入れている値です。

---

- [ ] `invariant`とは？

👉 **ずっと守られているべき条件やルール**

**解説：**
`invariant` は、プログラムの途中でも壊れてはいけない前提のことです。
Rails の特別な機能名ではありません。設計やレビューで「この条件は常に成り立つべき」と説明するときに使います。
たとえば「1つの部屋に共有リンクは1つだけ」のようなルールが invariant です。

```ruby
validates :room_id, uniqueness: true
```

このコードでは、1つの部屋に対して複数の共有リンクが作られないようにして、`room_id` の一意性という invariant を守るためにバリデーションを使っています。

---

- [ ] `SecureRandom.urlsafe_base64(16)`とは？

👉 **URLに使いやすい、安全なランダム文字列を作るメソッド**

**解説：**
`SecureRandom.urlsafe_base64(16)` は、推測されにくいランダムな文字列を作るときに使います。
トークンや招待URLなど、他人に当てられたくない値を作る場面でよく使います。
毎回違う値が生成されるので、固定の文字列とは違って安全性を高めやすいです。

```ruby
token = SecureRandom.urlsafe_base64(16)
# 例: "q8lY7kP2sD4xN9abCDeF1g"
```

このコードでは、招待リンク用の推測されにくいトークンを作るために `SecureRandom.urlsafe_base64(16)` を使っています。

---

- [ ] `inclusion`とは？

👉 **値が決められた候補の中に入っているかを確認するバリデーション**

**解説：**
`inclusion` は、ある値が指定した配列や範囲に含まれているかを検証するときに使います。
想定外の値が保存されるのを防ぎたいときに便利です。
フォームの選択肢や、許可する文字列が決まっている項目でよく使います。

```ruby
validates :expires_in, inclusion: { in: %w[1h 24h 3d 7d] }
```

このコードでは、`expires_in` に許可した値だけを保存できるようにするために `inclusion` を使っています。

---

- [ ] `allow_nil`とは？

👉 **値が nil のときは、バリデーションをスキップできる指定**

**解説：**
`allow_nil` は、値が `nil` ならそのバリデーションを実行しないようにするときに使います。
「未入力は許可するけれど、入力されたときだけ内容をチェックしたい」場合によく使います。
`nil` は許可されますが、空文字 `""` は別扱いになることがあるので注意が必要です。

```ruby
validates :expires_in, inclusion: { in: %w[1h 24h 3d 7d] }, allow_nil: true
```

このコードでは、`expires_in` が `nil` のときは通しつつ、値が入っているときだけ候補の中に含まれているか確認するために `allow_nil` を使っています。
