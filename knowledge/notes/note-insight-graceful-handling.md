---
id: note-insight-graceful-handling
title: "graceful に処理するの要点"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **エラーで落とさずユーザーに優しく処理すること**
- 例外でアプリを止めるのではなく、メッセージ表示やリダイレクトで対応します。
- ユーザー体験を守るために重要です。

## Tags
#insight

## Links

## Body
**エラーで落とさずユーザーに優しく処理すること**

**解説：**
例外でアプリを止めるのではなく、メッセージ表示やリダイレクトで対応します。
ユーザー体験を守るために重要です。


## Example
```ruby
redirect_to root_path, alert: "見つかりませんでした"
```

このコードでは、エラーで落とさずユーザーにメッセージを表示するためにリダイレクトしています。
