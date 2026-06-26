---
id: note-insight-stateless
title: "ステートレスは前のリクエストの状態を自動では覚えないHTTPの性質"
created: 2026-04-17
source: [[2026-04-17_insight_cookie-http-stateless.md]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- **ステートレスとは、前の状態を自動では覚えない性質のことです。**
- HTTP は各リクエストが独立しているため、前回ログインした情報はそのままでは引き継がれません。
- Cookie やセッションは、この性質を補うために使われます。

## Tags
#http #web

## Links
- [[note-insight-cookie]]
- [[note-insight-cookie-purpose]]
- [[note-insight-session]]
- [[note-insight-http-request]]

## Body
ステートレスとは、通信や処理のたびに前回の状態を保持しない考え方です。
HTTP では 1 回 1 回のリクエストが独立して扱われるため、あるリクエストでログインに成功しても、次のリクエストでその事実を自動的に覚えているわけではありません。
この性質のおかげで通信の仕組みは単純になりますが、そのままではログイン維持やカート保持ができません。
そこで Web アプリでは Cookie やセッションを組み合わせて、必要な状態だけを継続できるようにします。

## Example
```text
1回目のリクエスト -> ログイン
2回目のリクエスト -> ログイン状態は自動では保持されない
```

この例では、HTTP が前回の状態をそのまま覚えないことを表しています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
