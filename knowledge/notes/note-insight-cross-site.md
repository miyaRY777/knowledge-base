---
id: note-insight-cross-site
title: クロスサイトは別オリジンをまたぐ処理のこと
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
quiz_streak: 2
quiz_fail_log: []
---

## Summary
- クロスサイトとは、あるサイト（オリジン）から別のサイトに関係する処理が行われることです。
- XSS（クロスサイトスクリプティング）や CSRF（クロスサイトリクエストフォージェリ）の攻撃名に使われます。
- ブラウザの同一オリジンポリシーはクロスサイトのリスクを制限するための仕組みです。

## Tags
#security #web #xss #csrf

## Links
- [[note-insight-xss]]
- [[note-insight-htmlspecialchars-xss]]
- [[note-insight-internet-security]]

## Body
「クロスサイト」は `example.com` のページが `another-site.com` に関係する処理を行うように、オリジン（スキーム＋ホスト＋ポートの組み合わせ）をまたいだ処理を指します。XSSは攻撃者が別オリジンのスクリプトをページに注入する攻撃、CSRFはログイン中のサイトに別サイトから意図しないリクエストを送らせる攻撃です。どちらも「クロスサイト」という名前がつく理由は、攻撃の起点が別のサイトにあるためです。
