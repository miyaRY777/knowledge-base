---
id: note-insight-session-timeout
title: "セッションタイムアウトは無操作時にセッションを終了する考え方"
created: 2026-04-25
source: [[2026-04-25_insight_cookie-session-security-basics.md]]
quiz_fail_log: []
---

## Summary
- セッションタイムアウトは、一定時間操作がないとセッションを無効化する考え方。
- 放置されたログイン状態や盗まれたセッションの悪用リスクを下げる。
- Rails 固有機能名ではなく、何分で切るかや判定方法はアプリ実装で決まる。

## Tags
#http #web #session #security

## Links
- [[note-insight-session]]
- [[note-insight-session-id]]

## Body
セッションタイムアウトは、長時間操作のないセッションをそのまま有効にし続けないための考え方です。一定時間リクエストがなければセッションを切ることで、放置端末や盗まれたセッションが長く使われる危険を減らせます。これは Rails の特別な機能名ではなく、どこで最終アクセス時刻を記録し、何分で無効化するかはアプリ側の設計で決まります。無操作タイムアウトだけでなく、一定時間経過で必ず切る考え方も合わせて押さえると整理しやすいです。

## Example
```ruby
if session[:last_seen_at] && session[:last_seen_at] < 30.minutes.ago
  reset_session
end
session[:last_seen_at] = Time.current
```

このコードでは、一定時間アクセスがなければセッションを破棄して、再ログインを必要にしています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] idle timeout と absolute timeout の違いも整理する
