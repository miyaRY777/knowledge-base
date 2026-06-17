---
id: note-insight-console
title: "コンソールはプログラムの実行結果やエラーを表示する画面"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 1
---

## Summary
- コンソールは、プログラムが出力したメッセージやエラーを表示する画面です。
- 開発中の動作確認やデバッグに使われます。
- JavaScript では `console.log()` でコンソールへ出力できます。

## Tags
#javascript #programming #debug

## Links
- [[note-insight-programming-data]]

## Body
コンソールは実行中のプログラムの出力先で、ブラウザでは開発者ツール（F12）、Node.jsではターミナルに表示されます。
`console.log` の他に、警告には `console.warn`、エラーには `console.error` があり、それぞれ色や表示形式が異なります。
本番環境では不要な `console.log` を残すと情報漏洩やパフォーマンス低下につながるため、デバッグ後は削除します。

## Example
```js
console.log("Hello World");
```

このコードでは、文字列をコンソールへ出力するために `console.log` を使っています。
