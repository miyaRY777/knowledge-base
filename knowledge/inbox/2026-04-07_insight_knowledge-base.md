# knowledge-base

**日時**: 2026-04-07
**情報源**: Raycast学習メモ

---

# 3月31日
- [ ] `Active Record Callbacks`とは？

👉 
**モデルの処理の前後に、自動で特定の処理を実行する仕組みのこと**

例えば保存前にデータを整形したり、削除後にログの記録に使います。
使いすぎると処理の流れが見えづらくなるので注意が必要です。

**解説：**
Active Record Callbacks は、レコードの作成・更新・削除などのタイミングで、自動的に処理を挟むために使います。
バリデーション前や保存後など、特定のタイミングにフックして処理を書けます。
ただし処理が増えると見えにくくなるため、使いすぎには注意が必要です。

具体例：

```ruby
class User < ApplicationRecord
  before_create :set_default_name

  private

  def set_default_name
    self.name ||= "ゲスト"
  end
end
```

このコードでは、ユーザーが作成される前に name が空なら「ゲスト」を設定するために Active Record Callbacks を使っています。

---

- [ ] `CurrentAttributes`とは？

👉 **リクエストごとに共通で使いたい値を管理する仕組み**

**解説：**
CurrentAttributes は、ログイン中のユーザーなどをグローバルに扱うための仕組みです。
コントローラやモデルのどこからでも同じ値にアクセスできるようになります。
ただし状態を持つため、使いすぎると依存関係が分かりにくくなる点に注意が必要です。

```ruby
# app/models/current.rb
class Current < ActiveSupport::CurrentAttributes
  attribute :user
end

# controller
class ApplicationController < ActionController::Base
  before_action do
    Current.user = current_user
  end
end

# model
class Post < ApplicationRecord
  before_create do
    self.user = Current.user
  end
end
```

このコードでは、ログインユーザーをどこからでも使えるようにするために CurrentAttributes を使っています。

# 4月1日

- [ ] `Axios（アクシオス）`とは？

👉 **JavaScriptでサーバーにHTTPリクエストを簡単に送るためのライブラリ（道具）**

**解説：**
`Axios` は、JavaScriptからサーバーとやり取りするときに使うライブラリです。
たとえば、一覧データを取りに行ったり、フォームの内容を送信したりするときに使います。
外部ライブラリなので、使う前にインストールやCDN読み込みが必要です。

```js
axios.get("/users")
  .then(response => {
    console.log(response.data);
  });
```

このコードでは、`/users` からデータを取得するために `Axios` を使っています。

---

- [ ] `HTTPリクエスト`とは？

👉 **サーバーにデータを取りに行ったり、送ったりする通信のこと**

**解説：**
`HTTPリクエスト` は、ブラウザやアプリがサーバーに対して「データをください」「このデータを保存してください」とお願いする仕組みです。
WebアプリでAPIとやり取りするときの基本になります。
`GET` や `POST` など、目的ごとに種類があります。

```js
fetch("/posts/1");
```

このコードでは、サーバーにデータ取得を依頼するために `HTTPリクエスト` を使っています。

---

- [ ] `Promise`とは？

👉 **あとで結果が返ってくる処理を受け取るための仕組みのこと**

**解説：**
`Promise` は、すぐには終わらない処理の結果を、あとから受け取るための仕組みです。
HTTP通信のような非同期処理でよく使われます。
成功時は `.then()`、失敗時は `.catch()` で処理を書くことが多いです。

```js
axios.get("/users")
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```

このコードでは、通信結果をあとで受け取るために `Promise` を使っています。

---

- [ ] `Fetch API`とは？

👉 **ブラウザ標準で使えるHTTP通信の仕組みのこと**

**解説：**
`Fetch API` は、ブラウザに最初から用意されているHTTPリクエスト用の機能です。
追加インストールなしで使えますが、レスポンスをJSONとして使うには `response.json()` を呼ぶ必要があります。
`Axios` と比べると、少し記述が増えることがあります。

具体例：

```js
fetch("/users")
  .then(response => response.json())
  .then(data => {
    console.log(data);
  });
```

このコードでは、ブラウザ標準の仕組みでデータを取得するために `Fetch API` を使っています。

---

- [ ] `GETリクエスト`とは？

