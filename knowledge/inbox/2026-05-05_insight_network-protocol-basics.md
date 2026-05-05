`HTTP`とは？

👉 **WebブラウザとWebサーバーが、Webページなどのデータをやり取りするための通信ルール**

**解説：**
`HTTP` は、HTML文書などのリソースを取得するためのプロトコルです。
Webブラウザがサーバーに「このページをください」とリクエストし、サーバーが「この内容です」とレスポンスを返す流れで使われます。
参考: [MDN Web Docs - Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) / [MDN Web Docs - HTTP messages](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Messages)

**具体例：**
- ブラウザで `https://example.com` にアクセスする
- ブラウザがサーバーへリクエストを送る
- サーバーがHTMLや画像などをレスポンスとして返す

この例では、Webページを表示するために `HTTP` が関係しています。

---

- [ ] `FTP（File Transfer Protocol）`とは？

👉 **ネットワークを通じてファイルを転送するための通信ルール**

**解説：**
`FTP` は、あるコンピューターから別のコンピューターへファイルを送ったり、受け取ったりするためのプロトコルです。
Webサイトのファイルをサーバーへアップロードするときなどに使われることがあります。
参考: [Cloudflare Docs - Glossary: FTP](https://developers.cloudflare.com/spectrum/glossary/) / [Cloudflare Docs - FTP](https://developers.cloudflare.com/spectrum/about/ftp/)

**具体例：**
- 自分のPCにある画像ファイルをサーバーへアップロードする
- サーバー上のHTMLファイルをダウンロードする
- FTPソフトを使って、サーバー内のファイルを確認する

この例では、ファイルをネットワーク経由でやり取りするために `FTP` が関係しています。

---

- [ ] `SMTP（Simple Mail Transfer Protocol）`とは？

👉 **メールを送信するための通信ルール**

**解説：**
`SMTP` は、メールを送信者からメールサーバーへ送ったり、メールサーバー同士で配送したりするためのプロトコルです。
メールを「受信して読む」ためのプロトコルではなく、主に「送る・届ける」ために使われます。
参考: [Cloudflare - SMTPとは](https://www.cloudflare.com/ja-jp/learning/email-security/what-is-smtp/) / [Cloudflare - What SMTP port should be used?](https://www.cloudflare.com/learning/email-security/smtp-port-25-587/)

**具体例：**
- Railsアプリからユーザーに確認メールを送る
- パスワード再設定メールをメールサーバーへ送信する
- SendGridなどのメール配信サービスを使ってメールを届ける

この例では、アプリからメールを送信するために `SMTP` が関係しています。

---

- [ ] `TCP/IP`とは？

👉 **インターネット上でデータを相手に届けるための基本的な通信ルールのまとまり**

**解説：**
`TCP/IP` は、インターネット通信の土台になるプロトコル群です。
`IP` はデータをどこへ届けるかを扱い、`TCP` はデータが順番どおり・確実に届くようにする役割を持ちます。
参考: [Cloudflare - What is TCP/IP?](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/) / [Cloudflare - インターネットプロトコルとは？](https://www.cloudflare.com/ja-jp/learning/network-layer/internet-protocol/)

**具体例：**
- ブラウザでWebサイトを見る
- Railsアプリが外部APIと通信する
- メールやファイル転送など、ネットワーク上でデータを送る

この例では、インターネット上でデータを正しい相手に届ける土台として `TCP/IP` が関係しています。
