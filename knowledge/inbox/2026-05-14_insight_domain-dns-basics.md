`ドメイン名`とは？

👉 **Webサイトやメールで使う、インターネット上の名前**

**解説：**
`ドメイン名` は、`runteq.jp` のように、人間が覚えやすい形でWebサイトなどを識別するための名前です。
JPRSでは、ドメイン名はURLやメールアドレスの一部として使われ、インターネット上のコンピューターを識別する名前と説明されています。 ([JPRS](https://jprs.jp/related-info/domain/?utm_source=chatgpt.com "ドメイン名とは"))

**具体例：**
- `https://runteq.jp`
- `example.com`
- `miyary777.com`

この例では、Webサイトにアクセスしやすくするために `ドメイン名` が関係しています。

---

- [ ] `ドメイン登録`とは？

👉 **使いたいドメイン名を、一定期間使えるように申し込むこと**

**解説：**
`ドメイン登録` は、使いたいドメイン名を登録サービスを通して申し込み、利用できる状態にする手続きです。
JPRSでは、ドメイン名の登録者はドメイン名を「所有する」のではなく、一定期間使用する権利を持つ考え方が一般的と説明されています。 ([JPRS](https://jprs.jp/related-info/domain/?utm_source=chatgpt.com "ドメイン名とは"))

**具体例：**
- `example.com` を使いたい
- ドメイン登録サービスで空き状況を確認する
- 登録して、一定期間使えるようにする

この例では、自分のWebサイト用の名前を使えるようにするために `ドメイン登録` が関係しています。

---

- [ ] `ドメイン登録機関`とは？

👉 **ドメイン名の登録や管理を受け付ける事業者**

**解説：**
`ドメイン登録機関` は、ユーザーからドメイン名の登録申し込みを受け付ける事業者です。
ICANNは、ドメイン名はICANN認定レジストラやリセラーを通じて登録できると説明しています。 ([icann.org](https://www.icann.org/resources/pages/domain-name-registration-process-2023-11-02-en?utm_source=chatgpt.com "The Domain Name Registration Process"))

**具体例：**
- お名前.com
- ゴンベエドメイン
- Google Domains のようなドメイン登録サービス

この例では、使いたいドメイン名を申し込んで管理するために `ドメイン登録機関` が関係しています。

---

- [ ] `DNS`とは？

👉 **ドメイン名とIPアドレスを対応づける仕組み**

**解説：**
`DNS` は、`example.com` のようなドメイン名を、WebサーバーのIPアドレスに結びつける仕組みです。
JPRSでは、ドメイン名とIPアドレスの対応付けを行う仕組みをDNSと説明しています。 ([JPRS](https://jprs.jp/related-info/about/address/?utm_source=chatgpt.com "ドメイン名は「インターネット上 の住所表示」"))

**具体例：**
- ユーザーが `example.com` にアクセスする
- DNSが対応するIPアドレスを探す
- ブラウザがWebサーバーへアクセスする

この例では、ドメイン名からWebサーバーを見つけるために `DNS` が関係しています。

---

- [ ] `DNSサーバー`とは？

👉 **ドメイン名に対応する情報を返すサーバー**

**解説：**
`DNSサーバー` は、ドメイン名に関する問い合わせに答えるサーバーです。
JPRSでは、DNSサーバーは階層化されており、目的の問い合わせ先がわかるDNSサーバーまで誘導すると説明されています。 ([JPRS](https://jprs.jp/related-info/about/address/?utm_source=chatgpt.com "ドメイン名は「インターネット上 の住所表示」"))

**具体例：**
- `example.com` のIPアドレスを知りたい
- DNSサーバーに問い合わせる
- 必要な情報が返ってくる

この例では、ドメイン名から接続先を調べるために `DNSサーバー` が関係しています。

---

- [ ] `DNS設定`とは？

👉 **ドメイン名をどのサーバーにつなげるか決める設定**

**解説：**
`DNS設定` は、ドメイン名をWebサーバーやメールサーバーなどに結びつけるための設定です。
Cloudflareのドキュメントでは、DNSレコードはドメインに関する情報を持ち、Webサイトやアプリを利用者に提供するために使われると説明されています。 ([Cloudflare Docs](https://developers.cloudflare.com/dns/manage-dns-records/?utm_source=chatgpt.com "DNS records"))

**具体例：**
- `example.com` をRenderのアプリに向ける
- `www.example.com` を別のドメイン名に向ける
- メール用の設定を追加する

この例では、ドメイン名を実際のサービスに接続するために `DNS設定` が関係しています。

---

- [ ] `Aレコード`とは？

👉 **ドメイン名をIPv4アドレスに向けるDNSレコード**

**解説：**
`Aレコード` は、ドメイン名とIPv4アドレスを結びつけるためのDNS設定です。
たとえば、自分のドメインを特定のWebサーバーのIPアドレスに向けたいときに使います。

```txt
example.com  A  203.0.113.10
```

このコードでは、`example.com` を `203.0.113.10` に向けるために `Aレコード` を使っています。

---

- [ ] `CNAMEレコード`とは？

👉 **あるドメイン名を、別のドメイン名の別名として扱うDNSレコード**

**解説：**
`CNAMEレコード` は、サブドメインなどを別のドメイン名に向けるときに使います。
Cloudflareでは、CNAMEレコードは別名のドメインを正規名のドメインに向けるもので、IPアドレスではなくドメイン名を指定すると説明されています。 ([Cloudflare](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/?utm_source=chatgpt.com "What is a DNS CNAME record?"))

```txt
www.example.com  CNAME  example.com
```

このコードでは、`www.example.com` を `example.com` の別名として扱うために `CNAMEレコード` を使っています。
