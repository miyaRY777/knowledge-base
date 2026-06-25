---
id: note-insight-return-value
title: 戻り値は関数の処理結果として呼び出し元に返される値
created: 2026-06-08
source: [[2026-06-08_insight_void-null-return-values]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- 戻り値は、関数やメソッドを実行したあとに呼び出し元へ渡す処理の結果です。
- 計算結果や取得データを次の処理で使いたいときに戻り値を返します。
- 返す値がない場合は `void` を指定し、戻り値なしであることを明示します。

## Tags
#java #typescript #return-value #void #programming

## Links
- [[note-insight-void]]
- [[note-insight-null-vs-void]]
- [[note-insight-output-data]]
- [[note-insight-input-process-output]]

## Body
戻り値は「関数に仕事をさせた結果、何を受け取るか」を決めるものです。足し算の結果や検索で見つかったデータなど、呼び出し元でその値を使いたい場合に戻り値として返します。Java では戻り値の型をメソッド宣言に書き、`return` で値を返します。処理するだけで結果を渡す必要がない場合は型を `void` にし、`return` も省略できます。

入力・処理・出力の観点から見ると、戻り値は「出力データを作成するプログラム」の仕組みです。処理の結果を呼び出し元に渡すことで、次の処理につなげられます。

## Example
```java
// 戻り値あり
public static int add(int a, int b) {
    return a + b;
}

// 戻り値なし
public static void printResult(int n) {
    System.out.println(n);
}
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
