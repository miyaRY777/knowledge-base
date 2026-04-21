---
id: note-insight-session
title: セッションの要点
created: 2026-04-21
source: [[2026-04-21_insight_session-cookie-basics.md]]
---

## Summary
- **セッションは、ユーザーごとの状態をサーバー側で一時的に管理する仕組みです。**
- HTTP は各リクエストで状態を自動保持しないため、ログイン状態やカート情報の維持にセッションが使われます。
- ブラウザ側には本体ではなく識別用のセッションIDだけを持たせる構成が一般的です。

## Tags
#http #web #rails #session

## Links
- [[note-insight-stateless]]
- [[note-insight-session-id]]
- [[note-insight-session-vs-cookie]]
- [[note-insight-cookie]]
- [[note-insight-session-cookie]]

## Body
セッションは、HTTP のステートレス性を補うために、ユーザーごとの状態をサーバー側で保持する仕組みです。
Web アプリでは、ログイン中のユーザー識別やカート内容の保持のように、ページをまたいで同じ人の状態を引き継ぎたい場面でよく使われます。
ブラウザに保存するのは通常セッション情報そのものではなく、対応するデータを引くためのセッションIDだけです。
この役割分担によって、重要な状態本体はサーバー側に置いたまま、継続した利用体験を作れます。

## Example
```ruby
session[:user_id] = current_user.id
```

このコードでは、ログイン中のユーザーIDをセッションに保存して、次のリクエストでも同じユーザーとして識別できるようにしています。

## Action
- [ ] Rails の session が内部で Cookie とどう連携するかを確認する