👉 **サーバーからデータを取得するときのリクエストのこと**

**解説：**
`GETリクエスト` は、データを読むときに使う基本的なHTTPメソッドです。
一覧表示や詳細表示のデータ取得でよく使います。
Axiosでは `axios.get()` のように書けます。

```js
axios.get("/posts/1")
  .then(response => {
    console.log(response.data);
  });
```

このコードでは、投稿データを取得するために `GETリクエスト` を使っています。

---

- [ ] `POSTリクエスト`とは？

👉 **サーバーに新しいデータを送るときのリクエストのこと**

**解説：**
`POSTリクエスト` は、新規作成したいデータをサーバーに送るときによく使います。
フォーム送信や新規登録の処理でよく登場します。
Axiosでは、送信したいデータを第2引数に渡せます。

具体例：

```js
axios.post("/posts", {
  title: "New Post",
  body: "Hello"
});
```

このコードでは、新しい投稿データを作成するために `POSTリクエスト` を使っています。

---

- [ ] `リクエストメソッドエイリアス`とは？

👉 **HTTPメソッドを短くわかりやすく書ける便利な書き方**

**解説：**
`axios.get()` や `axios.post()` のような書き方は、`Axios` が用意しているエイリアスです。
`axios.request({ method: ... })` よりも短く書けるので、コードが読みやすくなります。
よく使う `GET` `POST` `PUT` `DELETE` などが用意されています。

具体例：

```js
axios.get("/users");
axios.post("/users", { name: "Taro" });
```

このコードでは、HTTPメソッドを簡潔に書くために `リクエストメソッドエイリアス` を使っています。

---

- [ ] `Axiosインスタンス`とは？

👉 **共通設定をまとめたAxios専用の通信オブジェクトのこと**

**解説：**
`Axiosインスタンス` は、`axios.create()` で作るカスタム設定付きのAxiosです。
`baseURL` や `headers` などを最初にまとめて設定できるので、同じ設定を書く手間を減らせます。
API通信が増えると特に便利です。

具体例：

```js
const apiClient = axios.create({
  baseURL: "https://api.example.com",
  timeout: 5000
});

apiClient.get("/users");
```

このコードでは、共通設定を使い回して通信を簡潔にするために `Axiosインスタンス` を使っています。

---

- [ ] `baseURL`とは？

👉 毎回同じURLの前半部分を、省略して書けるようにする設定

**解説：**
`baseURL` は、毎回同じドメインやURLの先頭部分を書く手間を減らすための設定です。
インスタンスに設定しておくと、`/users` のような相対パスだけで通信できます。
絶対URLを指定した場合は、そちらが優先されます。

具体例：

```js
const apiClient = axios.create({
  baseURL: "https://api.example.com"
});

apiClient.get("/users");
```

このコードでは、共通のURLを毎回書かなくて済むように `baseURL` を使っています。

---

- [ ] `timeout`とは？

👉 **通信をどれくらい待つか決める設定のこと**

**解説：**
`timeout` は、リクエストが終わるまでの待ち時間をミリ秒で指定する設定です。
時間内に応答が返らないと、エラーとして扱われます。
通信が止まり続けるのを防ぎたいときに便利です。

具体例：

```js
const apiClient = axios.create({
  timeout: 5000
});
```

このコードでは、5秒以上応答がない通信を打ち切るために `timeout` を使っています。

---

- [ ] `headers`とは？

👉 **リクエストやレスポンスに付ける追加情報**

**解説：**
`headers` は、通信時に一緒に送るメタ情報です。
たとえば「JSONを送ります」「認証トークンがあります」といった情報をここに入れます。
APIによって必要なヘッダーは変わるので、仕様確認が大切です。

具体例：

```js
const apiClient = axios.create({
  headers: {
    Authorization: "Bearer sample-token"
  }
});
```

このコードでは、認証情報をリクエストに含めるために `headers` を使っています。

---

- [ ] `Content-Type`とは？

👉 **送るデータの種類をサーバーに伝えるヘッダー**

**解説：**
`Content-Type` は、送信するデータがどんな形式かを示すためのヘッダーです。
`application/json` を指定すると、「JSON形式で送ります」という意味になります。
APIにJSONを送るときによく使います。

具体例：

