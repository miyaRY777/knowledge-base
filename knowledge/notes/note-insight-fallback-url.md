---
id: note-insight-fallback-url
title: フォールバックURLは使えないときの代替URL
created: 2026-04-19
source: [[2026-04-19_insight_rails-and-tailwind-terms.md]]
---

## Summary
- フォールバックURLは、優先したい URL が使えないときに代わりに返す URL です。
- Rails 固有の機能名ではなく、実装上の考え方として使われる言葉です。
- `presence` や `||` と組み合わせると、代替 URL をシンプルに書けます。

## Tags
#rails #url #fallback

## Links
- [[note-insight-rails-presence-use-case]]
- [[note-insight-rails-presence]]

## Body
フォールバックURLは、「まず本命の URL を使い、なければ別の URL を返す」という考え方を表します。Rails に専用の機能があるわけではなく、アプリ側でどれを本命にしてどれを代替にするかを決めて使います。

## Example
```ruby
def avatar_url(user)
  user.avatar_url.presence || "/images/default-avatar.png"
end
```

このコードでは、ユーザーに設定済みの画像 URL がなければ、代わりにデフォルト画像の URL を返しています。

## Action
- [ ] `default_url_options` との違いを後で確認する
