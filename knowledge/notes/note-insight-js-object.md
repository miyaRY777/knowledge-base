---
id: note-insight-js-object
title: JavaScriptのオブジェクトはデータと機能をまとめたもの
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
---

## Summary
- JavaScriptのオブジェクトは、関連するデータをキーと値のペアで一まとまりに表現します。
- `{}` の中にプロパティを列挙し、ドット記法でアクセスできます。
- 配列・関数・日付もオブジェクトとして扱われるのがJavaScriptの特徴です。

## Tags
#javascript #programming #data-type

## Links
- [[note-insight-object-based-language]]
- [[note-insight-object-oriented-programming]]
- [[note-insight-dom-tree]]

## Body
JavaScriptのオブジェクトは `{ name: "Taro", age: 20 }` のように書き、複数の情報をひとまとまりにして扱います。プロパティへは `user.name` のようにドット記法でアクセスできます。JavaScriptではプリミティブ値（数値・文字列・booleanなど）以外はすべてオブジェクトとして扱われるため、配列や関数もオブジェクトの一種です。この性質がJavaScriptを「オブジェクトベースの言語」と呼ぶ理由のひとつです。

## Example
```js
const user = {
  name: "Taro",
  age: 20
};
console.log(user.name); // "Taro"
```
