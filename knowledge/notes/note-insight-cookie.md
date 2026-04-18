---
id: note-insight-cookie
title: Cookieの要点
created: 2026-04-17
source: [[2026-04-17_insight_rails-cookies-headers-and-attributes.md]]
---

## Summary
- **Cookie は、ブラウザに保存される小さなデータです。**
- Web サイトは Cookie を使って、ログイン状態や表示設定などを次回アクセス時にも引き継げます。
- サーバーは `Set-Cookie` ヘッダーで保存を指示し、ブラウザは次回以降のリクエストで `Cookie` ヘッダーとして送り返します。

## Tags
#http #web #rails #cookie

## Links
- [[note-insight-cookie-purpose]]
- [[note-insight-rails-cookies]]
- [[note-insight-stateless]]
- [[note-insight-set-cookie-header]]
- [[note-insight-cookie-header]]
- [[note-insight-session-cookie]]
- [[note-insight-persistent-cookie]]
- [[note-insight-first-party-cookie]]
- [[note-insight-third-party-cookie]]
- [[note-insight-cookie-samesite]]
- [[note-insight-cookie-deletion]]

## Body
Cookie は、Web サイトがユーザーの状態をブラウザ側に覚えさせるための仕組みです。
HTTP の通信はそれぞれ独立しているため、何もしないと「誰がアクセスしているか」や「前回どんな設定だったか」を自動では保持できません。
そこでサーバーは `Set-Cookie` ヘッダーを使って識別用の情報や設定情報をブラウザに保存し、ブラウザは次のリクエストで `Cookie` ヘッダーとしてその値を送り返します。
このやり取りによって、Web サイトはログイン状態や設定を維持しているように見せられます。
ただし Cookie はユーザーの手元に保存されるため、機密情報をそのまま入れるのではなく、安全な値だけを扱う前提が大切です。

## Example
```http
# ① サーバー -> ブラウザ
Set-Cookie: user_id=12345; path=/; HttpOnly

# ② 次回リクエストでブラウザ -> サーバー
Cookie: user_id=12345
```

このコードでは、サーバーが保存を指示した Cookie を、ブラウザが次回のリクエストで送り返しています。

## Action
- [ ] Cookie の属性ごとの役割を見比べて整理する
