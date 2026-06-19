---
id: note-insight-string-type
title: 文字列型は複数の文字をまとめて扱うデータ型
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- 文字列型は、名前・文章・メールアドレスなど文字の並びを扱うためのデータ型です。
- 言語によって型名が異なり、JavaScriptは `string`、Rubyは `String`、Pythonは `str` と書きます。
- 数値のように計算するのではなく、文字データとして扱う点が整数型との違いです。

## Tags
#programming #data-type #javascript #ruby

## Links
- [[note-insight-char-type]]
- [[note-insight-empty-string]]
- [[note-insight-integer-vs-string]]

## Body
文字列型は文字の並びをひとまとまりとして扱う型です。`"Taro"` や `"hello@example.com"` のようにダブルクォートやシングルクォートで囲んで表現します。整数型と見た目が同じ `"1"` でも、文字列型では `"1" + "2"` が `"12"` になるなど、演算の挙動が変わります。JavaScriptでは `string`、Rubyでは `String`、Pythonでは `str` と言語によって型名の表記が異なります。

## Example
```js
const name = "Taro";
console.log(name.length); // 4
```

```python
message = "hello"
print(type(message))  # <class 'str'>
```
