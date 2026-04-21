---
id: note-insight-session-vs-cookie
title: セッションとCookieの違い
created: 2026-04-21
source: [[2026-04-21_insight_session-cookie-basics.md]]
---

## Summary
- **セッションと Cookie の大きな違いは、情報をどこに保存するかです。**
- セッションは主にサーバー側で状態本体を管理し、Cookie はブラウザ側で値を保持します。
- 実際の Web アプリでは、Cookie にセッションIDを保存してサーバー側セッションを参照する組み合わせがよく使われます。

## Tags
#http #web #session #cookie

## Links
- [[note-insight-session]]
- [[note-insight-session-id]]
- [[note-insight-cookie]]
- [[note-insight-cookie-purpose]]
- [[note-insight-session-cookie]]

## Body
セッションは、ログイン状態のような重要な状態本体をサーバー側で管理する仕組みです。
一方で Cookie は、ブラウザ側に保存される小さなデータで、設定値や識別用の値を保持する用途で使われます。
このため、セッションは状態管理向きで、Cookie はブラウザに値を持たせたい場面に向いています。
実際には両者は対立するものではなく、Cookie にセッションIDを保存し、サーバー側で対応するセッション情報を引く形で一緒に使われることが多いです。

## Example
```text
セッション: サーバー側に保存
Cookie: ブラウザ側に保存
```

この例では、セッションと Cookie の保存場所の違いを並べて整理しています。

## Action
- [ ] セッションCookie との違いも一緒に説明できるようにする
