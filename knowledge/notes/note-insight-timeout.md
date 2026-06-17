---
id: note-insight-timeout
title: "timeoutはHTTPリクエストが完了するまでの最大待ち時間をミリ秒で指定する設定"
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
`timeout` に指定した時間（ミリ秒）を超えてもレスポンスが返ってこなければ、Axios はリクエストをキャンセルして `AxiosError`（`code: "ECONNABORTED"`）を投げます。
設定しないとサーバーが応答しない場合に無限に待ち続けるため、UX やリソースの観点から実務では必ず設定するのが推奨されます。
一般的な目安は通常のAPIで3000〜10000ms、ファイルアップロードなど時間のかかる処理ではそれ以上に設定します。

## Example

```js
const apiClient = axios.create({
  timeout: 5000
});
```

このコードでは、5秒以上応答がない通信を打ち切るために `timeout` を使っています。
