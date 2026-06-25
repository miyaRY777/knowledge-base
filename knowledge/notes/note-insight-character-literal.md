---
id: note-insight-character-literal
title: 文字リテラルは1文字を表すリテラル
created: 2026-06-11
source: [[2026-06-11_insight_js-data-types-and-literals]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- 文字リテラルは `'a'` のように1文字を表す値です。
- Java・C++ には `char` 型として独立した文字リテラルがありますが、JavaScriptには `char` 型がなく、1文字でも `string` 型として扱われます。

## Tags
#javascript #programming

## Links
- [[note-insight-literal]]
- [[note-insight-char-type]]
- [[note-insight-string-literal]]
- [[note-insight-string-type]]

## Body
言語によって文字リテラルの扱いは異なります。JavaではシングルクォートでJava独自のchar型リテラル（`'a'`）を書きますが、JavaScriptではシングルクォートもダブルクォートもすべて文字列リテラルとして扱われます。

## Example
```js
console.log("a");
console.log(typeof "a"); // string（charではない）
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