```js
axios.post("/posts", { title: "Hello" }, {
  headers: {
    "Content-Type": "application/json"
  }
});
```

このコードでは、送信データがJSON形式であることを伝えるために `Content-Type` を使っています。

---

- [ ] `JSONPlaceholder`とは？

👉 本物のAPIのようにHTTP通信を試せる練習用サービス（**モックAPIサービス**）

**解説：**
`JSONPlaceholder` は、本物のAPIのようにHTTP通信を試せる練習用サービスです。
`GET` や `POST` などを気軽に試せるので、学習やサンプルコードによく使われます。
実際の本番データではなく、練習用のダミーデータです。

具体例：

```js
axios.get("https://jsonplaceholder.typicode.com/posts/1")
  .then(response => {
    console.log(response.data);
  });
```

このコードでは、練習用APIに通信して動作確認するために `JSONPlaceholder` を使っています。

# 4月2日
- [ ] `for文`とは？

👉 **同じ処理をくり返すための構文のこと**

**解説：**
`for` 文は、初期化・条件判定・増減処理を1セットで書いて、条件が `false` になるまで処理をくり返すときに使います。回数が決まっているループを書くときによく使います。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for "for - JavaScript | MDN"))

具体例：

```js
for (let i = 1; i <= 3; i++) {
  console.log(i);
}
```

このコードでは、`i` を 1 から 3 まで増やしながら、同じ処理を3回くり返すために `for` 文を使っています。

---

- [ ] `増減式`とは？

👉 **ループごとに値を増やしたり減らしたりする部分**

**解説：**
`for (初期化; 条件; 増減式)` の3つ目に書く式です。1回ループが終わるたびに実行され、カウンタを `i++` や `i--` のように変化させます。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration "Loops and iteration - JavaScript | MDN"))

```js
for (let i = 0; i < 3; i++) {
  console.log(i);
}
```

このコードでは、次のループへ進むたびに `i` を 1 ずつ増やすために増減式の `i++` を使っています。

---

- [ ] `初期化`とは？

👉 **ループを始める前に最初の値を用意すること**

**解説：**
`for` 文の最初の部分に書く式です。多くの場合、`let i = 0` のようにループ用の変数を作って、開始位置を決めます。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for "for - JavaScript | MDN"))

具体例：

```js
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

このコードでは、ループを 0 から始めるために `let i = 0` で初期化しています。

---

- [ ] `無限ループ`とは？

👉 **終わる条件がなく、処理がずっと続いてしまう状態**

**解説：**
ループの条件がずっと `true` のままだと、処理が止まらなくなります。`for (;;)` や、条件や増減式の書き間違いで起こることがあります。止まる条件を必ず確認するのが大切です。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration "Loops and iteration - JavaScript | MDN"))

具体例：

```js
let i = 0;

while (true) {
  console.log(i);
  i++;
}
```

このコードでは、条件が常に `true` なので、処理が終わらない無限ループになります。

---

- [ ] `配列とループ処理`とは？

👉 **配列の中身を順番に取り出して処理すること**

**解説：**
配列は複数の値を順番に持てるので、ループと相性がいいです。`for` 文では `length` を使って、先頭から末尾まで1つずつ処理できます。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Loops?utm_source=chatgpt.com "Looping code - Learn web development | MDN"))

具体例：

```js
const fruits = ["apple", "banana", "orange"];

for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}
```

このコードでは、配列の要素を先頭から順番に取り出して表示するために、配列とループ処理を組み合わせています。

補足：
- length（配列）：**配列に入っている要素の数を取得するプロパティ**

---

- [ ] `boolean, default: false, null: false`とは？

👉 **真偽値カラムに「初期値」と「未設定禁止」を付ける指定**

**解説：**
`boolean` は `true / false` を入れる型です。`default: false` は何も指定しなかったときの初期値を `false` にし、`null: false` は `nil`を保存できないようにします。3値状態を避けて、判定をわかりやすくしたいときによく使います。`default` はDBの既存データへの反映がDB依存になることがある点に注意が必要です。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/active_record_migrations.html "Active Record Migrations — Ruby on Rails Guides"))

具体例：

```ruby
add_column :users, :admin, :boolean, default: false, null: false
```

このコードでは、`admin` を true / false で管理しつつ、未設定の `nil` を防ぐために `default: false, null: false` を使っています。

---

- [ ] `trait :admin`とは？

👉 **FactoryBotで「管理者ユーザー用の追加設定」をまとめる書き方**

**解説：**
`trait` は、FactoryBotで属性のまとまりを名前付きで再利用するための機能です。`trait :admin` は Rails の特別な機能名ではなく、FactoryBot の機能です。

テストで `create(:user, :admin)` のように使うと、管理者用の値を持つデータを作りやすくなります。 ([Thoughtbot](https://thoughtbot.github.io/factory_bot/traits/summary.html?utm_source=chatgpt.com "Traits - factory_bot"))

具体例：

```ruby
FactoryBot.define do
  factory :user do
    name { "Taro" }

    trait :admin do
      admin { true }
    end
  end
