#   - [ ] `通信プロトコル`とは？

👉 **コンピューター同士が通信するときの約束ごと**

**解説：**
`通信プロトコル` は、データをどの形式で送り、どう受け取り、どう返事するかを決めたルールです。
HTTPは、HTMLなどのWeb上のリソースをやり取りするための通信プロトコルです。
参考: [MDN HTTP の概要](https://developer.mozilla.org/ja/docs/Web/HTTP/Guides/Overview)

**具体例：**
- ブラウザがサーバーに「このページをください」と送る
- サーバーが「このHTMLを返します」と返す
- そのやり取りのルールとしてHTTPが使われる

この例では、ブラウザとサーバーが同じルールで通信するために `通信プロトコル` が関係しています。

---

- [ ] `HTTPリクエスト`とは？

👉 **クライアントからサーバーへ送るお願いのメッセージ**

**解説：**
`HTTPリクエスト` は、ブラウザなどのクライアントがサーバーに対して「ページを取得したい」「データを送信したい」などを伝えるメッセージです。
HTTPメッセージには、クライアントから送るリクエストと、サーバーから返すレスポンスがあります。
参考: [MDN HTTP メッセージ](https://developer.mozilla.org/ja/docs/Web/HTTP/Guides/Messages)

**具体例：**

```http
GET /index.html HTTP/1.1
Host: www.runteq.jp
Connection: keep-alive
```

**この具体例の中身：**

```http
GET /index.html HTTP/1.1
```

これは **リクエストライン** です。
- `GET`
  サーバーからデータを取得したい、という意味です。
- `/index.html`
  取得したいページやファイルの場所です。
- `HTTP/1.1`
  使用しているHTTPのバージョンです。

この行では、`/index.html` というページを取得したいことをサーバーに伝えています。

```http
Host: www.runteq.jp
```

これは **HTTPヘッダー** です。
`Host` は、「どのホストに向けたリクエストか」を伝える情報です。
この例では、`www.runteq.jp` に対してリクエストしています。

```http
Connection: keep-alive
```

これも **HTTPヘッダー** です。
`keep-alive` は、通信をすぐに切らず、同じ接続を再利用できるようにする指定です。

**流れのイメージ：**
- ブラウザで `https://www.runteq.jp/index.html` にアクセスする
- ブラウザがサーバーに `GET /index.html` を送る
- サーバーがそのリクエストを見て、HTMLを返す

この例では、ブラウザがページを取得するために `HTTPリクエスト` を使っています。

---

- [ ] `HTTPレスポンス`とは？

👉 **サーバーからクライアントへ返す返事のメッセージ**

**解説：**
`HTTPレスポンス` は、HTTPリクエストに対してサーバーが返すメッセージです。
レスポンスには、ステータス行、ヘッダー、空行、本文が含まれることがあります。
ステータスコードは、リクエストが成功したかどうかなどを表します。
参考: [MDN HTTP メッセージ](https://developer.mozilla.org/ja/docs/Web/HTTP/Guides/Messages) / [MDN HTTP レスポンスステータスコード](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Status)

**具体例：**

```http
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2020 12:28:53 GMT
Server: Apache/2.4.7 (Ubuntu)
Content-Length: 1212
Content-Type: text/html; charset=UTF-8

<html>
  <head><title>Welcome</title></head>
  <body><h1>Welcome</h1></body>
</html>
```

**この具体例の中身：**

```http
HTTP/1.1 200 OK
```

これは **ステータス行** です。
- `HTTP/1.1`
  使用しているHTTPのバージョンです。
- `200`
  リクエストが成功したことを表すステータスコードです。
- `OK`
  `200` の意味を人間が読みやすくした説明です。

この行では、「リクエストは成功しました」とサーバーが返しています。

```http
Date: Mon, 27 Jul 2020 12:28:53 GMT
```

これは **HTTPヘッダー** です。
`Date` は、サーバーがレスポンスを作成した日時を表します。

```http
Server: Apache/2.4.7 (Ubuntu)
```

これは **HTTPヘッダー** です。
`Server` は、レスポンスを返したサーバーソフトウェアの情報です。
この例では、Ubuntu上のApacheサーバーが返していることを示しています。

```http
Content-Length: 1212
```

これは **HTTPヘッダー** です。
`Content-Length` は、レスポンス本文のサイズを表します。
この例では、本文の長さが `1212` バイトであることを示しています。

```http
Content-Type: text/html; charset=UTF-8
```

これは **HTTPヘッダー** です。
`Content-Type` は、返されるデータの種類を表します。
この例では、本文がHTMLで、文字コードが `UTF-8` であることを示しています。

ヘッダーのあとにある空行は、**ここまでがヘッダーで、ここから本文です** という区切りです。

```html
<html>
  <head><title>Welcome</title></head>
  <body><h1>Welcome</h1></body>
</html>
```

これは **レスポンス本文** です。
ブラウザはこのHTMLを受け取り、画面に `Welcome` と表示します。

**流れのイメージ：**
- ブラウザが `GET /index.html` を送る
- サーバーが `200 OK` を返す
- サーバーがHTMLを返す
- ブラウザがHTMLを画面に表示する

この例では、サーバーがリクエストの結果としてHTMLを返すために `HTTPレスポンス` を使っています。

---

- [ ] `GET`とは？

👉 **サーバーからデータを取得するためのHTTPメソッド**

**解説：**
`GET` は、指定したリソースを取得したいときに使うHTTPメソッドです。
Railsでは、一覧画面や詳細画面を表示するときによく使われます。
参考: [MDN GET](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Methods/GET)

```http
GET /posts HTTP/1.1
Host: example.com
```

このコードでは、投稿一覧を取得するために `GET` を使っています。

---

- [ ] `POST`とは？

👉 **サーバーにデータを送信して、新しいデータを作成するときによく使うHTTPメソッド**

**解説：**
`POST` は、指定したリソースにデータを送るためのHTTPメソッドです。
Railsでは、新規作成フォームを送信して、データを保存するときによく使われます。
参考: [MDN POST](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Methods/POST)

```http
POST /posts HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded

title=Hello
```

このコードでは、新しい投稿データを送信するために `POST` を使っています。

---

- [ ] `PUT`とは？

👉 **既存データ全体を置き換えるときに使うHTTPメソッド**

**解説：**
`PUT` は、指定したリソースを作成または置き換えるためのHTTPメソッドです。
Railsでは更新処理に使われることがありますが、部分的な更新では `PATCH` が使われることも多いです。
参考: [MDN PUT](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Methods/PUT)

```http
PUT /posts/1 HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded

title=Updated&body=NewBody
```

このコードでは、IDが1の投稿全体を更新するために `PUT` を使っています。

---

- [ ] `DELETE`とは？

👉 **指定したデータを削除するためのHTTPメソッド**

**解説：**
`DELETE` は、指定したリソースを削除するときに使うHTTPメソッドです。
Railsでは、投稿やコメントなどを削除する処理でよく使われます。
参考: [MDN DELETE](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Methods/DELETE)

```http
DELETE /posts/1 HTTP/1.1
Host: example.com
```

このコードでは、IDが1の投稿を削除するために `DELETE` を使っています。

---

- [ ] `HEAD`とは？

👉 **本文なしで、ヘッダー情報だけを取得するHTTPメソッド**

**解説：**
`HEAD` は、`GET` と同じようなレスポンスを求めますが、レスポンス本文は返しません。
ページやファイルが存在するか、サイズや更新情報を確認したいときに使われます。
参考: [MDN HEAD](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Methods/HEAD)

```http
HEAD /index.html HTTP/1.1
Host: example.com
```

このコードでは、`/index.html` の本文を取得せずに、ヘッダー情報だけを確認するために `HEAD` を使っています。

---

- [ ] `PATCH`とは？

👉 **既存データの一部を更新するためのHTTPメソッド**

**解説：**
`PATCH` は、指定したリソースの一部を変更するときに使うHTTPメソッドです。
Railsでは、編集フォームから既存データを更新するときによく使われます。
参考: [MDN PATCH](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Methods/PATCH)

```http
PATCH /posts/1 HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded

title=NewTitle
```

このコードでは、IDが1の投稿のタイトルだけを更新するために `PATCH` を使っています。
