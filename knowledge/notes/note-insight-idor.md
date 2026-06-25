---
id: note-insight-idor
title: "IDORはIDを直接指定することで他人のデータにアクセスできてしまう脆弱性"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
quiz_fail_log: []
---

## Summary
- **他人のデータに不正アクセスできてしまう脆弱性**
- IDを直接指定して他人のデータにアクセスできる状態のことです。
- 関連を使った取得や認可チェックで防ぎます。

## Tags
#security

## Links

## Body
IDOR（Insecure Direct Object Reference）は、URLやパラメータのIDを書き換えることで他人のリソースにアクセスできてしまう脆弱性です。
`Model.find(params[:id])` はテーブル全体を対象にするため、認可チェックなしに使うと攻撃者が任意のIDを指定して他人のデータを閲覧・操作できます。
防ぐには `current_user.resources.find(params[:id])` のように関連をたどってスコープを絞るか、Pundit などの認可ライブラリでアクセス制御を強制します。


## Example
```ruby
Room.find(params[:id]) # 認可なし
```

このコードでは、他人のデータにもアクセスできる可能性があり、IDORの原因になる書き方です。

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
