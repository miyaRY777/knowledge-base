---
id: note-insight-boolean-literal
title: 論理値リテラルはtrueまたはfalseを直接書いた値
created: 2026-06-11
source: [[2026-06-11_insight_js-data-types-and-literals]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- 論理値リテラルは、真偽を表す `true` と `false` をコードに直接書いた値です。
- `"true"` のようにクォートで囲むと文字列になり、論理値ではなくなります。

## Tags
#javascript #programming

## Links
- [[note-insight-literal]]
- [[note-insight-boolean-type]]
- [[note-insight-false-value]]

## Body
`true` と `false` はキーワードとして予約されており、クォートなしで書くと論理値リテラルになります。条件分岐やフラグ管理でよく使われます。`typeof true` は `"boolean"` を返します。

## Example
```js
console.log(true);
console.log(false);
console.log(typeof true);    // boolean
console.log(typeof "true");  // string（論理値ではない）
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
