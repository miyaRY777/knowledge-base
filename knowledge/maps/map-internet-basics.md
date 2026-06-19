# インターネット基礎マップ

> **このMOCで分かること**: インターネットの仕組み・HTTPメソッド・URL・APIエンドポイントまでの基礎を俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | インターネット | 世界中のコンピューターをつなぐネットワークの集合体 | [[note-insight-internet]] |
| 2 | GETリクエスト | リソースを取得するHTTPメソッド | [[note-insight-get-request]] |
| 3 | POSTリクエスト | データを送信してリソースを作成するHTTPメソッド | [[note-insight-post-request]] |
| 4 | PUTリクエスト | リソースを全体更新するHTTPメソッド | [[note-insight-put-request]] |
| 5 | PATCHリクエスト | リソースを部分更新するHTTPメソッド | [[note-insight-patch-request]] |
| 6 | DELETEリクエスト | リソースを削除するHTTPメソッド | [[note-insight-delete-request]] |
| 7 | HEADリクエスト | レスポンスヘッダーだけを取得するHTTPメソッド | [[note-insight-head-request]] |
| 8 | べき等性 | 同じリクエストを何度送っても結果が変わらない性質 | [[note-insight-idempotent]] |
| 9 | ステートレス | HTTPはリクエストをまたいで状態を保持しない | [[note-insight-stateless]] |
| 10 | APIエンドポイント | クライアントがAPIにアクセスするURL | [[note-insight-api-endpoint]] |
| 11 | 絶対URL | ドメインから始まる完全なURL | [[note-insight-absolute-url]] |
| 12 | 相対URL | 現在のパスを基準にした省略形URL | [[note-insight-relative-url]] |
| 13 | リクエストメソッドの別名 | フレームワークでPUT/DELETEを扱うための仕組み | [[note-insight-request-method-alias]] |

---

## インターネットとは

[[note-insight-internet]]
[[note-insight-stateless]]

**ポイント**:
- インターネットはTCP/IPプロトコルで接続されたネットワークのネットワーク
- HTTPはステートレス。リクエストをまたいで状態を保持しない。状態管理にはCookieやセッションを使う

---

## HTTPメソッドの種類と使い分け

[[note-insight-get-request]]
[[note-insight-post-request]]
[[note-insight-put-request]]
[[note-insight-patch-request]]
[[note-insight-delete-request]]
[[note-insight-head-request]]
[[note-insight-request-method-alias]]

**ポイント**:
- GET: 読み取り専用。URLにパラメータを付けて送る。副作用なし・べき等
- POST: データを送信して新規作成。リクエストボディにデータを入れる。べき等ではない
- PUT: リソース全体を置き換える更新。べき等
- PATCH: リソースの一部だけ更新。べき等とは限らない
- DELETE: リソースを削除する。べき等
- HEAD: GETと同じだがボディを返さない。存在確認やキャッシュ確認に使う
- HTMLフォームはGETとPOSTしか使えない。PUT/DELETEは `_method` パラメータで代替する

---

## べき等性とサイドエフェクト

[[note-insight-idempotent]]

**ポイント**:
- べき等（idempotent）: 同じ操作を複数回実行しても結果が1回実行したのと同じ
- GET・HEAD・PUT・DELETE はべき等。POST・PATCH はべき等でない場合がある
- APIを安全に設計するためにべき等性を意識する。ネットワーク障害でリトライするときに重要

---

## URLとAPIエンドポイント

[[note-insight-api-endpoint]]
[[note-insight-absolute-url]]
[[note-insight-relative-url]]

**ポイント**:
- APIエンドポイントはクライアントとサーバーが通信する入口のURL
- RESTful APIでは「リソース名/ID」の形式でエンドポイントを設計する（例: `/users/1`）
- 絶対URLは他ドメインとの通信に。相対URLは同一オリジン内の参照に使うことが多い

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| RESTful APIの設計原則をまとめる | - | - | - |
| CORS（クロスオリジンリソース共有）のノートを作成する | - | - | - |
| WebSocketとHTTPの違いを整理する | - | - | - |

---

## 関連リンク

- [[map-network-basics]]
- [[map-http-status-and-methods]]
- [[map-http-client-basics]]
- [[map-web-basics]]
- [[map-dns-domain-basics]]
