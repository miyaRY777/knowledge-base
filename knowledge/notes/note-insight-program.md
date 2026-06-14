---
id: note-insight-program
title: プログラムはコンピュータへの命令の集まり
created: 2026-06-09
source: [[2026-06-09_insight_program-input-process-output]]
quiz_streak: 1
---

## Summary
- プログラムは、コンピュータに「何をしてほしいか」を伝えるための命令の集まりです。
- 計算・文字表示・データ保存など、目的に合わせて命令を書きます。
- 多くのプログラムは入力を受け取り、処理して、必要に応じて出力を作ります。

## Tags
#programming #basics #java

## Links
- [[note-insight-input-data]]
- [[note-insight-input-process-output]]
- [[note-insight-programming-data]]

## Body
プログラムは、コンピュータに特定の作業をさせるための手順書です。人間が日本語で「3と5を足して結果を教えて」と頼む代わりに、コンピュータが理解できる言語（JavaやTypeScriptなど）で命令を書きます。単純な計算から、フォーム入力の保存、画像の表示まで、コンピュータが行う作業はすべてプログラムとして記述されています。

## Example
```java
public static void main(String[] args) {
    int result = 3 + 5;
    System.out.println(result); // 8
}
```
