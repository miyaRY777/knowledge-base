---
id: note-insight-http-request
title: HTTPの要点
created: 2026-04-07
source: [[2026-04-17_insight_cookie-http-stateless.md]]
---

## Summary（3行）
- **HTTP は、Webブラウザとサーバーが通信するためのルールです。**
- ブラウザは HTTP を使ってページ表示やフォーム送信、API 通信を行います。
- `GET` や `POST` などのリクエスト方法があり、Web の基本的なやり取りを支えています。

## Tags
#javascript #http

## Links
- [[note-insight-cookie]]
- [[note-insight-stateless]]
- [[関連ノート]]

## Body
HTTP は、ブラウザやアプリとサーバーがデータをやり取りするための共通ルールです。
Web ページを開く、フォームを送信する、API からデータを取得するといった処理は、どれも HTTP に基づいて行われます。
HTTP の通信はリクエストとレスポンスで成り立っており、ブラウザが「このページを見せてほしい」「このデータを保存してほしい」と依頼し、サーバーがその結果を返します。
また HTTP はステートレスなので、ログイン状態の維持には Cookie などの補助的な仕組みが必要です。

## Example
```http
GET /index.html HTTP/1.1
Host: example.com
```

このコードでは、ブラウザがサーバーに `index.html` を返してほしいと依頼しています。
