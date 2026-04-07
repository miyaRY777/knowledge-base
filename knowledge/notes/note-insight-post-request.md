---
id: note-insight-post-request
title: POSTリクエストの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **サーバーに新しいデータを送るときのリクエストのこと**
- `POSTリクエスト` は、新規作成したいデータをサーバーに送るときによく使います。
- フォーム送信や新規登録の処理でよく登場します。

## Tags
#javascript

## Links
- [[関連ノート]]

## Body
**サーバーに新しいデータを送るときのリクエストのこと**

**解説：**
`POSTリクエスト` は、新規作成したいデータをサーバーに送るときによく使います。
フォーム送信や新規登録の処理でよく登場します。
Axiosでは、送信したいデータを第2引数に渡せます。

## Example

```js
axios.post("/posts", {
  title: "New Post",
  body: "Hello"
});
```

このコードでは、新しい投稿データを作成するために `POSTリクエスト` を使っています。
