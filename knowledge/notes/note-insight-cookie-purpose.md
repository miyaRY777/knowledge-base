---
id: note-insight-cookie-purpose
title: Cookieが必要な理由
created: 2026-04-17
source: [[2026-04-17_insight_cookie-http-stateless.md]]
---

## Summary
- **Cookie は、ステートレスな HTTP でユーザーの状態を引き継ぐために使われます。**
- ログイン維持、カート保持、設定保存、表示の個別化などを実現できます。
- 便利な一方で、個人情報や安全性への配慮が必要です。

## Tags
#http #web #rails #要復習

## Links
- [[note-insight-cookie]]
- [[note-insight-stateless]]
- [[note-insight-rails-cookies]]

## Body
HTTP はステートレスなので、何もしないとユーザーの状態を次のリクエストへ持ち越せません。
Cookie はその弱点を補い、同じユーザーからのアクセスであることを見分けたり、前回の選択や設定を維持したりするために使われます。
代表例はログイン状態の維持ですが、ショッピングカートの保存、閲覧履歴に応じた表示、言語設定やテーマ設定の保持にも使われます。
一方で、Cookie はユーザー環境に保存されるので、何を保存するかを慎重に決める必要があります。

## Example
```http
Set-Cookie: user_id=12345
Cookie: user_id=12345
```

このコードでは、サーバーが保存を指示した値をブラウザが次回以降のリクエストで送り返しています。

## Action
- [ ] セッション管理とトラッキング用途を分けて整理する

<!-- review_log: 2026-04-17 -->
