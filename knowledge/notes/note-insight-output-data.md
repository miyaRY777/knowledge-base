---
id: note-insight-output-data
title: 出力データはプログラムが処理した結果として返すデータ
created: 2026-06-09
source: [[2026-06-09_insight_program-input-process-output]]
---

## Summary
- 出力データは、プログラムが処理を終えたあとに作る結果です。
- 計算結果・検索結果・APIのレスポンスなどが該当します。
- すべてのプログラムが出力データを返すわけではありません。

## Tags
#programming #basics #output #java

## Links
- [[note-insight-processing]]
- [[note-insight-input-process-output]]
- [[note-insight-return-value]]
- [[note-insight-output-device]]

## Body
出力データは「プログラムが処理した結果として外に渡すもの」です。`3 + 5` の結果として `8` を返す、検索結果の一覧を画面に表示する、APIがJSONでユーザー情報を返すなどが典型例です。出力データがある場合はJavaでは戻り値の型を宣言して `return` で返します。一方、画面表示だけが目的の処理のように出力データが不要な場合は `void` を指定します。

## Example
```java
// 出力データあり（int を返す）
public static int add(int a, int b) {
    return a + b;
}

// 出力データなし（void）
public static void showMessage() {
    System.out.println("完了しました");
}
```
