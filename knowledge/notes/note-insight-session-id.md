---
id: note-insight-session-id
title: "セッションIDはサーバー側でどのユーザーのセッションかを見分けるための識別子"
created: 2026-04-21
source: [[2026-04-21_insight_session-cookie-basics.md]]
review_streak: 1
last_reviewed_on: 2026-06-18
---

## Summary
- **セッションID は、どのユーザーのセッションかを見分けるための識別子です。**
- サーバー側セッションでは、ブラウザは参照キーとしてセッションIDを持つのが一般的です。
- Rails のデフォルト CookieStore では、セッションデータ自体を暗号化 Cookie に保存します。
- セッションID が漏れると他人になりすませる危険があるため、取り扱いには注意が必要です。
- セッションID はサーバーが発行し、Cookie 経由でブラウザに保存され、以後のリクエストで自動送信されます。

## Tags
#http #web #session #security

## Links
- [[note-insight-session]]
- [[note-insight-session-vs-cookie]]
- [[note-insight-cookie-header]]
- [[note-insight-set-cookie-header]]

## Body
セッションID は、サーバー側に保存されているセッション情報を見つけるための識別子です。
サーバー側セッションでは、ブラウザはログイン情報やカート内容そのものではなく、その情報に対応するセッションIDだけを保持します。
サーバーはリクエストで送られてきた ID を見て、どのユーザーの状態を使うかを判断します。
初回のセッション作成時には、サーバーがこの ID を発行し、`Set-Cookie` ヘッダーなどを通してブラウザへ渡します。
ブラウザは保存した Cookie を次回以降のリクエストに自動で含めるため、サーバーは同じユーザーのセッション情報を再び取り出せます。
この ID が第三者に漏れると、本来のユーザーになりすましてアクセスされるおそれがあるため、安全な管理が重要です。

ただし Rails のデフォルトである CookieStore では、セッションデータ自体を暗号化した Cookie としてブラウザ側に保存します。そのため、Rails では「必ずサーバー側に本体がある」とは限りません。

## Example
```http
Cookie: _app_session=abc123xyz
```

このコードでは、ブラウザが保存しているセッションIDをサーバーに送り、対応するセッション情報を特定できるようにしています。

```http
Set-Cookie: _app_session=abc123xyz; Path=/; HttpOnly
```

このコードでは、サーバーが発行したセッションIDをブラウザへ渡して保存させています。

## Action
- [ ] セッション固定化攻撃との関係を別ノートで整理する
