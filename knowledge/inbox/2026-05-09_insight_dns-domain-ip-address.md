* [ ] `IPアドレス`とは？

👉 **インターネット上で通信相手を見つけるための住所のような番号**

**解説：**
`IPアドレス` は、IPネットワーク上の機器を一意に指定するための番号です。
Webサイトを見るときも、最終的にはサーバーのIPアドレスを使って通信します。
IPv4の例は `192.0.2.172`、IPv6の例は `2001:db8:8b73:0000:0000:8a2e:0370:1337` のような形です。
参考: MDN / ICANN ([MDNウェブドキュメント][1])

**具体例：**

* 自分のPCやスマホがインターネットに接続する
* ブラウザでWebサイトにアクセスする
* 通信先のサーバーを見つけるためにIPアドレスが使われる

この例では、ネットワーク上で通信相手を特定するために `IPアドレス` が関係しています。

---

* [ ] `ドメイン`とは？

👉 **人間が覚えやすいWebサイトの住所**

**解説：**
`ドメイン` は、`example.com` のように、人間が読みやすい形でWebサイトを指定するための名前です。
コンピューター同士の通信ではIPアドレスが使われますが、人間が毎回数字の住所を覚えるのは大変なので、ドメイン名が使われます。
参考: MDN / Cloudflare ([MDNウェブドキュメント][2])

**具体例：**

* `google.com`
* `github.com`
* `example.com`

この例では、Webサイトにアクセスしやすくするために `ドメイン` が関係しています。

---

* [ ] `DNS`とは？

👉 **ドメイン名をIPアドレスに変換する仕組み**

**解説：**
`DNS` は、Domain Name System の略です。
`example.com` のようなドメイン名と、それに対応するIPアドレスなどの情報を結びつける仕組みです。
よく「インターネットの電話帳」のように説明されます。
参考: MDN / ICANN / Cloudflare ([MDNウェブドキュメント][3])

**具体例：**

* ブラウザに `example.com` と入力する
* DNSが `example.com` に対応するIPアドレスを探す
* 見つかったIPアドレスのサーバーへアクセスする

この例では、人間が入力したドメイン名を、コンピューターが通信できるIPアドレスに変換するために `DNS` が関係しています。

[1]: https://developer.mozilla.org/en-US/docs/Glossary/IP_Address?utm_source=chatgpt.com "IP Address - Glossary - MDN Web Docs"
[2]: https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_domain_name?utm_source=chatgpt.com "What is a Domain Name? - Learn web development | MDN"
[3]: https://developer.mozilla.org/en-US/docs/Glossary/DNS?utm_source=chatgpt.com "DNS - Glossary - MDN Web Docs - Mozilla"
