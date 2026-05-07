* [ ] `200 OK`とは？

👉 **リクエストが成功したことを表すHTTPステータスコード**

**解説：**
`200 OK` は、クライアントのリクエストが成功し、サーバーが正常にレスポンスを返したことを示します。
HTTPステータスコードのうち、`200` 番台は成功レスポンスに分類されます。
参考: [MDN HTTP レスポンスステータスコード](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Status), [IANA HTTP Status Code Registry](https://www.iana.org/assignments/http-status-codes)

**具体例：**

* ユーザーが一覧ページにアクセスする
* サーバーがページのHTMLを正常に返す
* ブラウザに画面が表示される

この例では、リクエストが成功したことを表すために `200 OK` が関係しています。

---

* [ ] `301 Moved Permanently`とは？

👉 **リソースが恒久的に別のURLへ移動したことを表すHTTPステータスコード**

**解説：**
`301 Moved Permanently` は、リクエストされたURLが今後も別のURLに移動したことを示します。
ブラウザや検索エンジンは、新しいURLへリダイレクトされるものとして扱います。
参考: [MDN 301 Moved Permanently](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Status/301), [IANA HTTP Status Code Registry](https://www.iana.org/assignments/http-status-codes)

**具体例：**

* 古いURL：`/old-profile`
* 新しいURL：`/profile`
* 古いURLにアクセスすると、新しいURLへ自動で移動する

この例では、ページのURLが恒久的に変わったことを伝えるために `301 Moved Permanently` が関係しています。

---

* [ ] `404 Not Found`とは？

👉 **リクエストされたリソースが見つからないことを表すHTTPステータスコード**

**解説：**
`404 Not Found` は、サーバーがリクエストされたページやデータを見つけられなかったことを示します。
URLが間違っている場合や、対象のページが削除されている場合などに返されます。
参考: [MDN 404 Not Found](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Status/404), [IANA HTTP Status Code Registry](https://www.iana.org/assignments/http-status-codes)

**具体例：**

* 存在しないURLにアクセスする
* 削除済みの記事ページを開こうとする
* 存在しないIDの詳細ページにアクセスする

この例では、指定されたページやデータが見つからないことを表すために `404 Not Found` が関係しています。

---

* [ ] `500 Internal Server Error`とは？

👉 **サーバー内部で予期しないエラーが起きたことを表すHTTPステータスコード**

**解説：**
`500 Internal Server Error` は、サーバー側で予期しない問題が起き、リクエストを正常に処理できなかったことを示します。
Railsアプリでは、未処理の例外や設定ミスなどで発生することがあります。
参考: [MDN 500 Internal Server Error](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Status/500), [RFC 9110](https://datatracker.ietf.org/doc/rfc9110/)

**具体例：**

* Railsアプリで予期しない例外が発生する
* サーバー設定に問題がある
* 本来表示できるはずのページでエラー画面が出る

この例では、サーバー側の処理に失敗したことを表すために `500 Internal Server Error` が関係しています。

---

* [ ] `403 Forbidden`とは？

👉 **リクエスト内容は理解されたが、アクセスが拒否されたことを表すHTTPステータスコード**

**解説：**
`403 Forbidden` は、サーバーがリクエストを理解したものの、アクセスを許可しない場合に返されます。
ログイン済みでも権限が足りないページにアクセスしたときなどに使われます。
参考: [MDN 403 Forbidden](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Status/403), [IANA HTTP Status Code Registry](https://www.iana.org/assignments/http-status-codes)

**具体例：**

* 一般ユーザーが管理者画面にアクセスする
* 自分に権限のない編集ページを開こうとする
* アクセス許可されていないファイルを表示しようとする

この例では、アクセス権がないリクエストを拒否するために `403 Forbidden` が関係しています。

---

* [ ] `502 Bad Gateway`とは？

👉 **中継サーバーが上流サーバーから不正な応答を受け取ったことを表すHTTPステータスコード**

**解説：**
`502 Bad Gateway` は、ゲートウェイやプロキシとして動くサーバーが、上流サーバーから有効な応答を受け取れなかった場合に返されます。
Railsアプリ本体だけでなく、Webサーバー、プロキシ、外部サービスとの連携部分で問題が起きている可能性があります。
参考: [MDN 502 Bad Gateway](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Status/502), [IANA HTTP Status Code Registry](https://www.iana.org/assignments/http-status-codes)

**具体例：**

* NginxがRailsアプリサーバーから正常な応答を受け取れない
* プロキシサーバーが上流サーバーとの通信に失敗する
* デプロイ先のサービスでアプリサーバーが落ちている

この例では、中継役のサーバーが上流サーバーから正しい応答を受け取れなかったことを表すために `502 Bad Gateway` が関係しています。
