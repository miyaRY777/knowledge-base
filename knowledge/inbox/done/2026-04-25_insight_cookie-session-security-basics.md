{
- [ ] `Secure属性`とは？

👉 **CookieをHTTPS通信のときだけ送るための属性のこと**

**解説：**
`Secure` を付けると、そのCookieは暗号化されたHTTPS通信でのみ送信されます。
これにより、平文のHTTP通信でCookieが送られるのを防ぎ、盗み見される危険を下げます。 ([MDN Web Docs](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Headers/Set-Cookie "Set-Cookie ヘッダー - HTTP - MDN Web Docs"))

具体例：

```http
Set-Cookie: session_id=abc123; Path=/; Secure
```

このコードでは、セッションID入りのCookieをHTTPS通信のときだけ送るようにするために `Secure` 属性を使っています。

**注意点：**
`Secure` を付けても、それだけですべて安全になるわけではありません。
JavaScriptからのアクセスを防ぎたい場合は、`HttpOnly` もあわせて使うことが大切です。 ([MDN Web Docs](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Headers/Set-Cookie "Set-Cookie ヘッダー - HTTP - MDN Web Docs"))

---

- [ ] `HttpOnly属性`とは？

👉 **JavaScriptからCookieを読めなくするための属性**

**解説：**
`HttpOnly` を付けると、ブラウザ上のJavaScriptからそのCookieにアクセスできなくなります。
そのため、XSSによってセッションIDを盗まれる危険を減らすのに役立ちます。 ([MDN Web Docs](https://developer.mozilla.org/ja/docs/Web/HTTP/Guides/Cookies "HTTP Cookie の使用 - MDN Web Docs"))

具体例：

```http
Set-Cookie: session_id=abc123; Path=/; HttpOnly
```

このコードでは、JavaScriptからセッションID入りのCookieを読めないようにするために `HttpOnly` 属性を使っています。

**注意点：**
`HttpOnly` はJavaScriptからの読み取りを防ぐためのものです。
通信自体をHTTPSだけに限定したい場合は、`Secure` と組み合わせて使います。 ([MDN Web Docs](https://developer.mozilla.org/ja/docs/Web/HTTP/Guides/Cookies "HTTP Cookie の使用 - MDN Web Docs"))

---

- [ ] `セッションタイムアウト`とは？

👉 **一定時間、操作がないとセッションを終了させる仕組み**

**解説：**
セッションタイムアウトは、長時間放置されたログイン状態をそのままにしないための仕組みです。
一定時間リクエストがなければセッションを無効化する考え方で、盗まれたセッションが長く使われる危険を下げます。OWASP でも、**一定時間の無操作でセッションを終了する idle timeout** を実装すべきだと説明されています。 ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html "Session Management Cheat Sheet"))

```ruby
if session[:last_seen_at] && session[:last_seen_at] < 30.minutes.ago
  reset_session
end
session[:last_seen_at] = Time.current
```

このコードでは、一定時間アクセスがなかったときにセッションを破棄して、再ログインを必要にするために セッションタイムアウト を実装しています。

**注意点：**
`セッションタイムアウト` は Rails の特別な機能名ではありません。
何分で切るか、どこで判定するかはアプリ側の実装で決まります。また、OWASP は無操作タイムアウトだけでなく、一定時間で必ず切る **absolute timeout** も推奨しています。 ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html "Session Management Cheat Sheet"))
- [ ] `HTTPS`とは？

👉 **HTTP通信を暗号化して、安全にやり取りするための仕組み**

**解説：**
HTTPS は、HTTP を TLS で保護した通信方式です。
ブラウザとサーバーの間の通信内容を暗号化することで、盗み見や改ざんのリスクを下げます。MDN でも、HTTPS は HTTP を暗号化したバージョンだと説明されています。 ([MDN Web Docs](https://developer.mozilla.org/ja/docs/Glossary/HTTPS "HTTPS - MDN Web Docs 用語集"))

具体例：

```http
GET /login HTTP/1.1
Host: example.com
```

このコードでは、HTTPS で保護された通信の中で、ブラウザがサーバーにリクエストを送るイメージを表すために HTTP リクエストの形を書いています。

**注意点：**
HTTPS は通信を守る仕組みですが、アプリのバグまで自動で防ぐわけではありません。
ログイン情報やCookieを扱うページでは、HTTPS を使うことが重要です。 ([MDN Web Docs](https://developer.mozilla.org/ja/docs/Glossary/HTTPS "HTTPS - MDN Web Docs 用語集"))

---

- [ ] `クロスサイトスクリプティング（XSS）攻撃`とは？

👉 **悪意あるスクリプトをページに混ぜて、他のユーザーのブラウザで実行させる攻撃**

**解説：**
XSS は、Webアプリがユーザー入力を適切に検証・エスケープせずに表示したときに起こる代表的な攻撃です。
OWASP では、信頼されたWebページに悪意あるスクリプトが入り込み、別のユーザーのブラウザで実行される攻撃だと説明されています。 ([OWASP](https://owasp.org/www-community/attacks/xss/ "Cross Site Scripting (XSS)"))

具体例：

```erb
<p><%= params[:name] %></p>
```

このコードでは、受け取った値をページに表示する場面で、入力の扱いを誤ると XSS 攻撃 につながることがある、という例を表しています。

**注意点：**
XSS が起きると、画面の書き換えだけでなく、セッション情報の悪用やなりすましにつながることがあります。
対策としては、出力時のエスケープや、危険なHTMLをそのまま表示しないことが重要です。 ([OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html "Cross Site Scripting Prevention Cheat Sheet"))

---

- [ ] `セッションハイジャック`とは？

👉 **他人のセッションIDやセッションCookieを盗んで、本人になりすます攻撃**

**解説：**
セッションハイジャックは、攻撃者が有効なセッションIDを手に入れて、そのユーザーとしてアクセスする攻撃です。
OWASP では、セッション制御の仕組みを悪用し、セッショントークンを使って被害者になりすます攻撃だと説明されています。 ([OWASP](https://owasp.org/www-community/attacks/Session_hijacking_attack "Session hijacking attack"))

具体例：

```ruby
reset_session
session[:user_id] = user.id
```

このコードでは、ログイン時に古いセッションを引き継がないようにして、セッションハイジャック のリスクを下げるために `reset_session` を使っています。

**注意点：**
セッションIDが盗まれると、パスワードを知らなくてもログイン済みユーザーとして扱われることがあります。
対策としては、HTTPS の利用、`Secure` 属性や `HttpOnly` 属性の付与、ログイン時のセッション再生成などが重要です。 ([OWASP](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/06-Session_Management_Testing/09-Testing_for_Session_Hijacking "Testing for Session Hijacking"))}
