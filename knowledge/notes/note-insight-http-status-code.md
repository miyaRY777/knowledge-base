---
id: note-insight-http-status-code
title: "HTTPステータスコードはレスポンスの結果を表す番号"
created: 2026-05-07
source: [[2026-05-07_insight_http-status-codes]]
review_streak: 0
last_reviewed_on: 2026-05-13
quiz_fail_log: []
---

## Summary
- HTTPステータスコードは、HTTPレスポンスでリクエスト結果を表す番号です。
- `2xx` は成功、`3xx` はリダイレクト、`4xx` はクライアント側の問題、`5xx` はサーバー側の問題を表します。
- ブラウザやアプリはステータスコードを見て、成功表示、リダイレクト、エラー表示などを判断できます。

## Tags
#http #web #status-code

## Links
- [[note-insight-http-response]]
- [[note-insight-200-ok]]
- [[note-insight-301-moved-permanently]]
- [[note-insight-404-not-found]]
- [[note-insight-500-internal-server-error]]
- [[note-insight-403-forbidden]]
- [[note-insight-502-bad-gateway]]

## Body
HTTPステータスコードは、サーバーが HTTPレスポンスで「リクエストをどう扱ったか」をクライアントへ伝える番号です。成功したのか、別のURLへ移動すべきなのか、リクエスト側に問題があるのか、サーバー側で問題が起きたのかを大まかに分類できます。

代表的には、`200` 番台は成功、`300` 番台はリダイレクト、`400` 番台はクライアント側の問題、`500` 番台はサーバー側の問題を表します。Rails アプリでも、画面表示、認可エラー、存在しないページ、サーバー例外などを理解するときに重要な手がかりになります。

## Example
```http
HTTP/1.1 200 OK
```

この例では、リクエストが成功したことをサーバーが伝えています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
