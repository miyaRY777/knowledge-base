---
id: note-insight-base-url
title: "baseURLの要点"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary
- 毎回同じURLの前半部分を、省略して書けるようにする設定
- `baseURL` は、毎回同じドメインやURLの先頭部分を書く手間を減らすための設定です。
- インスタンスに設定しておくと、`/users` のような相対パスだけで通信できます。

## Tags
#javascript #http

## Links

## Body
毎回同じURLの前半部分を、省略して書けるようにする設定

**解説：**
`baseURL` は、毎回同じドメインやURLの先頭部分を書く手間を減らすための設定です。
インスタンスに設定しておくと、`/users` のような相対パスだけで通信できます。
絶対URLを指定した場合は、そちらが優先されます。

## Example

```js
const apiClient = axios.create({
  baseURL: "https://api.example.com"
});

apiClient.get("/users");
```

このコードでは、共通のURLを毎回書かなくて済むように `baseURL` を使っています。
