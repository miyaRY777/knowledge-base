---
id: note-insight-null-vs-void
title: nullは「値がない」、voidは「戻り値がない」
created: 2026-06-08
source: [[2026-06-08_insight_void-null-return-values]]
quiz_streak: 1
---

## Summary
- `null` は変数に値が入っていない状態を表し、値として扱われることがあります。
- `void` は関数が結果の値を返さないことを表し、値ではなく「不在の宣言」です。
- 混同しやすいですが、指している対象が「変数の状態」と「関数の振る舞い」で異なります。

## Tags
#java #javascript #null #void #programming

## Links
- [[note-insight-null-value]]
- [[note-insight-void]]
- [[note-insight-return-value]]

## Body
`null` と `void` はどちらも「何もない」イメージを持ちやすいですが、指している対象がまったく異なります。`null` は変数やフィールドに「値が存在しない」状態を入れるためのもので、それ自体が一種の値として扱われます。一方 `void` は、関数やメソッドの設計として「返す値そのものがない」ことを宣言するためのキーワードです。「値の不在」と「戻り値の不在」を区別して理解することが重要です。

## Example
```java
String name = null;        // null: 値が入っていない状態
public static void log() { // void: 戻り値を返さない関数
    System.out.println("done");
}
```
