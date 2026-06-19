---
id: note-insight-processing
title: 処理は入力データを使って計算・判定・保存などを行うこと
created: 2026-06-09
source: [[2026-06-09_insight_program-input-process-output]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- 処理は、プログラムが実際に行う作業のことです。
- 計算・条件判定・データベースへの保存・並び替えなど多様な作業を指します。
- 特定技術に限らず、プログラム全般で使われる一般的な概念です。

## Tags
#programming #basics #processing

## Links
- [[note-insight-input-data]]
- [[note-insight-output-data]]
- [[note-insight-input-process-output]]

## Body
処理は「入力データを受け取って何かをすること」です。足し算・パスワード照合・DB保存・一覧の並び替えなど、プログラムが行うあらゆる作業が処理にあたります。処理の内容によって戻り値（出力データ）を返す場合と返さない場合があり、返す場合は戻り値の型を、返さない場合は `void` を指定します。

## Example
```java
// 計算する処理
public static int add(int a, int b) {
    return a + b;
}

// 表示するだけの処理（出力データなし）
public static void printResult(int n) {
    System.out.println(n);
}
```
