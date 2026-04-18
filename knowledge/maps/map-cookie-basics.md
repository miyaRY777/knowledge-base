# Cookie基礎マップ

> **このMOCで分かること**: Cookie の役割、送受信の流れ、保持期間、セキュリティ属性、プライバシー論点のつながり

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | ステートレス | HTTP が前回状態を自動保持しない性質 | [[note-insight-stateless]] |
| 2 | Cookie | ブラウザに状態を保存する仕組み | [[note-insight-cookie]] |
| 3 | Cookieが必要な理由 | ステートレスな HTTP を補う考え方 | [[note-insight-cookie-purpose]] |
| 4 | Set-Cookieヘッダー | サーバーが Cookie 保存を指示するレスポンスヘッダー | [[note-insight-set-cookie-header]] |
| 5 | Cookieヘッダー | ブラウザが Cookie を送り返すリクエストヘッダー | [[note-insight-cookie-header]] |
| 6 | セッションCookie | 一時的に保持される Cookie | [[note-insight-session-cookie]] |
| 7 | 永続Cookie | 有効期限まで残る Cookie | [[note-insight-persistent-cookie]] |
| 8 | expires属性 | Cookie の有効期限を決める属性 | [[note-insight-cookie-expires]] |
| 9 | ファーストパーティCookie | 閲覧中サイト自身が設定する Cookie | [[note-insight-first-party-cookie]] |
| 10 | サードパーティCookie | 別ドメインのサービスが設定する Cookie | [[note-insight-third-party-cookie]] |
| 11 | HttpOnly属性 | JavaScript から Cookie を参照できなくする属性 | [[note-insight-cookie-httponly]] |
| 12 | Secure属性 | HTTPS のときだけ Cookie を送る属性 | [[note-insight-cookie-secure]] |
| 13 | SameSite属性 | クロスサイト送信を制御する属性 | [[note-insight-cookie-samesite]] |
| 14 | Cookie削除 | 不要になった Cookie を無効化する方法 | [[note-insight-cookie-deletion]] |
| 15 | Rails cookies | Rails で Cookie を読み書きする仕組み | [[note-insight-rails-cookies]] |

---

## セクション1: Cookie が必要になる前提

[[note-insight-stateless]]
[[note-insight-cookie]]
[[note-insight-cookie-purpose]]

**ポイント**:
- HTTP はステートレスなので、そのままではログイン状態や設定を継続できない
- Cookie はその不足を補うために、ブラウザ側へ状態を持たせる仕組み
- まず「なぜ必要か」を押さえると、各属性の役割も理解しやすい

---

## セクション2: Cookie の送受信

[[note-insight-set-cookie-header]]
[[note-insight-cookie-header]]
[[note-insight-rails-cookies]]

**ポイント**:
- サーバーは `Set-Cookie` で保存を指示し、ブラウザは `Cookie` ヘッダーで送り返す
- Rails の `cookies` は、このやり取りをアプリ側から扱う入口になる
- Cookie は保存だけでなく、次回リクエストでどう返るかまでセットで理解する

---

## セクション3: 保持期間と種類

[[note-insight-session-cookie]]
[[note-insight-persistent-cookie]]
[[note-insight-cookie-expires]]
[[note-insight-first-party-cookie]]
[[note-insight-third-party-cookie]]

**ポイント**:
- セッションCookieと永続Cookieは「どれだけ残るか」の違い
- ファーストパーティCookieとサードパーティCookieは「誰が設定するか」の違い
- サードパーティCookieは追跡に使われやすく、プライバシー上の制限対象になりやすい

---

## セクション4: セキュリティと送信制御

[[note-insight-cookie-httponly]]
[[note-insight-cookie-secure]]
[[note-insight-cookie-samesite]]
[[note-insight-cookie-deletion]]

**ポイント**:
- `HttpOnly` は JavaScript から読ませない
- `Secure` は HTTPS の通信だけに限定する
- `SameSite` はクロスサイト送信を制御し、CSRF 対策とプライバシー整理に関わる
- 不要になった Cookie は削除まで含めて状態管理を考える

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| `Expires` と `Max-Age` をどう使い分けるか | - | - | [[note-insight-persistent-cookie]] |
| `Lax` `Strict` `None` の違いを実際のリクエストでどう見分けるか | - | - | [[note-insight-cookie-samesite]] |
| サードパーティCookieのブラウザ別制限はどう違うか | - | - | [[note-insight-third-party-cookie]] |
| セッションCookieとサーバー側セッションストアの関係はどう整理するか | - | - | [[note-insight-session-cookie]] |
| `Path` や `Domain` が違う Cookie をどう削除するか | - | - | [[note-insight-cookie-deletion]] |

---

## 関連リンク

- [[map-http-client-basics]]
- [[note-insight-stateless]]
- [[note-insight-cookie]]
- [[note-insight-cookie-purpose]]
- [[note-insight-set-cookie-header]]
- [[note-insight-cookie-header]]
- [[note-insight-session-cookie]]
- [[note-insight-persistent-cookie]]
- [[note-insight-cookie-expires]]
- [[note-insight-first-party-cookie]]
- [[note-insight-third-party-cookie]]
- [[note-insight-cookie-httponly]]
- [[note-insight-cookie-secure]]
- [[note-insight-cookie-samesite]]
- [[note-insight-cookie-deletion]]
- [[note-insight-rails-cookies]]
