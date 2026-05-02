---
id: note-insight-build-output
title: "ビルド出力は変換後にできる最終ファイル"
created: 2026-04-09
source: [[2026-04-09_insight-entry-point-css-entry-build-output-stimulus-classes]]
---

## Summary
- ビルド出力は、変換や結合のあとに生成される最終的なファイルです。
- 元ファイルを直接配信せず、ブラウザ向けに使いやすい形へ変えた結果がここに出ます。
- 通常は元ファイルを編集し、ビルド出力を直接触らないことが多いです。

## Tags
#frontend #build #output #asset

## Links
- [[note-insight-entry-point]]
- [[note-insight-css-entry]]

## Body
ビルド出力は、ソースコードや元のスタイル定義をそのまま使うのではなく、ブラウザ向けにまとめたり変換したりした結果として生成されるファイルです。開発では元ファイルを編集し、ビルドによって出力ファイルを作り直すのが基本です。そのため、出力先は「入口」ではなく「結果」の置き場として考えると整理しやすいです。

## Example
```bash
$ yarn build
# app/assets/builds/application.css が生成される
```

このコードでは、ビルドした結果としてブラウザで使うファイルを作るためにビルド出力を使っています。

## Action
- [ ] エントリーポイントとの違いを対比表で追加する
