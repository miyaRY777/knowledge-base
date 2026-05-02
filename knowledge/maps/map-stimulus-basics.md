# Stimulus基礎マップ

> **このMOCで分かること**: Stimulus コントローラの基本要素を、接続・要素参照・値受け渡し・イベント処理の観点で整理できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | connect() | コントローラ接続時に初期化処理を行う | [[note-insight-stimulus-connect-callback]] |
| 2 | static targets | 操作したい要素へ名前を付ける | [[note-insight-stimulus-targets]] |
| 3 | static values | data属性を型付きで受け取る | [[note-insight-stimulus-values]] |
| 4 | event / currentTarget | 何が起きてどこで受けたかを知る | [[note-insight-event-and-current-target]] |
| 5 | dataset | data属性から状態や識別子を読む | [[note-insight-dataset-and-data-attributes]] |
| 6 | classList / hidden | 表示状態を切り替える | [[note-insight-classlist-and-hidden]] |
| 7 | Classes API | class名をHTMLから受け取る | [[note-insight-stimulus-classes-property-api]] |
| 8 | エントリーポイント | JSやビルド処理の読み込み起点 | [[note-insight-entry-point]] |
| 9 | CSSエントリ | スタイル読み込みやビルドの起点 | [[note-insight-css-entry]] |
| 10 | ビルド出力 | 変換後にブラウザへ渡す成果物 | [[note-insight-build-output]] |
| 11 | TailwindレスポンシブGrid | 画面幅に応じて列数を切り替える指定 | [[note-insight-tailwind-responsive-grid-columns]] |

---

## セクション1: ライフサイクルと初期化

[[note-insight-stimulus-connect-callback]]

**ポイント**:
- `connect()` は最初の見た目や状態をそろえる場所になる
- `disconnect()` と対で考えると後片付けの整理もしやすい

---

## セクション2: 要素参照と値受け渡し

[[note-insight-stimulus-targets]]
[[note-insight-stimulus-values]]
[[note-insight-dataset-and-data-attributes]]

**ポイント**:
- `targets` は要素参照、`values` は設定値、`dataset` は個々の属性読み取りに向く
- `hasXTarget` のような存在確認を使うと optional な要素にも安全に対応できる

---

## セクション3: イベント処理と表示切り替え

[[note-insight-event-and-current-target]]
[[note-insight-classlist-and-hidden]]
[[note-insight-stimulus-classes-property-api]]

**ポイント**:
- `event.currentTarget` で、どの要素に紐付いた処理かを安定して取れる
- `classList` と `hidden` の組み合わせは開閉UIの基本パターンになる
- Classes API を使うと class 名を JS に直書きせずに済む

---

## セクション4: フロントエンド資産の入口

[[note-insight-entry-point]]
[[note-insight-css-entry]]
[[note-insight-build-output]]
[[note-insight-tailwind-responsive-grid-columns]]

**ポイント**:
- エントリーポイントは、JavaScript や CSS をどこから読み込み始めるかを示す
- ビルド出力は編集元ではなく、変換後にブラウザへ渡す結果として見る
- Tailwind のレスポンシブ指定は、画面幅ごとの見た目の切り替えに使う

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| `event.target` と `event.currentTarget` の違いを DOM ツリー込みで説明したい | - | - | [[note-insight-event-and-current-target]] |
| `values` と `dataset` をどう使い分けるかを実例で整理したい | - | - | [[note-insight-stimulus-values]] |
| `disconnect()` が必要になる典型例を追加したい | - | - | [[note-insight-stimulus-connect-callback]] |
| エントリーポイントとビルド出力の違いをRails構成で説明したい | - | - | [[note-insight-entry-point]] |

---

## 関連リンク

- [[2026-04-08-member-detail-tabs]]
- [[2026-04-09-tabs-controller-css-refactor]]
- [[2026-04-12-rooms-ui-improvement]]
- [[2026-04-12-profile-edit-ui]]
- [[note-insight-entry-point]]
- [[note-insight-css-entry]]
- [[note-insight-build-output]]
- [[note-insight-tailwind-responsive-grid-columns]]
