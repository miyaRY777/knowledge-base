`SSL/TLS`とは？

👉 **Web上の通信を暗号化して、安全にやり取りするための仕組み**

**解説：**
`SSL/TLS` は、ブラウザとサーバーの通信を暗号化し、盗み見や改ざんを防ぐための仕組みです。
現在のWebでは主に `TLS` が使われていますが、昔の呼び方として `SSL` という名前もよく使われます。
`HTTPS` は、HTTP通信を SSL/TLS で安全にしたものです。
参考: [MDN - TLS](https://developer.mozilla.org/ja/docs/Glossary/TLS) / [MDN - HTTPS](https://developer.mozilla.org/ja/docs/Glossary/HTTPS) / [Cloudflare - SSLの仕組み](https://www.cloudflare.com/ja-jp/learning/ssl/how-does-ssl-work/)

**具体例：**
- `http://example.com` は通信が暗号化されていない
- `https://example.com` は SSL/TLS によって通信が暗号化されている
- ログイン画面や決済画面では、パスワードやカード情報を守るために HTTPS が使われる

この例では、ブラウザとサーバーの通信を安全にするために `SSL/TLS` が関係しています。
