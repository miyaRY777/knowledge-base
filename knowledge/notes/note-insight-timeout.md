---
id: note-insight-timeout
title: "リクエストのtimeoutの要点"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- **通信をどれくらい待つか決める設定のこと**
- `timeout` は、リクエストが終わるまでの待ち時間をミリ秒で指定する設定です。
- 時間内に応答が返らないと、エラーとして扱われます。

## Tags
#javascript #http

## Links

## Body
**通信をどれくらい待つか決める設定のこと**

**解説：**
`timeout` は、リクエストが終わるまでの待ち時間をミリ秒で指定する設定です。
時間内に応答が返らないと、エラーとして扱われます。
通信が止まり続けるのを防ぎたいときに便利です。

## Example

```js
const apiClient = axios.create({
  timeout: 5000
});
```

このコードでは、5秒以上応答がない通信を打ち切るために `timeout` を使っています。
