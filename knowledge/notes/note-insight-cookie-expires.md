---
id: note-insight-cookie-expires
title: "expires属性はCookieの有効期限を指定する属性"
created: 2026-04-17
source: [[2026-04-17_insight_rails-cookies-headers-and-attributes.md]]
quiz_fail_log: []
---

## Summary
- **`expires` は、Cookie の有効期限を指定する属性です。**
- 指定した日時までブラウザに Cookie を保存できます。
- 指定しない場合は、ブラウザを閉じると消える扱いになることがあります。

## Tags
#http #web #cookie

## Links
- [[note-insight-set-cookie-header]]
- [[note-insight-cookie]]

## Body
`expires` 属性は、Cookie をいつまで保持するかを指定するための設定です。
サーバーが `Set-Cookie` と一緒に期限を返すことで、ブラウザはその日時まで Cookie を保存します。
有効期限のある Cookie は、ログイン状態を一定期間維持したいときなどに使われます。

## Example
```http
Set-Cookie: session_id=abc123; expires=Wed, 21 Oct 2026 07:28:00 GMT
```

このコードでは、指定された日時まで `session_id` の Cookie を保持します。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
