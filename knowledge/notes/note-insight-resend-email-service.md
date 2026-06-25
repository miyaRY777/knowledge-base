---
id: note-insight-resend-email-service
title: "ResendはWebアプリからメールを送る外部メールサービス"
created: 2026-05-04
source: [[2026-05-04_insight_rails-model-basics]]
review_streak: 0
last_reviewed_on: 2026-05-27
quiz_fail_log: []
---

## Summary
- Resend は Rails 標準機能ではなく、メール送信を任せる外部サービスです。
- 確認メール、招待メール、パスワード再設定メールなどの送信に使えます。
- アプリ側はメールを作り、実際の配信は外部サービスに任せる形になります。

## Tags
#email #web-service #rails #operations

## Links
- [[note-insight-on-premise]]

## Body
Resend は、Web アプリからユーザーや管理者へメールを送るための外部メールサービスです。Rails の標準機能名ではなく、メール配信の部分を外部サービスとして利用する選択肢のひとつです。

ユーザー登録後の確認メール、パスワード再設定メール、プロジェクト招待メール、問い合わせ通知のように、アプリの処理をきっかけに送るメールで関係します。Rails 側ではメールの内容や送信タイミングを扱い、実際の配信は Resend のようなサービスに任せます。

## Example
- ユーザー登録後に確認メールを送る
- パスワード再設定メールを送る
- プロジェクト招待メールを送る
- お問い合わせ内容を管理者へ送る


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] Rails の Action Mailer と外部メールサービスの関係を整理する
