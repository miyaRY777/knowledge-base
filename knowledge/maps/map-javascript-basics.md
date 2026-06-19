---
title: JavaScript基礎マップ
created: 2026-06-20
tags:
  - javascript
---

# JavaScript基礎マップ

> **このMOCで分かること**: JavaScriptのデータ・型・DOM操作・非同期通信・関数の基本を体系的に整理できる（ループ・null系は別MOCに任せる）

---

## ノート一覧

| # | 概念 | 一言メモ | ノート |
|---|------|---------|--------|
| 1 | Number型 | 整数も小数も同じnumber型 | [[note-insight-javascript-number-type]] |
| 2 | number型の統一 | 2と2.0はどちらもnumber | [[note-insight-js-number-type-unified]] |
| 3 | JS除算 | 整数同士でも小数を含む結果 | [[note-insight-js-division]] |
| 4 | NaN | 数値として表せないときに返る特別な値 | [[note-insight-nan]] |
| 5 | Infinity | 正の無限大を表すnumber型の値 | [[note-insight-infinity]] |
| 6 | -Infinity | 負の無限大を表すnumber型の値 | [[note-insight-negative-infinity]] |
| 7 | Number.MAX_VALUE | number型で表現できる最大の有限値 | [[note-insight-number-max-value]] |
| 8 | Number.MIN_VALUE | 0より大きい最小の正の値 | [[note-insight-number-min-value]] |
| 9 | typeof演算子 | 値のデータ型を文字列で返す | [[note-insight-typeof]] |
| 10 | オブジェクト | データと機能をまとめたもの | [[note-insight-js-object]] |
| 11 | オブジェクトベース言語 | すべてがオブジェクトとして扱われる言語 | [[note-insight-object-based-language]] |
| 12 | 関数・メソッド・引数 | 処理をまとめて再利用できる仕組み | [[note-insight-function-method-argument-basics]] |
| 13 | 戻り値 | 関数の処理結果として返される値 | [[note-insight-return-value]] |
| 14 | 副作用（関数） | 戻り値以外で外部の状態を変える処理 | [[note-insight-side-effect-function]] |
| 15 | void演算子 | 式を評価してundefinedを返す | [[note-insight-js-void-operator]] |
| 16 | コンソール | 実行結果やエラーを表示する画面 | [[note-insight-console]] |
| 17 | Promise | 非同期処理の結果をあとから受け取る仕組み | [[note-insight-promise]] |
| 18 | Fetch API | ブラウザ標準のHTTPリクエスト機能 | [[note-insight-fetch-api]] |
| 19 | Axios | HTTPリクエストを簡単に送るライブラリ | [[note-insight-axios]] |
| 20 | Axiosインスタンス | 共通設定をまとめたカスタムAxiosオブジェクト | [[note-insight-axios-instance]] |
| 21 | timeout | リクエストの最大待ち時間設定 | [[note-insight-timeout]] |
| 22 | JSONPlaceholder | HTTP通信を練習できるモックAPIサービス | [[note-insight-jsonplaceholder]] |
| 23 | DOM操作 classList | HTML要素のclassを操作するAPI | [[note-insight-classlist-and-hidden]] |
| 24 | dataset | data属性をJSから読む仕組み | [[note-insight-dataset-and-data-attributes]] |
| 25 | event.currentTarget | イベントリスナーが設定された要素を指すプロパティ | [[note-insight-event-and-current-target]] |

---

## セクション1: Number型の特性

[[note-insight-javascript-number-type]]
[[note-insight-js-number-type-unified]]
[[note-insight-js-division]]

**ポイント**:
- JavaScriptにはintやfloatの区別がなく、すべての数値は`number`型（IEEE 754の64bit浮動小数点数）
- `2 / 5` は `0.4` を返す（Javaでは `0` になる点と対照的）
- 整数として安全に扱える範囲は `Number.MAX_SAFE_INTEGER` で確認できる

---

## セクション2: 特殊な数値

[[note-insight-nan]]
[[note-insight-infinity]]
[[note-insight-negative-infinity]]
[[note-insight-number-max-value]]
[[note-insight-number-min-value]]

**ポイント**:
- `NaN` は `number` 型だが自分自身と等しくない（`NaN === NaN` が `false`）—判定には `Number.isNaN()` を使う
- `Infinity` / `-Infinity` はエラーではなく正常な `number` 型の値
- `Number.MIN_VALUE` は「最小の負の数」ではなく「0に最も近い正の数」—名前に注意

---

## セクション3: 型の確認

[[note-insight-typeof]]
[[note-insight-object-based-language]]
[[note-insight-js-object]]

**ポイント**:
- `typeof` でデータ型を文字列として取得できるが、`typeof null` が `"object"` を返す落とし穴がある
- JavaScriptでは配列・関数・日付もすべてオブジェクトとして扱われる
- `{}` の中にプロパティを列挙し、ドット記法でアクセスできる

---

## セクション4: 関数と副作用

[[note-insight-function-method-argument-basics]]
[[note-insight-return-value]]
[[note-insight-side-effect-function]]
[[note-insight-js-void-operator]]
[[note-insight-console]]

**ポイント**:
- 関数は処理をまとめて再利用できる仕組み、メソッドはオブジェクトに属する関数
- 副作用とは、関数の実行で画面・ファイル・DBなど外部の状態が変わること
- `void` 演算子はJavaScriptで式を評価してundefinedを返す（言語の型キーワードvoidとは別）
- `console.log()` はデバッグの基本ツール

---

## セクション5: 非同期通信

[[note-insight-promise]]
[[note-insight-fetch-api]]
[[note-insight-axios]]
[[note-insight-axios-instance]]
[[note-insight-timeout]]
[[note-insight-jsonplaceholder]]

**ポイント**:
- `Promise` は非同期処理の結果を後から受け取るための仕組み
- `Fetch API` はインストール不要のブラウザ標準の通信機能—レスポンスは `.json()` で取り出す
- `Axios` は `Fetch API` より使いやすく、共通設定を `Axiosインスタンス` としてまとめられる
- `timeout` を設定しないと応答待ちが永続する可能性がある
- `JSONPlaceholder` はAPIの動作を試すためのモックサービス

---

## セクション6: DOM操作

[[note-insight-classlist-and-hidden]]
[[note-insight-dataset-and-data-attributes]]
[[note-insight-event-and-current-target]]

**ポイント**:
- `classList.toggle("hidden")` で表示・非表示を簡単に切り替えられる
- `dataset` は `data-*` 属性をJavaScriptから読む仕組み—値は文字列として返る
- `event.currentTarget` はイベントハンドラーが設定された要素を指す

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| Fetch APIとAxiosの使い分け基準は何か | - | - | [[note-insight-axios]] |
| Promise, async/awaitの違いをまとめる | - | - | [[note-insight-promise]] |
| `typeof` 以外の型判定方法は何があるか | - | - | [[note-insight-typeof]] |

---

## 関連MOC

- [[map-javascript-loop-basics]] — forループ・配列処理
- [[map-null-and-falsy-basics]] — null・undefined・falsy値
- [[map-type-and-literal-basics]] — データ型とリテラル
- [[map-type-conversion-basics]] — 型変換
- [[map-operator-and-expression-basics]] — 演算子と式
- [[map-stimulus-basics]] — StimulusによるDOM操作
- [[map-http-client-basics]] — HTTP通信の詳細
