# HTML・DOM基礎マップ

> **このMOCで分かること**: HTML要素の種類・属性・フォームの構造とDOMツリーの概念を整理できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | HTML属性 | 要素に追加設定を与える `属性名="値"` の形 | [[note-insight-html-attribute]] |
| 2 | class属性 | 要素に目印をつける属性 | [[note-insight-html-class-attribute]] |
| 3 | ブロックレベル要素 | 横幅いっぱいを使い前後で改行される要素 | [[note-insight-block-level-element]] |
| 4 | インライン要素 | 文章の一部として横に並ぶ要素 | [[note-insight-inline-element]] |
| 5 | span要素 | 文章の一部を囲む汎用インライン要素 | [[note-insight-span-element]] |
| 6 | DOMツリー | HTMLを木構造として表現したもの | [[note-insight-dom-tree]] |
| 7 | form要素 | ユーザー入力をサーバーに送信するHTML要素 | [[note-insight-html-form]] |
| 8 | label要素 | フォーム部品に説明文をつけるHTML要素 | [[note-insight-html-label]] |
| 9 | action属性 | フォームの送信先URLを指定する | [[note-insight-form-action-attribute]] |
| 10 | method属性 | フォーム送信のHTTPメソッドを指定する | [[note-insight-form-method-attribute]] |
| 11 | CSSの基本構文 | `プロパティ:値` で見た目の設定を書く | [[note-insight-css-property-value]] |

---

## セクション1: 要素の種類と構造

[[note-insight-html-attribute]]
[[note-insight-html-class-attribute]]
[[note-insight-block-level-element]]
[[note-insight-inline-element]]
[[note-insight-span-element]]
[[note-insight-dom-tree]]

**ポイント**:
- 属性は `<要素 属性名="値">` の形で書く
- `class` 属性はCSS・JavaScriptからの操作の起点になる
- ブロック要素は縦に積まれ、インライン要素は横に並ぶ
- `span` は意味を持たない汎用インライン要素（スタイル適用や範囲指定に使う）
- DOMツリーはブラウザがHTMLを解析して作る木構造。JavaScriptで操作できる

---

## セクション2: フォームの仕組み

[[note-insight-html-form]]
[[note-insight-html-label]]
[[note-insight-form-action-attribute]]
[[note-insight-form-method-attribute]]

**ポイント**:
- `<form>` はユーザー入力をサーバーへ送るコンテナ
- `action` で送信先URL、`method` でGET/POSTを指定する
- `<label>` はフォーム部品と説明文を関連付ける（アクセシビリティに重要）

---

## セクション3: CSSの基本

[[note-insight-css-property-value]]

**ポイント**:
- CSSは `セレクタ { プロパティ: 値; }` の形で書く
- プロパティと値の組み合わせが見た目の設定の最小単位

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| ブロック要素とインライン要素の代表例を一覧にまとめる | - | - | [[note-insight-block-level-element]] |
| DOMツリーをJavaScriptで操作する基本パターンをまとめる | - | - | [[note-insight-dom-tree]] |
| formのmethod="POST"とRailsのルーティングの対応を整理する | - | - | [[note-insight-form-method-attribute]] |

---

## 関連リンク

- [[map-http-client-basics]]
- [[map-web-security-basics]]
- [[map-stimulus-basics]]
- [[map-programming-basics]]
