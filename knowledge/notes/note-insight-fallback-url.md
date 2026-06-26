---
id: note-insight-fallback-url
title: "フォールバックURLとは？"
created: 2026-04-19
source: [[2026-04-19_insight_rails-and-tailwind-terms.md]]
quiz_fail_log: []
---

## Summary
- フォールバックURLは、本命の URL が使えないときに代わりに返す URL です。
- Rails 固有の機能名ではなく、実装上の考え方として使われる言葉です。
- `presence` や `||` と組み合わせると、代替 URL をシンプルに書けます。

## Tags
#rails #url #fallback

## Links
- [[note-insight-rails-presence-use-case]]
- [[note-insight-rails-presence]]

## Body
フォールバックURLは、「まず本命の URL を使い、なければ別の URL を返す」という代替先の考え方です。Rails の特別な機能名ではなく、アプリ側でどの URL を本命にし、どの URL を代わりに使うかを決めます。

画像や遷移先などが未設定の場合に、デフォルトの URL を返したいときに使うと整理しやすくなります。

## Example
```ruby
def avatar_url(user)
  user.avatar_url.presence || "/images/default-avatar.png"
end
```

このコードでは、ユーザーに設定済みの画像 URL がなければ、代わりにデフォルト画像の URL を返しています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
