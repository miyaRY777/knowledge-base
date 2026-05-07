---
id: note-insight-403-forbidden
title: "403 Forbiddenは理解されたリクエストのアクセス拒否を表す"
created: 2026-05-07
source: [[2026-05-07_insight_http-status-codes]]
---

## Summary
- `403 Forbidden` は、サーバーがリクエストを理解したもののアクセスを許可しないことを表します。
- ログイン済みでも権限が足りないページにアクセスしたときなどに使われます。
- 認証済みかどうかより、操作や閲覧の権限があるかが焦点になります。

## Tags
#http #web #status-code #authorization #security

## Links
- [[note-insight-http-status-code]]
- [[note-insight-database-permission-control]]
- [[note-insight-authorize-and-allowed-to-difference]]

## Body
`403 Forbidden` は、サーバーがリクエスト内容を理解したうえで、アクセスを許可しない場合に返すHTTPステータスコードです。ログインしていても、管理者専用画面や自分に権限のない編集ページへアクセスした場合に関係します。

「誰か分からないから拒否する」というより、「何をしたいかは分かるが、その権限はない」と考えると整理しやすいです。Rails アプリでは認可処理とつながりやすいステータスコードです。

## Example
- 一般ユーザーが管理者画面にアクセスする
- 自分に権限のない編集ページを開こうとする
- アクセス許可されていないファイルを表示しようとする

## Action
- [ ] `401 Unauthorized` との違いを整理する
