# HTTPクライアント基礎マップ

> **このMOCで分かること**: JavaScript から API 通信を行うときの基本概念と、Axios / Fetch の使い分け

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | HTTPリクエスト | サーバーへデータ取得や送信を行う通信の基本 | [[note-insight-http-request]] |
| 2 | Promise | 非同期処理の結果をあとで受け取る仕組み | [[note-insight-promise]] |
| 3 | Fetch API | ブラウザ標準の HTTP 通信機能 | [[note-insight-fetch-api]] |
| 4 | Axios | HTTP 通信を簡潔に書ける外部ライブラリ | [[note-insight-axios]] |
| 5 | GETリクエスト | データ取得に使う基本メソッド | [[note-insight-get-request]] |
| 6 | POSTリクエスト | 新規データ送信に使う基本メソッド | [[note-insight-post-request]] |
| 7 | リクエストメソッドエイリアス | `axios.get` などの短い呼び出し方 | [[note-insight-request-method-alias]] |
| 8 | Axiosインスタンス | 共通設定をまとめて使い回す方法 | [[note-insight-axios-instance]] |
| 9 | baseURL | URL の共通部分をまとめる設定 | [[note-insight-base-url]] |
| 10 | timeout | 通信の待ち時間を制御する設定 | [[note-insight-timeout]] |
| 11 | headers | 追加情報を通信に載せる仕組み | [[note-insight-headers]] |
| 12 | Content-Type | 送信データの形式を伝えるヘッダー | [[note-insight-content-type]] |
| 13 | JSONPlaceholder | HTTP 通信を試せる練習用 API | [[note-insight-jsonplaceholder]] |
| 14 | ステートレス | HTTP が前回状態を自動保持しない性質 | [[note-insight-stateless]] |
| 15 | Cookie | ブラウザに状態を保存する仕組み | [[note-insight-cookie]] |
| 16 | Cookieが必要な理由 | ステートレスな HTTP を補う考え方 | [[note-insight-cookie-purpose]] |
| 17 | Set-Cookieヘッダー | サーバーが Cookie 保存を指示するレスポンスヘッダー | [[note-insight-set-cookie-header]] |
| 18 | Cookieヘッダー | ブラウザが Cookie を送り返すリクエストヘッダー | [[note-insight-cookie-header]] |
| 19 | expires属性 | Cookie の有効期限を決める属性 | [[note-insight-cookie-expires]] |
| 20 | HttpOnly属性 | JavaScript から Cookie を参照できなくする属性 | [[note-insight-cookie-httponly]] |
| 21 | Secure属性 | HTTPS のときだけ Cookie を送る属性 | [[note-insight-cookie-secure]] |
| 22 | Rails cookies | Rails で Cookie を読み書きする仕組み | [[note-insight-rails-cookies]] |
| 23 | APIエンドポイント | APIへリクエストを送る入口のURL | [[note-insight-api-endpoint]] |

---

## セクション1: 通信の土台

[[note-insight-http-request]]
[[note-insight-promise]]
[[note-insight-fetch-api]]
[[note-insight-axios]]
[[note-insight-api-endpoint]]

**ポイント**:
- 通信の基本単位は HTTP リクエスト
- JavaScript では通信結果を Promise として受け取る
- Fetch は標準機能、Axios は使いやすさが強み
- APIエンドポイントは、HTTPリクエストを送る具体的な入口として見る

---

## セクション2: 具体的な送受信

[[note-insight-get-request]]
[[note-insight-post-request]]
[[note-insight-request-method-alias]]

**ポイント**:
- 読み取りは GET、新規送信は POST から覚える
- Axios のエイリアスを使うとコードの意味が読みやすい

---

## セクション3: 実務で使う設定

[[note-insight-axios-instance]]
[[note-insight-base-url]]
[[note-insight-timeout]]
[[note-insight-headers]]
[[note-insight-content-type]]
[[note-insight-jsonplaceholder]]

**ポイント**:
- 通信設定は Axios インスタンスに寄せると保守しやすい
- `headers` と `Content-Type` は API 仕様の理解とセット
- 練習段階では JSONPlaceholder が便利

---

## セクション4: 状態保持と Cookie

[[note-insight-stateless]]
[[note-insight-cookie]]
[[note-insight-cookie-purpose]]
[[note-insight-set-cookie-header]]
[[note-insight-cookie-header]]
[[note-insight-cookie-expires]]
[[note-insight-cookie-httponly]]
[[note-insight-cookie-secure]]
[[note-insight-rails-cookies]]

**ポイント**:
- HTTP はステートレスなので、そのままではログイン状態を維持できない
- サーバーは `Set-Cookie` で保存を指示し、ブラウザは `Cookie` ヘッダーで送り返す
- `expires` `HttpOnly` `Secure` は Cookie の保持期間や安全性を調整する属性

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| Fetch API と Axios を実務でどう使い分けるか | - | - | [[note-insight-fetch-api]] |
| 通信失敗時の標準的なエラーハンドリングの型は何か | - | - | [[note-insight-promise]] |
| 認証付き API で headers をどう設計するか | - | - | [[note-insight-headers]] |
| SameSite 属性をどう整理するか | - | - | [[note-insight-cookie-samesite]] |

---

## 関連リンク

- [[map-cookie-basics]]
- [[note-insight-http-request]]
- [[note-insight-promise]]
- [[note-insight-fetch-api]]
- [[note-insight-axios]]
- [[note-insight-get-request]]
- [[note-insight-post-request]]
- [[note-insight-request-method-alias]]
- [[note-insight-axios-instance]]
- [[note-insight-base-url]]
- [[note-insight-timeout]]
- [[note-insight-headers]]
- [[note-insight-content-type]]
- [[note-insight-jsonplaceholder]]
- [[note-insight-stateless]]
- [[note-insight-cookie]]
- [[note-insight-cookie-purpose]]
- [[note-insight-set-cookie-header]]
- [[note-insight-cookie-header]]
- [[note-insight-cookie-expires]]
- [[note-insight-cookie-httponly]]
- [[note-insight-api-endpoint]]
- [[note-insight-cookie-secure]]
- [[note-insight-rails-cookies]]
