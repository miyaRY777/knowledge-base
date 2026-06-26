---
id: note-insight-session-hijacking
title: "セッションハイジャックは盗んだセッションIDで本人になりすます攻撃"
created: 2026-04-25
source: [[2026-04-25_insight_cookie-session-security-basics.md]]
quiz_streak: 2
quiz_fail_log: []
---

## Summary
- セッションハイジャックは、有効なセッションIDを盗んで本人になりすます攻撃。
- パスワードを知らなくてもログイン済みユーザーとして扱われる危険がある。
- HTTPS、Cookie 属性、ログイン時のセッション再生成などが対策になる。

## Tags
#http #web #session #security

## Links
- [[note-insight-session-id]]
- [[note-insight-cookie-secure]]
- [[note-insight-cookie-httponly]]

## Body
セッションハイジャックは、攻撃者が有効なセッションIDやセッションCookieを手に入れて、そのユーザーとしてアクセスする攻撃です。セッションIDが盗まれると、パスワードを知らなくてもログイン済みユーザーとして扱われることがあります。そのため、通信を HTTPS で保護し、Cookie に `Secure` や `HttpOnly` を付け、ログイン時にセッションを再生成することが重要になります。

## Example
```ruby
reset_session
session[:user_id] = user.id
```

このコードでは、ログイン時に古いセッションを引き継がないようにして、セッションハイジャックのリスクを下げています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
