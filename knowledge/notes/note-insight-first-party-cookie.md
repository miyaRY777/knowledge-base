---
id: note-insight-first-party-cookie
title: ファーストパーティCookieの要点
created: 2026-04-18
source: [[2026-04-18_insight_cookie-basics-and-security.md]]
---

## Summary
- **ファーストパーティCookie は、今見ているサイト自身が設定する Cookie です。**
- サイト内のログイン状態や表示設定など、基本機能の維持によく使われます。
- 普段の Web 利用で最も一般的に出てくる Cookie の形です。

## Tags
#http #web #cookie

## Links
- [[note-insight-cookie]]
- [[note-insight-third-party-cookie]]
- [[note-insight-set-cookie-header]]

## Body
ファーストパーティCookie は、ユーザーが現在アクセスしているサイトのドメインが自分で設定する Cookie です。
そのサイトの中だけで状態を保ったり、好みの設定を覚えたりする用途に向いています。
ログイン状態の維持やテーマ設定の保存など、サイトの基本機能を支える場面でよく使われます。

## Example
```http
Set-Cookie: theme=dark; Path=/; Secure
```

このコードでは、現在アクセスしているサイトが表示設定を記憶するために Cookie を設定しています。

## Action
- [ ] `Domain` 属性が指定されたときの適用範囲も確認する
