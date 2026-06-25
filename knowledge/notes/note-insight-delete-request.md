---
id: note-insight-delete-request
title: "DELETEは指定したリソースを削除するHTTPメソッド"
created: 2026-05-06
source: [[2026-05-06_insight_http-message-methods]]
review_streak: 0
last_reviewed_on: 2026-05-25
quiz_fail_log: []
---

## Summary
- `DELETE` は、指定したリソースを削除するためのHTTPメソッドです。
- 投稿やコメントなど、既存データを消す処理で使われます。
- Rails では destroy アクションと対応して考えると分かりやすいです。

## Tags
#http #rails #web

## Links
- [[note-insight-http-request]]
- [[note-insight-destroy-vs-destroy-bang]]
- [[note-insight-idempotent]]

## Body
`DELETE` は、サーバー上の指定したリソースを削除したいときに使う HTTP メソッドです。投稿、コメント、プロフィール画像など、既に存在するデータを消す操作に対応します。

Rails では RESTful なルーティングの中で、削除処理は `destroy` アクションとして扱われます。HTTP のメソッドとしては `DELETE /posts/1` のように、どのリソースを削除したいのかをパスで伝えます。

## Example
```http
DELETE /posts/1 HTTP/1.1
Host: example.com
```

この例では、ID が 1 の投稿を削除したいことをサーバーに伝えています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] 論理削除と物理削除の違いとつなげて整理する
