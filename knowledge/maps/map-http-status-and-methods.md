# HTTPステータスコード・メソッド詳細マップ

> **このMOCで分かること**: 主要なHTTPステータスコードの意味と使い分け、PUTやDELETEなどの全メソッドの役割を俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | HTTPステータスコード | サーバーからのレスポンス結果を表す3桁の数字 | [[note-insight-http-status-code]] |
| 2 | HTTPレスポンス | サーバーがクライアントへ返す返答の全体 | [[note-insight-http-response]] |
| 3 | 200 OK | リクエスト成功 | [[note-insight-200-ok]] |
| 4 | 301 Moved Permanently | 恒久的なリダイレクト | [[note-insight-301-moved-permanently]] |
| 5 | 403 Forbidden | 認証済みでもアクセス権限がない | [[note-insight-403-forbidden]] |
| 6 | 404 Not Found | リソースが見つからない | [[note-insight-404-not-found]] |
| 7 | 500 Internal Server Error | サーバー側の予期しないエラー | [[note-insight-500-internal-server-error]] |
| 8 | 502 Bad Gateway | 上流サーバーから不正な応答が返ってきた | [[note-insight-502-bad-gateway]] |
| 9 | PUTリクエスト | リソースの全体を置き換える | [[note-insight-put-request]] |
| 10 | PATCHリクエスト | リソースの一部を更新する | [[note-insight-patch-request]] |
| 11 | DELETEリクエスト | リソースを削除する | [[note-insight-delete-request]] |
| 12 | HEADリクエスト | レスポンスボディなしでヘッダーだけ取得する | [[note-insight-head-request]] |

---

## ステータスコードの分類

[[note-insight-http-status-code]]
[[note-insight-http-response]]

**ポイント**:
- 2xx: 成功 / 3xx: リダイレクト / 4xx: クライアントエラー / 5xx: サーバーエラー
- ステータスコードはHTTPレスポンスの一部。ヘッダー・ボディもセットで理解する

---

## よく使うステータスコード

[[note-insight-200-ok]]
[[note-insight-301-moved-permanently]]
[[note-insight-403-forbidden]]
[[note-insight-404-not-found]]
[[note-insight-500-internal-server-error]]
[[note-insight-502-bad-gateway]]

**ポイント**:
- 200: 正常完了。GETでもPOSTでも使われる
- 301: URL変更の恒久リダイレクト。SEOにも影響する
- 403 vs 404: 403はアクセス権なし（存在は知っている）、404はそもそも見つからない
- 500: アプリのバグや例外が原因が多い
- 502: プロキシ・ロードバランサの上流で問題が発生している

---

## HTTPメソッドの全体像

[[note-insight-put-request]]
[[note-insight-patch-request]]
[[note-insight-delete-request]]
[[note-insight-head-request]]

**ポイント**:
- PUT: リソース全体を置き換える（存在しなければ作成）。冪等
- PATCH: リソースの一部だけ更新する。PUTより細かい変更向き
- DELETE: リソースを削除する。冪等
- HEAD: GETと同じURLにヘッダーだけを問い合わせる。ファイルサイズ確認などに使う

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| 401 Unauthorized と 403 Forbidden の違いを整理する | - | - | [[note-insight-403-forbidden]] |
| OPTIONSメソッド（CORS preflight）を別ノートにするか | - | - | - |

---

## 関連リンク

- [[map-http-client-basics]]
- [[map-web-security-basics]]
- [[note-insight-idempotent]]
