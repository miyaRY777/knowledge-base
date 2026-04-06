---
id: note-insight-headers
title: headersの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **リクエストやレスポンスに付ける追加情報**
- `headers` は、通信時に一緒に送るメタ情報です。
- たとえば「JSONを送ります」「認証トークンがあります」といった情報をここに入れます。

## Tags
#javascript #http

## Links
- [[関連ノート]]

## Body
**リクエストやレスポンスに付ける追加情報**

**解説：**
`headers` は、通信時に一緒に送るメタ情報です。
たとえば「JSONを送ります」「認証トークンがあります」といった情報をここに入れます。
APIによって必要なヘッダーは変わるので、仕様確認が大切です。

具体例：

```js
const apiClient = axios.create({
  headers: {
    Authorization: "Bearer sample-token"
  }
});
```

このコードでは、認証情報をリクエストに含めるために `headers` を使っています。