end
```

このコードでは、通常の `user` に管理者用の設定を追加できるようにするために `trait :admin` を使っています。

---

- [ ] `current_user.admin?`とは？

👉 **今ログインしているユーザーが管理者かどうかを確認する書き方**

**解説：**
`current_user` は、ログイン中のユーザーを表すことが多いです。そこに対して `admin?` を呼ぶと、管理者権限があるかどうかを判定できます。`current_user` という名前自体は Rails 本体の共通メソッドではなく、Devise などの認証機能でよく使われるものです。`admin?` の部分は boolean カラム由来の判定です。 ([Ruby on Rails API](https://api.rubyonrails.org/classes/ActiveRecord/AttributeMethods.html?utm_source=chatgpt.com "ActiveRecord::AttributeMethods - Rails API"))

具体例：

```ruby
if current_user.admin?
  redirect_to admin_root_path
end
```

このコードでは、今ログインしているユーザーが管理者なら管理画面へ進ませるために `current_user.admin?` を使っています。
- [ ] `クエリメソッド`とは？

👉 **「〜か？」を確認するためのメソッド**

**解説：**
Rubyでは、名前の最後に `?` が付くメソッドは、状態や条件をたずねるためのメソッドとして使うのが慣習です。
たとえば `empty?` や `nil?` は、「空ですか？」「nilですか？」を確認します。
Rubyの公式ドキュメントでも、`?` で終わるメソッドは慣習として真偽値を返すものと説明されています。 ([Ruby言語ドキュメント](https://docs.ruby-lang.org/en/3.0/syntax/methods_rdoc.html?utm_source=chatgpt.com "methods - RDoc Documentation"))

具体例：

```ruby
fruits = []

puts fruits.empty?
```

このコードでは、配列が空かどうかを確認するために `クエリメソッド` を使っています。

---

- [ ] `db:seed`とは？

👉 `db/seeds.rb`** の初期データをDBに入れるコマンド**

**解説：**
`db:seed` は `db/seeds.rb` を読み込んで、初期データや参照データを投入するときに使います。新しい環境を作ったときや、開発環境をそろえたいときによく使います。何度も実行する可能性があるので、重複しにくい書き方にすることが大切です。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/command_line.html "The Rails Command Line — Ruby on Rails Guides"))

具体例：

```bash
bin/rails db:seed
```

このコードでは、`db/seeds.rb` に書いた初期データをデータベースへ投入するために `db:seed` を使っています。

---

- [ ] `find_or_create_by!`とは？

👉 **見つけるか、なければ作るメソッド（失敗時は例外）**

**解説：**
`find_or_create_by!` は、条件に合うレコードを探して、なければ新しく作ります。新規作成時にバリデーションで失敗すると例外を出すのが `!` 付きの特徴です。seedやマスターデータ投入でよく使われます。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/v7.0.2/active_record_querying.html "Active Record Query Interface — Ruby on Rails Guides"))

具体例：

```ruby
ParentTag.find_or_create_by!(name: "ゲーム")
```

このコードでは、`name` が `ゲーム` の `ParentTag` を探し、なければ新しく作るために `find_or_create_by!` を使っています。

---

- [ ] `find_or_initialize_by + update!`とは？

👉 **見つけるか、なければメモリ上で作ってから、保存まで明示的に行う書き方**

**解説：**
`find_or_initialize_by` は、見つかればそのレコードを返し、なければ未保存の新しいオブジェクトを返します。

そのあと `update!` を使うと、属性を代入して保存まで行い、失敗時は例外になります。
新規作成か既存更新かを同じ流れで扱いたいときに便利です。 ([Ruby on Rails Guides](https://guides.rubyonrails.org/v7.0.2/active_record_querying.html "Active Record Query Interface — Ruby on Rails Guides"))

具体例：

```ruby
tag = ParentTag.find_or_initialize_by(name: "ゲーム")
tag.update!(description: "遊びに関する親タグ")
```

このコードでは、既存レコードがあれば更新し、なければ新しいオブジェクトを作って保存するために `find_or_initialize_by + update!` を使っています。

# 4月3日
- [ ] `bin/rails db:prepare`とは？

👉 **データベースを「使える状態」にまとめて整えるコマンドのこと**

**解説：**
`db:prepare` は、データベースが無ければ作成し、マイグレーションを実行し、必要に応じて seed も実行するコマンドです。
開発環境やテスト環境を一発で整えるために使います。
既にDBがある場合はマイグレーションのみ実行されます。

具体例：

```
bin/rails db:prepare
```

このコードでは、データベースを作成・更新して、アプリがすぐ使える状態にするために db:prepare を使っています。

# 4月4日

- [ ]  順番に回すときは `i = 0` から始めて `i++` する
- [ ] 逆順に回すときは `animals.length - 1` から始めて `i--` する
- [ ] toUpperCase()
      people[i].toUpperCase()
-  `i = 0 から始めて i++ する`

👉 配列やリストを最初から順番に処理するための基本的な書き方

**解説：**
配列は0番目から始まるため、`i = 0` からスタートします。
`i++` は1ずつ増やすという意味で、先頭から順番に処理したいときに使います。

```
const animals = ["dog", "cat", "bird"];

