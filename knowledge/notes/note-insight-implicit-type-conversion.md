---
id: note-insight-implicit-type-conversion
title: 暗黙的な型変換は言語が自動的に型を変換すること
created: 2026-06-14
source: [[2026-06-14_insight_type-conversion-and-integer-division]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- 暗黙的な型変換はプログラマーが変換処理を書かなくても言語が自動で行う型変換です。
- 意図しない結果になる場合があるため、変換ルールを把握することが重要です。

## Tags
#programming #java #javascript #data-type

## Links
- [[note-insight-type-conversion]]
- [[note-insight-explicit-type-conversion]]
- [[note-insight-type-promotion]]
- [[note-insight-addition-operator]]

## Body
Javaでは `int` と `double` を一緒に計算すると `int` が自動で `double` へ変換されます。JavaScriptでは `"2" + 5` が `"25"` になるなど、意図しない連結が起きることがあります。言語ごとの自動変換ルールを理解しておくことがバグ防止につながります。

## Example
```java
double result = 2.0 * 5; // 5がdoubleへ自動変換
System.out.println(result); // 10.0
```
