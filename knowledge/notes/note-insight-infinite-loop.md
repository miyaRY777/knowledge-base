---
id: note-insight-infinite-loop
title: "無限ループは終了条件がなく処理がずっと続いてしまう状態"
created: 2026-04-07
source: [[2026-04-07_insight_knowledge-base.md]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- **終わる条件がなく、処理がずっと続いてしまう状態**
- ループの条件がずっと `true` のままだと、処理が止まらなくなります。`for (;;)` や、条件や増減式の書き間違いで起こることがあります。止まる条件を必ず確認するのが大切です。 ([MDNのウェブドキュメント](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration "Loops and iteration - JavaScript | MDN"))
- let i = 0;

## Tags
#javascript #loop

## Links

## Body
無限ループは、条件式が常に `true` になること（`while (true)` の書き間違い、増減式の忘れなど）で発生します。
意図的に使う場合（ゲームループ・ポーリングなど）は `break` で抜ける出口を用意しますが、バグによる無限ループはタブをフリーズさせたりプロセスを占有します。
`for` ループでよくあるミスは、減算すべき変数を `i++` と書いてしまうケースです。

## Example

```js
let i = 0;

while (true) {
  console.log(i);
  i++;
}
```

このコードでは、条件が常に `true` なので、処理が終わらない無限ループになります。

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
