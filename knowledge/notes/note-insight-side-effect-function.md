---
id: note-insight-side-effect-function
title: 関数の副作用は戻り値以外で外部の状態を変える処理
created: 2026-06-08
source: [[2026-06-08_insight_void-null-return-values]]
quiz_streak: 1
---

## Summary
- 副作用とは、関数の実行によって画面表示・ファイル保存・DB更新など外部の状態が変わることです。
- `void` の関数は戻り値を返さず、副作用そのものを目的として使われることが多いです。
- Web文脈の副作用（HTTPリクエストによるDB変更）とは異なる、プログラミング全般の概念です。

## Tags
#programming #side-effect #void #function

## Links
- [[note-insight-void]]
- [[note-insight-side-effect-web]]

## Body
副作用はプログラミング全般の概念で、「関数が戻り値以外の形で外部の何かを変化させること」を指します。コンソールへの出力・ファイルへの書き込み・グローバル変数の書き換えなどが代表例です。`void` の関数は計算結果を返さない代わりに、この副作用を目的として動きます。Web開発で使われる「副作用」（POSTリクエストによるDB更新など）も同じ語源ですが、文脈が異なるため区別して理解しておくと混乱しにくくなります。

## Example
```js
function logMessage() {
  console.log("保存しました"); // 戻り値なし、コンソールへの出力が副作用
}
```
