---
id: note-insight-session
title: "セッションの要点"
created: 2026-04-21
source: [[2026-04-21_insight_session-cookie-basics.md]]
---

## Summary
- **セッションは、ユーザーごとの状態をリクエスト間で一時的に管理する仕組みです。**
- HTTP は各リクエストで状態を自動保持しないため、ログイン状態やカート情報の維持にセッションが使われます。
- サーバー側に本体を置き、ブラウザ側に識別用のセッションIDだけを持たせる構成が一般的です。
- Rails のデフォルト CookieStore では、セッションデータ自体を暗号化 Cookie に保存します。
- セッション管理は、最初のアクセスで始まり、サーバー側で状態を保存して次のリクエストへつなげる流れとして理解できます。

## Tags
#http #web #rails #session #要復習 #要復習

## Links
- [[note-insight-stateless]]
- [[note-insight-session-id]]
- [[note-insight-session-vs-cookie]]
- [[note-insight-cookie]]
- [[note-insight-session-cookie]]
- [[note-insight-session-termination]]

## Body
セッションは、HTTP のステートレス性を補うために、ユーザーごとの状態をリクエスト間で保持する仕組みです。
Web アプリでは、ログイン中のユーザー識別やカート内容の保持のように、ページをまたいで同じ人の状態を引き継ぎたい場面でよく使われます。
一般的なサーバー側セッションでは、ブラウザに保存するのはセッション情報そのものではなく、対応するデータを引くためのセッションIDだけです。
ただし Rails のデフォルトである CookieStore は例外で、セッションデータ自体を暗号化した Cookie としてブラウザ側に保存します。
最初にユーザーがサイトへアクセスすると、サーバーは必要に応じてそのユーザー用のセッションを用意し、以後は同じセッションを使って状態を引き継ぎます。
保存先の方式は異なっても、セッションは状態を次のリクエストへつなげるために使われます。

## Example
```ruby
session[:user_id] = current_user.id
```

このコードでは、ログイン中のユーザーIDをセッションに保存して、次のリクエストでも同じユーザーとして識別できるようにしています。

```ruby
session[:cart_item_ids] ||= []
```

このコードでは、ユーザーごとのセッション内にカート情報を保存する場所を用意して、あとから状態を保持できるようにしています。

## Action
- [ ] Rails の session が内部で Cookie とどう連携するかを確認する

<!-- review_log: 2026-04-25,2026-04-25 -->
