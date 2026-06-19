---
id: note-insight-301-moved-permanently
title: "301 Moved Permanentlyは恒久的なURL移動を表す"
created: 2026-05-07
source: [[2026-05-07_insight_http-status-codes]]
review_streak: 0
last_reviewed_on: 2026-05-25
quiz_fail_log: []
---

## Summary
- `301 Moved Permanently` は、リソースが恒久的に別のURLへ移動したことを表します。
- ブラウザや検索エンジンは、新しいURLへリダイレクトされるものとして扱います。
- 古いURLを今後も新しいURLへ案内したい場面で使われます。

## Tags
#http #web #status-code #redirect

## Links
- [[note-insight-http-status-code]]
- [[note-insight-fallback-url]]

## Body
`301 Moved Permanently` は、リクエストされたリソースが今後も別のURLに移動したことを伝えるHTTPステータスコードです。一時的な移動ではなく、恒久的な移動として扱われます。

古いURLにアクセスしたユーザーを新しいURLへ自動で移動させたい場合に使います。検索エンジンにも「今後はこちらのURLを正として扱ってよい」という意味が伝わるため、URL変更時には意味を理解して使う必要があります。

## Example
- 古いURL: `/old-profile`
- 新しいURL: `/profile`
- 古いURLへアクセスすると、新しいURLへ自動で移動する

## Action
- [ ] `302 Found` など一時的なリダイレクトとの違いを整理する
