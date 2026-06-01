---
id: note-insight-boolean-type
title: "ブーリアン型は真（true）か偽（false）を表すデータ型"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
---

## Summary
- ブーリアン型（Boolean型）は、true か false の2値だけを持つデータ型です。
- 条件分岐やフラグ管理でよく使われます。
- 言語によって `bool`、`boolean`、`Boolean` などと書きます。

## Tags
#programming #data-type

## Links
- [[note-insight-boolean-default-false-null-false]]
- [[note-insight-programming-data]]

## Body
ブーリアン型は、条件が成立するか（true）しないか（false）を表すためのデータ型です。プログラムの分岐処理やフラグの管理に使われます。Rails のマイグレーションでの `boolean` 型とは別に、プログラミング一般の概念として理解しておくことが重要です。

## Example
```js
const isAdmin = true;
const isLoggedIn = false;

if (isAdmin) {
  console.log("管理者です");
}
```

このコードでは、管理者かどうかを `true / false` で表すためにブーリアン型を使っています。
