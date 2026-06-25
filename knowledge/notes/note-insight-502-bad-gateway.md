---
id: note-insight-502-bad-gateway
title: "502 Bad Gatewayは中継サーバーが上流から有効な応答を受け取れない状態"
created: 2026-05-07
source: [[2026-05-07_insight_http-status-codes]]
review_streak: 0
last_reviewed_on: 2026-05-25
quiz_fail_log: []
---

## Summary
- `502 Bad Gateway` は、ゲートウェイやプロキシが上流サーバーから有効な応答を受け取れないことを表します。
- Webサーバー、プロキシ、アプリサーバー、外部サービスの連携部分で問題が起きている可能性があります。
- Rails アプリ本体だけでなく、Nginx やデプロイ先の構成も確認対象になります。

## Tags
#http #web #status-code #server #operations

## Links
- [[note-insight-http-status-code]]
- [[note-insight-on-premise]]

## Body
`502 Bad Gateway` は、ゲートウェイやプロキシとして動くサーバーが、上流サーバーから有効な応答を受け取れなかった場合に返すHTTPステータスコードです。クライアントから見るとサーバーエラーですが、原因は中継役と上流サーバーの間にあることが多いです。

たとえば Nginx が Rails アプリサーバーへリクエストを渡そうとしたものの、アプリサーバーが落ちていたり、通信できなかったりすると発生します。外部サービスやデプロイ先の構成が絡むこともあるため、アプリのログだけでなくインフラ側の状態も確認します。

## Example
- Nginx が Rails アプリサーバーから正常な応答を受け取れない
- プロキシサーバーが上流サーバーとの通信に失敗する
- デプロイ先のサービスでアプリサーバーが落ちている


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] 502 と 500 の切り分け方を整理する
