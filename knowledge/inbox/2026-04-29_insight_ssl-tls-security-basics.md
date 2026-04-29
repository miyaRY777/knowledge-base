`SSL（Secure Sockets Layer）`とは？

👉 **インターネット通信を暗号化するために使われていた古い仕組み**

**解説：**
`SSL` は、Webサイトとブラウザの間の通信を暗号化し、盗み見や改ざんを防ぐために使われていたセキュリティプロトコルです。
現在は `SSL` そのものではなく、後継の `TLS` が使われています。
ただし、慣習として「SSL証明書」「SSL化」のように呼ばれることがあります。 ([cloudflare.com](https://www.cloudflare.com/learning/ssl/what-is-ssl/?utm_source=chatgpt.com "What is SSL (Secure Sockets Layer)?"))

**具体例：**
- `http://example.com` では、通信内容が暗号化されていない
- `https://example.com` では、TLSによって通信が暗号化される
- ただし、一般的にはこれを「SSL化」と呼ぶことがある

この例では、Webサイトとブラウザの通信を安全にするために `SSL` が関係しています。

---

- [ ] `TLS（Transport Layer Security）`とは？

👉 **現在使われている、インターネット通信を安全にするための暗号化の仕組み**

**解説：**
`TLS` は、ブラウザとWebサーバーの通信を暗号化し、通信内容の盗み見や改ざんを防ぐためのプロトコルです。
MDNでは、現在のバージョンは `TLS 1.3` で、`TLS 1.2` も一部のWebサイトで使われている一方、`TLS 1.0` と `TLS 1.1`は使うべきではないと説明されています。 ([MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Transport_Layer_Security?utm_source=chatgpt.com "Transport Layer Security (TLS) - MDN Web Docs"))

**具体例：**
- ユーザーがログインフォームにメールアドレスとパスワードを入力する
- ブラウザが `https://` のWebサイトに送信する
- TLSによって通信内容が暗号化され、途中で盗み見されにくくなる

この例では、ログイン情報を安全に送信するために `TLS` が関係しています。

---

- [ ] `ファイアウォール`とは？

👉 **通信を通してよいか、止めるべきかを判断するセキュリティの仕組み**

**解説：**
`ファイアウォール` は、ネットワークに入ってくる通信や出ていく通信を確認し、条件に応じて許可・ブロックする仕組みです。
Microsoftの説明では、IPアドレス、ポート番号、アプリケーションなどの条件にもとづいて通信を制御できるとされています。 ([Microsoft Learn](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/?utm_source=chatgpt.com "Windows Firewall Overview"))

**具体例：**
- Webサーバーでは、Webアクセス用の `80番` や `443番` ポートは許可する
- 管理用のポートは、特定のIPアドレスからだけ許可する
- 不審な通信はブロックする

この例では、必要な通信だけを通して不要な通信を防ぐために `ファイアウォール` が関係しています。

---

- [ ] `二要素認証（2FA: Two-Factor Authentication）`とは？

👉 **2種類以上の確認方法を使って、本人確認を強くする仕組み**

**解説：**
`二要素認証` は、パスワードだけでなく、スマホアプリの確認コードや生体認証など、別の要素も使ってログインする仕組みです。
NISTでは、認証要素として「知っているもの」「持っているもの」「本人自身の特徴」が説明されています。 ([NISTコンピュータセキュリティリソースセンター](https://csrc.nist.gov/glossary/term/2fa?utm_source=chatgpt.com "2FA - Glossary | CSRC"))

**具体例：**
- 1つ目の要素：パスワードを入力する
- 2つ目の要素：スマホの認証アプリに表示されたコードを入力する
- 両方が正しい場合だけログインできる

この例では、パスワードが漏れても不正ログインされにくくするために `二要素認証` が関係しています。

`SSLとTLSの違い`とは？

👉 **SSLは古い暗号化の仕組み、TLSは現在使われている後継の仕組み**

**解説：**
`SSL` は、昔使われていた通信暗号化の仕組みです。
現在のWeb通信では、SSLではなく後継の `TLS` が使われています。
Cloudflareでは、SSLは1996年の `SSL 3.0` 以降更新されておらず、現在は非推奨と説明されています。 ([Cloudflare](https://www.cloudflare.com/learning/ssl/what-is-ssl/))

**具体例：**
- 昔の呼び方：`SSL`
- 現在の実体：`TLS`
- よくある言い方：`SSL証明書`
- 実際に使われる技術：`TLS証明書` / `TLS通信`

この例では、名前としては `SSL` と呼ばれることがあっても、実際の安全な通信には `TLS` が関係しています。
- [ ] `SSL証明書`とは？

👉 **名前はSSLでも、実際にはTLS通信で使われる証明書のことが多い**

**解説：**
実務では今でも「SSL証明書」という言葉がよく使われます。
しかし、現在のHTTPS通信で使われている仕組みは基本的に `TLS` です。
つまり「SSL証明書」は昔から残っている呼び方で、実体としてはTLS通信のための証明書と考えるとわかりやすいです。 ([Cloudflare](https://www.cloudflare.com/learning/ssl/what-is-ssl/))

**具体例：**
- サーバーに証明書を設定する
- ブラウザがその証明書を確認する
- 問題なければ `https://` で安全に通信できる

この例では、サーバーが本物か確認し、暗号化通信を始めるために `SSL証明書` が関係しています。
