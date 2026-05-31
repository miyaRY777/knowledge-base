# データ型・2進数基礎マップ

> **このMOCで分かること**: トランジスタ・2進数・16進数の表現方法から、各言語のデータ型（整数・真偽値・文字）とオーバーフローまでの全体像を俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | トランジスタ | CPUの基本部品・ON/OFFで0と1を表現 | [[note-insight-transistor]] |
| 2 | バイナリ | 0と1だけで表現されたデータ | [[note-insight-binary-data]] |
| 3 | ビット | 情報の最小単位（0か1） | [[note-insight-bit]] |
| 4 | バイト | 8ビットをまとめた単位 | [[note-insight-byte]] |
| 5 | オクテット | バイトの別名（通信・プロトコル分野で使う） | [[note-insight-octet]] |
| 6 | プログラムのデータ | プログラムが扱うデータの基本概念 | [[note-insight-programming-data]] |
| 7 | 2^ビット数 | ビット数で表現できる組み合わせ数を求める式 | [[note-insight-bit-count-combinations]] |
| 8 | 0b表記 | JavaScriptで2進数リテラルを書く方法 | [[note-insight-binary-literal-0b]] |
| 9 | 0x表記 | JavaScriptで16進数リテラルを書く方法 | [[note-insight-hexadecimal-literal-0x]] |
| 10 | ブーリアン型 | true / false を表すデータ型 | [[note-insight-boolean-type]] |
| 11 | int型（符号付き整数型） | 正と負の整数を扱えるデータ型 | [[note-insight-signed-integer-type]] |
| 12 | 符号なし整数型 | 0以上の整数だけを扱うデータ型 | [[note-insight-unsigned-integer-type]] |
| 13 | オーバーフロー | 表現できる範囲を超えて値があふれる現象 | [[note-insight-integer-overflow]] |
| 14 | int型とlong型の違い | 扱える整数の大きさの違い | [[note-insight-int-vs-long-type]] |
| 15 | integer（Rails/DB） | Railsで整数カラムに使うデータ型 | [[note-insight-integer-data-type]] |
| 16 | bigint（Rails/DB） | 大きな整数に対応するDBのカラム型 | [[note-insight-bigint-data-type]] |
| 17 | JavaScriptのNumber型 | 整数も小数も同じ型で扱うJS固有の設計 | [[note-insight-javascript-number-type]] |
| 18 | コンソール | プログラムの実行結果を表示する画面 | [[note-insight-console]] |

---

## ハードウェアの土台

[[note-insight-transistor]]
[[note-insight-binary-data]]
[[note-insight-bit]]
[[note-insight-byte]]
[[note-insight-octet]]

**ポイント**:
- コンピュータはトランジスタのON/OFFによって0と1を実現している
- バイナリ・ビット・バイトはデータの大きさを考えるときの基本単位
- 1バイト = 8ビット。オクテットはネットワーク・プロトコルの文脈でバイトを指す別名

---

## 進数表記とビット計算

[[note-insight-binary-literal-0b]]
[[note-insight-hexadecimal-literal-0x]]
[[note-insight-bit-count-combinations]]

**ポイント**:
- `0b` で2進数、`0x` で16進数リテラルを書ける（JavaScript）
- 16進数1桁 = 4ビット。`3桁 × 4 = 12ビット` のように換算できる
- nビットで表現できる組み合わせ数は 2ⁿ 通り

---

## 整数型の種類

[[note-insight-signed-integer-type]]
[[note-insight-unsigned-integer-type]]
[[note-insight-integer-overflow]]
[[note-insight-int-vs-long-type]]
[[note-insight-integer-data-type]]
[[note-insight-bigint-data-type]]

**ポイント**:
- 符号付き（int）は正負どちらも扱える。最上位ビットを符号に使う分、最大値が小さい
- 符号なし（unsigned）は0以上のみ。同じビット数でより大きな正の数を表現できる
- オーバーフローは最大値を超えたときに値がラップアラウンドする現象。バグの原因になる
- long は int より大きな範囲の整数を扱える（Java: int=32bit, long=64bit）
- Rails/DBでは `integer`（32bit相当）と `bigint`（64bit相当）を使い分ける

---

## 真偽値・JS型の特徴

[[note-insight-boolean-type]]
[[note-insight-javascript-number-type]]

**ポイント**:
- ブーリアン型は `true / false` の2値のみ。条件分岐やフラグ管理の基本
- JavaScriptは `int` / `float` を区別しない。整数も小数も `Number` 型で統一
- 他言語のデータ型と比較することで、JavaScriptの設計上の特徴が見えやすくなる

---

## 開発ツール

[[note-insight-console]]
[[note-insight-programming-data]]

**ポイント**:
- コンソールはデバッグ・動作確認の出発点。`console.log` で値の確認ができる
- プログラムが扱うデータの種類を把握することで、適切な型選択の土台になる

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| 浮動小数点数（float/double）との比較整理 | - | - | [[note-insight-javascript-number-type]] |
| JavaScriptのBigInt型との使い分け | - | - | [[note-insight-javascript-number-type]] |
| オーバーフローが脆弱性につながるケースを整理する | - | - | [[note-insight-integer-overflow]] |

---

## 関連リンク

- [[map-character-encoding-basics]]
- [[map-computer-architecture-basics]]
