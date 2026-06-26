---
id: note-insight-securerandom-urlsafe-base64
title: "SecureRandom.urlsafe_base64はURLで使えるランダム文字列を生成するメソッド"
created: 2026-04-07
source: [[2026-04-07_insight_rails-ruby-terms.md]]
quiz_fail_log: []
---

## Summary
- `SecureRandom.urlsafe_base64(16)` は URL に使いやすいランダム文字列を作ります。
- 推測されにくいトークンや招待 URL に向いています。
- 毎回異なる値が生成されるため、安全性を高めやすいです。

## Tags
#ruby #security #token

## Links

## Body
`SecureRandom.urlsafe_base64(16)` は、URL に使いやすく、推測されにくいランダム文字列を作るメソッドです。トークンや招待リンクのように、他人に当てられたくない値を作る場面でよく使います。

固定文字列ではなく毎回異なる値が生成されるため、公開 URL や一時的な識別子に使うと安全性を高めやすくなります。

## Example
```ruby
token = SecureRandom.urlsafe_base64(16)
```

このコードでは、招待リンクなどに使える、推測されにくいランダムなトークンを生成しています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