for (let i = 0; i < animals.length; i++) {
  console.log(animals[i]);
}
```

このコードでは、配列の先頭から順番に要素を取り出すために i = 0 から始めて i++ を使っています。

---

-  `animals.length - 1 から始めて i-- する`と

👉 配列を後ろから逆順に処理するための書き方

**解説：**
配列の最後のインデックスは `length - 1` なので、そこからスタートします。
`i--` は1ずつ減らすという意味で、後ろから順番に処理したいときに使います。

```
const animals = ["dog", "cat", "bird"];

for (let i = animals.length - 1; i >= 0; i--) {
  console.log(animals[i]);
}
```

このコードでは、配列の最後から逆順に要素を取り出すために length - 1 から始めて i-- を使っています。

---

-  `toUpperCase()`とは？

👉 文字列をすべて大文字に変換するメソッド

**解説：**
`toUpperCase()` はJavaScriptの文字列メソッドで、小文字を大文字に変換します。
配列の中の文字列にも使うことができます。

```
const people = ["Scooby", "Velma", "Daphne"];

for (let i = 0; i < people.length; i++) {
  console.log(people[i].toUpperCase());
}
```

このコードでは、配列の各要素を大文字に変換するために toUpperCase() を使っています。

# 4月5日
- [ ] `headers: { "Accept" => "text/vnd.turbo-stream.html" }`とは？

👉 **Turbo Stream形式でレスポンスを受け取るためのHTTPヘッダー**

**解説：**
リクエスト時に「Turbo Stream形式で返してほしい」とサーバーに伝えるために使います。
これにより、`format.turbo_stream` が選ばれて部分更新が行われます。

```ruby
post room_path(room), headers: { "Accept" => "text/vnd.turbo-stream.html" }
```

このコードでは、Turbo Streamとしてレスポンスを受け取り、画面の一部更新を行うために headers を使っています。

---

- [ ] `subject(:request!)`とは？

👉 **テストで呼び出す処理に名前をつける仕組み**

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

---

- [ ] `format.turbo_stream { flash.now[:notice] = "部屋から退出しました" }`とは？

👉 **Turbo通信時にその場でフラッシュメッセージを表示する処理**

**解説：**
`flash.now` はリダイレクトせず同じリクエスト内で表示するために使います。
Turbo Streamでは画面遷移しないため、`flash.now` が必要です。

```ruby
format.turbo_stream { flash.now[:notice] = "削除しました" }
```

このコードでは、画面遷移せずにメッセージを表示するために flash.now を使っています。

---

- [ ] `format.html { redirect_to mypage_rooms_path, notice: "部屋から退出しました" }`とは？

👉 **通常のHTMLリクエスト時にリダイレクトとメッセージ表示を行う処理**

**解説：**
HTMLリクエストではページ遷移が必要なので `redirect_to` を使います。
`notice:` はフラッシュメッセージとして次の画面に渡されます。

```ruby
format.html { redirect_to root_path, notice: "完了しました" }
```

このコードでは、処理後に別ページへ遷移しつつメッセージを表示するために redirect_to を使っています。

---

- [ ] `rescue`とは？

👉 **例外をキャッチする仕組み（書く場所と範囲が違う）**

**解説：**
`rescue` はメソッド内でエラーを捕まえるキーワードです。
`rescue_from`（よく「Rescue」と呼ばれる）はコントローラ全体でエラーを処理するために使います。

```ruby
def show
  @room = Room.find(params[:id])
