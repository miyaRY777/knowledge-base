---
id: note-insight-third-party-cookie
title: "サードパーティCookieは閲覧中のサイトとは別ドメインのサービスが設定するCookie"
created: 2026-04-18
source: [[2026-04-18_insight_cookie-basics-and-security.md]]
review_streak: 1
last_reviewed_on: 2026-04-30
quiz_fail_log: []
---

## Summary
- **サードパーティCookie は、閲覧中のサイトとは別ドメインのサービスが設定する Cookie です。**
- 広告配信やアクセス解析などで使われてきました。
- 複数サイトをまたぐ追跡に使われやすいため、プライバシー面の制限対象になりやすいです。

## Tags
#http #web #cookie #privacy

## Links
- [[note-insight-cookie]]
- [[note-insight-first-party-cookie]]
- [[note-insight-cookie-samesite]]

## Body
サードパーティCookie は、今開いているページそのものではなく、埋め込まれた外部サービスや別ドメインの仕組みが設定する Cookie です。
代表例として、広告配信やアクセス解析でユーザー行動を複数のサイトにまたがって把握したい場面があります。
そのぶんプライバシー上の懸念が大きく、近年はブラウザ側で制限されたり、無効化の対象になったりすることが増えています。

## Example
```http
Set-Cookie: tracking_id=xyz789; Domain=analytics.example.com; Path=/
```

このコードでは、閲覧中のサイトとは別の解析サービスが追跡用の Cookie を設定しています。

## Action
- [ ] ブラウザごとのサードパーティCookie制限の違いも確認する
<!-- review_log: 2026-04-18 -->
