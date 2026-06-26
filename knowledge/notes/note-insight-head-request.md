---
id: note-insight-head-request
title: "HEADは本文なしでヘッダーだけを取得するHTTPメソッド"
created: 2026-05-06
source: [[2026-05-06_insight_http-message-methods]]
review_streak: 0
last_reviewed_on: 2026-05-25
quiz_fail_log: []
---

## Summary
- `HEAD` は、`GET` に近いがレスポンス本文を返さないHTTPメソッドです。
- ヘッダーだけを見て、ページやファイルの存在、サイズ、更新情報などを確認できます。
- 本文が不要な確認処理で通信量を抑えたいときに役立ちます。

## Tags
#http #web #network

## Links
- [[note-insight-get-request]]
- [[note-insight-http-response]]

## Body
`HEAD` は、`GET` と同じように指定したリソースについて問い合わせますが、レスポンス本文は受け取りません。返ってくるのはステータス行やヘッダーだけです。

本文そのものを表示したいわけではなく、ページやファイルが存在するか、どんな種類のデータか、サイズはどれくらいかを確認したい場面で使えます。本文を受け取らないため、内容確認だけなら通信量を小さくできます。

## Example
```http
HEAD /index.html HTTP/1.1
Host: example.com
```

この例では、`/index.html` の本文を取得せずに、ヘッダー情報だけを確認しようとしています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
