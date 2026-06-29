# Rubyメモリ管理基礎マップ

> **このMOCで分かること**: メモリの種類・領域の役割・GC・スワップ・OOMまで、Ruby/Rails視点のメモリ管理を俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | メモリ | プログラムが今使うデータを置く一時的な作業スペース | [[note-insight-memory-as-workspace]] |
| 2 | ディスク | データを長期保存するストレージ | [[note-insight-disk-storage]] |
| 3 | 静的領域 | プログラム起動中ずっと存在するメモリ領域 | [[note-insight-memory-static-area]] |
| 4 | ヒープ | 動的に作られたオブジェクトを置くメモリ領域 | [[note-insight-memory-heap]] |
| 5 | スタック | メソッド呼び出し中の一時情報を管理するメモリ領域 | [[note-insight-memory-stack]] |
| 6 | メモリ使いすぎのリスク | GC多発・スワップ・OOMにつながる | [[note-insight-memory-overuse-risk]] |
| 7 | GC | 使われなくなったオブジェクトを自動回収する仕組み | [[note-insight-gc]] |
| 8 | スワップ | メモリ不足時にディスクをメモリ代わりに使う仕組み | [[note-insight-swap]] |
| 9 | OOM | メモリ不足でプロセスが強制終了される状態 | [[note-insight-oom]] |
| 10 | Rails メモリ効率クエリ | pluck / select / find_each でメモリ負荷を抑える実装方法 | [[note-insight-rails-memory-efficient-query]] |

---

## メモリの種類

[[note-insight-memory-as-workspace]]
[[note-insight-disk-storage]]

**ポイント**:
- メモリ（RAM）は高速だが容量に限りがあり、電源を切ると消える
- ディスクは低速だが大容量で永続的に保存できる
- 処理中のデータはメモリで扱い、必要なときだけディスクから読み込む

---

## メモリの内部領域

[[note-insight-memory-static-area]]
[[note-insight-memory-heap]]
[[note-insight-memory-stack]]

**ポイント**:
- 静的領域: クラス・メソッド情報など、起動中ずっと保持される情報
- ヒープ: 実行中に動的に生成されるオブジェクトの置き場。GCで回収される
- スタック: メソッド呼び出しごとの一時情報。メソッド終了と同時に解放される

---

## メモリ不足の連鎖

[[note-insight-memory-overuse-risk]]
[[note-insight-gc]]
[[note-insight-swap]]
[[note-insight-oom]]

**ポイント**:
- 大量オブジェクト → GC頻発 → 処理遅延
- 物理メモリ枯渇 → スワップ発生 → さらに遅延
- スワップも枯渇 → OOMでプロセス強制終了
- `find_each` による分割処理が基本的な対策
- `pluck` で不要なカラムを取得しないことも有効な対策

[[note-insight-rails-memory-efficient-query]]

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| find_each・in_batches の使い分けを整理する | - | - | [[note-insight-rails-memory-efficient-query]] |
| RubyのGCアルゴリズム（マーク&スイープ）を深掘りする | - | - | - |

---

## 関連リンク

- [[map-computer-architecture-basics]]
- [[map-database-fundamentals]]
- [[map-activerecord-query-basics]]
- [[note-insight-rails-memory-efficient-query]]
