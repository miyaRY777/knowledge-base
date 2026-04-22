---
id: note-insight-session-termination
title: セッション終了の要点
created: 2026-04-22
source: [[2026-04-22_insight_session-flow-basics.md]]
---

## Summary
- **セッション終了とは、セッションに保存していた状態を使わなくして、ログイン状態などを破棄することです。**
- ログアウト時や一定時間操作がないときに、セッションの情報は削除またはリセットされます。
- セッションを適切に破棄しないと、意図せず以前のログイン状態が残る危険があります。

## Tags
#http #web #session #security

## Links
- [[note-insight-session]]
- [[note-insight-session-id]]
- [[note-insight-cookie-deletion]]

## Body
セッション終了は、サーバー側で保持していたユーザーごとの状態を無効化することです。
Web アプリでは、ログアウト時や一定時間の無操作後に、保存していたログイン情報や一時的な状態を破棄するために使われます。
これにより、次のアクセス時は以前の状態を引き継がず、新しいセッションとして扱えるようになります。
特にログアウト時にセッション情報を消さないままだと、意図せずログイン状態が残る危険があるため、明示的な破棄が重要です。

## Example
```ruby
reset_session
```

このコードでは、現在のセッション全体を破棄して、以前の状態を引き継がないようにしています。

```ruby
session.delete(:user_id)
```

このコードでは、ログイン状態を表す `user_id` だけをセッションから削除して、ログアウト状態にしています。

## Action
- [ ] `reset_session` と `session.delete` の使い分けを整理する
