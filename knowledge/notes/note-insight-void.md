---
id: note-insight-void
title: voidは「返す値がない」を表す型・キーワード
created: 2026-06-08
source: [[2026-06-08_insight_void-null-return-values]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- `void` は、関数やメソッドが結果の値を返さないことを示す型・キーワードです。
- Java ではメソッドの戻り値の型として、TypeScript では関数の返り値の型として使います。
- `null`（値がない）とは異なり、「そもそも返す値が存在しない」ことを表します。

## Tags
#java #typescript #void #return-value #programming

## Links
- [[note-insight-return-value]]
- [[note-insight-null-vs-void]]
- [[note-insight-side-effect-function]]
- [[note-insight-output-data]]
- [[note-insight-input-process-output]]

## Body
`void` は、関数やメソッドが「処理は行うが、結果として値を返さない」ことを宣言するためのキーワードです。Java では戻り値の型として `void` を書くことで、呼び出し元に値を渡さないことを明示します。TypeScript でも同様に、関数の返り値の型注釈に使われます。値を返さない関数は、画面表示・ログ出力・ファイル保存など、処理そのものが目的である場合に使います。

入力・処理・出力の観点から見ると、`void` の関数は「出力データを作成しないプログラム」です。処理を実行すること自体が目的であり、呼び出し元に結果を渡す必要がない場合に使います。

## Example
```java
// Java: 値を返さないメソッド
public static void sayHello() {
    System.out.println("Hello World");
}
```

```ts
// TypeScript: 値を返さない関数
function showMessage(): void {
  console.log("Hello World");
}
```

## 言語化

結論：
理由：
具体例：
結論（まとめ）：
