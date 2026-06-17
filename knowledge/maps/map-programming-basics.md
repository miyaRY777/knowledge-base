# プログラミング基礎マップ

> **このMOCで分かること**: プログラムの基本概念・入力→処理→出力の流れ・URLの種類・JSオブジェクトの基礎を整理できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | プログラム | コンピュータへの命令の集まり | [[note-insight-program]] |
| 2 | 入力データ | プログラムが処理するために受け取るデータ | [[note-insight-input-data]] |
| 3 | 処理 | 入力データを使って計算・判定・保存などを行うこと | [[note-insight-processing]] |
| 4 | 出力データ | プログラムが処理した結果として返すデータ | [[note-insight-output-data]] |
| 5 | 入力・処理・出力 | プログラムの基本的な流れ | [[note-insight-input-process-output]] |
| 6 | 絶対URL | 通信方式からパスまで省略なく書くURL | [[note-insight-absolute-url]] |
| 7 | 相対URL | 現在の場所を基準に指定するURL | [[note-insight-relative-url]] |
| 8 | インターネット | 世界中の機器をつなぐ巨大ネットワーク | [[note-insight-internet]] |
| 9 | JSオブジェクト | データと機能をまとめたもの | [[note-insight-js-object]] |
| 10 | オブジェクトベース言語 | オブジェクトを中心に扱える言語 | [[note-insight-object-based-language]] |
| 11 | void演算子（JS） | 式を評価してundefinedを返す演算子 | [[note-insight-js-void-operator]] |
| 12 | Webの副作用 | サーバー側の状態を変える処理のこと | [[note-insight-side-effect-web]] |

---

## セクション1: プログラムの基本概念

[[note-insight-program]]
[[note-insight-input-data]]
[[note-insight-processing]]
[[note-insight-output-data]]
[[note-insight-input-process-output]]

**ポイント**:
- プログラムは「命令の集まり」。コンピュータは命令を順番に実行する
- どんなプログラムも「入力→処理→出力」の流れで考えられる
- 入力はユーザー操作・ファイル・APIなど。出力は画面表示・ファイル・レスポンスなど

---

## セクション2: URLの種類

[[note-insight-absolute-url]]
[[note-insight-relative-url]]
[[note-insight-internet]]

**ポイント**:
- 絶対URLは `https://example.com/path` のように完全な形
- 相対URLは `/path` や `../image.png` のように現在位置からの相対パス
- インターネットはTCP/IPで接続された世界規模のネットワーク

---

## セクション3: JavaScriptのオブジェクト

[[note-insight-js-object]]
[[note-insight-object-based-language]]
[[note-insight-js-void-operator]]

**ポイント**:
- JavaScriptはオブジェクトベース言語。関数・配列なども内部的にはオブジェクト
- `{ key: value }` の形でデータと機能をまとめられる
- `void 0` はundefinedを確実に返すために使う場面がある

---

## セクション4: Webの副作用

[[note-insight-side-effect-web]]

**ポイント**:
- GETリクエストは副作用なし（データ取得のみ）が原則
- POST / PUT / DELETE はサーバー状態を変える副作用あり
- 副作用のある操作はCSRF対策が必要

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| 絶対URLと相対URLをRailsのビューでどう使い分けるか | - | - | [[note-insight-relative-url]] |
| JavaScriptのオブジェクトとRubyのハッシュの違いをまとめる | - | - | [[note-insight-js-object]] |
| 副作用なしのGETリクエストに誤ってPOST処理を書いた場合のリスクは | - | - | [[note-insight-side-effect-web]] |

---

## 関連リンク

- [[map-network-basics]]
- [[map-http-client-basics]]
- [[map-html-and-dom-basics]]
- [[map-operator-and-expression-basics]]
- [[map-web-security-basics]]
