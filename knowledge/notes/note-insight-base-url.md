---
id: note-insight-base-url
title: "baseURLはAxiosインスタンスでURLの共通部分をまとめる設定"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
quiz_fail_log: []
---

## Summary
- 毎回同じURLの前半部分を、省略して書けるようにする設定
- `baseURL` は、毎回同じドメインやURLの先頭部分を書く手間を減らすための設定です。
- インスタンスに設定しておくと、`/users` のような相対パスだけで通信できます。

## Tags
#javascript #http

## Links

## Body
`baseURL` を設定すると、`apiClient.get("/users")` のような相対パスが自動的に `https://api.example.com/users` に展開されます。
相対パスを使うときはスラッシュの有無に注意が必要で、`baseURL` がスラッシュで終わっているときに `/users` のような絶対相対パスを渡すと期待通りに連結されない場合があります。
環境ごとに `baseURL` を切り替えると（`process.env.API_BASE_URL` など）、開発・ステージング・本番で向き先を簡単に変えられます。

## Example

```js
const apiClient = axios.create({
  baseURL: "https://api.example.com"
});

apiClient.get("/users");
```

このコードでは、共通のURLを毎回書かなくて済むように `baseURL` を使っています。
