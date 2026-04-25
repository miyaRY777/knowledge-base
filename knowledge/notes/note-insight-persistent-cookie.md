---
id: note-insight-persistent-cookie
title: 永続Cookieの要点
created: 2026-04-18
source: [[2026-04-18_insight_cookie-basics-and-security.md]]review_streak: 0
---

## Summary
- **永続Cookie は、有効期限までブラウザに残る Cookie です。**
- ブラウザを閉じても保持されるため、再訪時の設定やログイン状態の維持に使われます。
- 便利な一方で、長く残るぶん保存内容には注意が必要です。

## Tags
#http #web #cookie #要復習

## Links
- [[note-insight-cookie]]
- [[note-insight-session-cookie]]
- [[note-insight-cookie-expires]]
- [[note-insight-set-cookie-header]]

## Body
永続Cookie は、`Expires` や `Max-Age` などで保存期間を指定して、一定期間ブラウザに残す Cookie です。
次回アクセス時にも前回の情報を引き継ぎたいときに使いやすく、言語設定やログイン状態の維持でよく見かけます。
ただし、ユーザーの端末に長く残るため、保存する値が安全かどうかを意識して設計する必要があります。

## Example
```http
Set-Cookie: user_locale=ja; Expires=Wed, 21 Oct 2026 07:28:00 GMT; Path=/
```

このコードでは、言語設定を次回アクセス時にも使えるように、期限付きで Cookie を保持しています。

## Action
- [ ] `Expires` と `Max-Age` の使い分けも確認する
