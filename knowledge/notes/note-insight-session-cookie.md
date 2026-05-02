---
id: note-insight-session-cookie
title: "セッションCookieの要点"
created: 2026-04-18
source: [[2026-04-18_insight_cookie-basics-and-security.md]]
review_streak: 0
last_reviewed_on: 2026-04-30
---

## Summary
- **セッションCookie は、主にブラウザを閉じるまで保持される一時的な Cookie です。**
- ログイン中の状態や画面遷移中の情報を保つ用途でよく使われます。
- 有効期限を明示しない Cookie は、この扱いになることがあります。

## Tags
#http #web #cookie #session #要復習

## Links
- [[note-insight-cookie]]
- [[note-insight-persistent-cookie]]
- [[note-insight-set-cookie-header]]

## Body
セッションCookie は、ユーザーがサイトを使っている間だけ必要な情報を保持したいときに使われる Cookie です。
典型的にはログイン中の識別や、一連の操作の途中状態を保つ場面で使われます。
永続的な保存期間を持つ Cookie と違って、ブラウザを閉じると消える前提で扱われることが多いため、一時的な状態管理と相性がよいです。

## Example
```http
Set-Cookie: session_id=abc123; Path=/; HttpOnly
```

このコードでは、アクセス中の状態を識別するための `session_id` を一時的な Cookie として保存しています。

## Action
- [ ] セッションとサーバー側セッションストアの関係も整理する

<!-- review_log: 2026-04-25 -->
