# コンピュータ基礎構成マップ

> **このMOCで分かること**: 5大装置を中心に、CPU・記憶装置・フォン・ノイマン型アーキテクチャのつながりを俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | 5大装置 | コンピュータを役割で整理する基本枠組み | [[note-insight-computer-five-major-units]] |
| 2 | 入力装置 | データや命令を取り込む入口 | [[note-insight-input-device]] |
| 3 | 出力装置 | 処理結果を外に見せる出口 | [[note-insight-output-device]] |
| 4 | 記憶装置 | データやプログラムを保存する装置 | [[note-insight-storage-device]] |
| 5 | 主記憶装置 | CPU がすぐ使う一時領域 | [[note-insight-main-memory]] |
| 6 | 補助記憶装置 | データを長期保存する場所 | [[note-insight-secondary-storage]] |
| 7 | 制御装置 | 各装置に指示を出す司令塔 | [[note-insight-control-unit]] |
| 8 | 演算装置 | 計算や比較を実行する装置 | [[note-insight-arithmetic-unit]] |
| 9 | CPU | 制御装置と演算装置をまとめた中心装置 | [[note-insight-cpu]] |
| 10 | マザーボード | 各部品を接続する基盤 | [[note-insight-motherboard]] |
| 11 | バス | 部品間でデータを運ぶ通り道 | [[note-insight-bus]] |
| 12 | スロット / ソケット | 部品を取り付ける接続口 | [[note-insight-slot-and-socket]] |
| 13 | 命令 | CPU に実行内容を伝えるデータ | [[note-insight-instruction]] |
| 14 | フェッチ・デコード・実行 | CPU が命令を処理する基本の流れ | [[note-insight-fetch-decode-execute]] |
| 15 | フォン・ノイマン型アーキテクチャ | 5大装置の考え方の土台 | [[note-insight-von-neumann-architecture]] |

---

## 5大装置の全体像

[[note-insight-computer-five-major-units]]

5大装置は、コンピュータを役割ごとに分けて理解するための出発点です。個別の装置を覚える前に、まず全体の枠組みを見ると関係がつかみやすくなります。

---

## 入出力

[[note-insight-input-device]]
[[note-insight-output-device]]

入力装置は情報を取り込み、出力装置は処理結果を外に見せます。人とコンピュータの接点を担う2つの役割です。

---

## 記憶

[[note-insight-storage-device]]
[[note-insight-main-memory]]
[[note-insight-secondary-storage]]

記憶装置は、作業中の一時保持と長期保存で役割が分かれます。主記憶装置と補助記憶装置の違いを分けて理解すると整理しやすくなります。

---

## 接続の土台

[[note-insight-motherboard]]
[[note-insight-bus]]
[[note-insight-slot-and-socket]]

CPU や記憶装置は単独で並んでいるだけではなく、マザーボード上で接続されて連携します。部品同士をどうつなぐかという視点で見ると、バスやスロット / ソケットの役割も理解しやすくなります。

---

## 処理の中心

[[note-insight-control-unit]]
[[note-insight-arithmetic-unit]]
[[note-insight-cpu]]

制御装置が流れを管理し、演算装置が実際の計算や比較を担当します。CPU はその2つをまとめた中心装置です。

---

## 実行の流れ

[[note-insight-instruction]]
[[note-insight-fetch-decode-execute]]

CPU は、メモリに読み込まれた命令を順番に処理して動きます。命令という単位で何をするかが決まり、その処理はフェッチ、デコード、実行の流れを繰り返すことで進みます。全体像としては `ストレージ -> メモリ -> CPU` の流れで理解するとつながりやすいです。

---

## 設計の土台

[[note-insight-von-neumann-architecture]]

フォン・ノイマン型アーキテクチャは、5大装置でコンピュータを理解するための土台になる考え方です。

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| 主記憶装置とキャッシュの違いをどう整理するか | - | - | [[note-insight-main-memory]] |
| SSD と HDD の違いを別ノート化するか | - | - | [[note-insight-secondary-storage]] |
| プログラム内蔵方式をどこまで掘るか | - | - | [[note-insight-von-neumann-architecture]] |

---

## 関連リンク

- [[map-2026-04-learning]]
