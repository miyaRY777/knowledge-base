---
id: note-insight-input-data
title: 入力データはプログラムが処理するために受け取るデータ
created: 2026-06-09
source: [[2026-06-09_insight_program-input-process-output]]
---

## Summary
- 入力データは、プログラムが処理を始めるための材料です。
- ユーザーが入力した文字・数値・ファイル・フォームの内容などが該当します。
- 入力データがあることで、プログラムはそれをもとに計算や判定を行えます。

## Tags
#programming #basics #input #java

## Links
- [[note-insight-program]]
- [[note-insight-input-process-output]]
- [[note-insight-input-device]]

## Body
入力データは「プログラムに渡す材料」です。足し算プログラムなら `3` と `5`、ログイン画面ならメールアドレスとパスワードがそれにあたります。ハードウェアの入力装置（キーボードなど）からデータが届く場合もあれば、別のプログラムやAPIから渡される場合もあります。入力データが何かを意識することで、プログラムの役割が整理しやすくなります。

## Example
```java
public static int add(int a, int b) { // a, b が入力データ
    return a + b;
}
```
