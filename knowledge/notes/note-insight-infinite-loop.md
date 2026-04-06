---
id: note-insight-infinite-loop
title: 無限ループの要点
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
---

## Summary（3行）
- **終わる条件がなく、処理がずっと続いてしまう状態**
- ループの条件がずっと `true` のままだと、処理が止まらなくなります。`for (;;)` や、条件や増減式の書き間違いで起こることがあります。止まる条件を必ず確認するのが大切です。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration "Loops and iteration - JavaScript | MDN"))
- let i = 0;

## Tags
#javascript #http

## Links
- [[関連ノート]]

## Body
**終わる条件がなく、処理がずっと続いてしまう状態**

**解説：**
ループの条件がずっと `true` のままだと、処理が止まらなくなります。`for (;;)` や、条件や増減式の書き間違いで起こることがあります。止まる条件を必ず確認するのが大切です。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration "Loops and iteration - JavaScript | MDN"))

具体例：

```js
let i = 0;

while (true) {
  console.log(i);
  i++;
}
```

このコードでは、条件が常に `true` なので、処理が終わらない無限ループになります。