rescue ActiveRecord::RecordNotFound
  redirect_to root_path
end
```

このコードでは、レコードが見つからないエラーを捕まえてリダイレクトするために rescue を使っています。

---

- [ ] `current_user.profile.room_memberships.find(params[:id])`とは？

👉 **ログインユーザーに紐づくデータだけを安全に取得する方法**

**解説：**
関連をたどって検索することで、自分のデータ以外にアクセスできないようにします。
セキュリティ対策として重要です。

```ruby
current_user.posts.find(params[:id])
```

このコードでは、自分の投稿だけを取得して他人のデータを防ぐために関連経由の find を使っています。

---

- [ ] `RoomMembership.find(params[:id])`とは？

👉 **IDだけでレコードを取得する方法（危険な場合あり）**

**解説：**
単純にIDで検索するため、他人のデータも取得できてしまう可能性があります。
認可チェックが必要です。

```ruby
RoomMembership.find(params[:id])
```

このコードでは、IDだけでデータを取得するために find を使っています。

---

- [ ] `IDOR (Insecure Direct Object Reference)`とは？

👉 **他人のデータに不正アクセスできてしまう脆弱性**

**解説：**
IDを直接指定して他人のデータにアクセスできる状態のことです。
関連を使った取得や認可チェックで防ぎます。

```ruby
Room.find(params[:id]) # 認可なし
```

このコードでは、他人のデータにもアクセスできる可能性があり、IDORの原因になる書き方です。

---

- [ ] `ActiveRecord::RecordNotFound`とは？

👉 **レコードが見つからなかったときに発生する例外**

**解説：**
`find` でデータが存在しない場合に発生します。
rescueしてリダイレクトなどに使います。

```ruby
Room.find(999)
```

このコードでは、存在しないIDを指定したときに RecordNotFound が発生します。

---

- [ ] `destroy! と destroy の違い`とは？

👉 **失敗時に例外を出すかどうかの違い**

**解説：**
`destroy` は失敗しても false を返します。
`destroy!` は失敗すると例外を発生させます。

```ruby
user.destroy!
```

このコードでは、削除に失敗したときに例外を発生させるために destroy! を使っています。

---

- [ ] `graceful に処理する`とは？

👉 **エラーで落とさずユーザーに優しく処理すること**

**解説：**
例外でアプリを止めるのではなく、メッセージ表示やリダイレクトで対応します。
ユーザー体験を守るために重要です。

```ruby
redirect_to root_path, alert: "見つかりませんでした"
```

このコードでは、エラーで落とさずユーザーにメッセージを表示するためにリダイレクトしています。

---

- [ ] `where.not`とは？

👉 **条件に一致しないレコードを取得するメソッド**

**解説：**
指定した条件を除外して検索したいときに使います。
SQLの NOT に相当します。

```ruby
User.where.not(role: "admin")
```

このコードでは、admin以外のユーザーを取得するために where.not を使っています。

---

- [ ] `ActiveRecord::Relation`とは？

👉 **クエリ結果を表すオブジェクト（まだ実行されていない状態）**

**解説：**
`where` などはすぐにデータを取得せず、クエリの条件だけを持つオブジェクトを返します。
実際にデータが取得されるのは `each` や `to_a` のときです。

```ruby
users = User.where(active: true)
```

このコードでは、まだ実行されていない検索条件を持つオブジェクトとして Relation を使っています。
