# Java基礎マップ

> **このMOCで分かること**: Javaの型システム・演算・制御フロー・オブジェクト指向の基礎を俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | プリミティブ型 | Javaの基本データ型（int・double・booleanなど） | [[note-insight-primitive-type]] |
| 2 | int型とlong型 | 扱える整数の範囲が異なる整数型 | [[note-insight-int-vs-long-type]] |
| 3 | 整数データ型 | byte・short・int・longの使い分け | [[note-insight-integer-data-type]] |
| 4 | 整数の範囲 | 各整数型が表現できる最大・最小値 | [[note-insight-integer-range]] |
| 5 | 32ビット整数 | int型は32ビットで約±21億まで表現できる | [[note-insight-32bit-integer]] |
| 6 | 符号あり整数型 | 正負両方を扱う整数型 | [[note-insight-signed-integer-type]] |
| 7 | 符号なし整数型 | 0以上のみを扱う整数型 | [[note-insight-unsigned-integer-type]] |
| 8 | bigint型 | 非常に大きな整数を扱うデータ型 | [[note-insight-bigint-data-type]] |
| 9 | double型 | 64ビットの浮動小数点型 | [[note-insight-double-type]] |
| 10 | float型 | 32ビットの浮動小数点型 | [[note-insight-float-type]] |
| 11 | fixed-point型 | 小数点位置を固定して精度を保つ型 | [[note-insight-fixed-point-type]] |
| 12 | char型 | 1文字を文字コードとして保存する型 | [[note-insight-char-type]] |
| 13 | boolean型 | true/falseの2値を持つ型 | [[note-insight-boolean-type]] |
| 14 | String型 | 文字列を扱う参照型 | [[note-insight-string-type]] |
| 15 | キャスト | 値を指定した型として扱う明示的な型変換 | [[note-insight-cast]] |
| 16 | 型昇格 | 演算時に小さい型が大きい型に自動変換される仕組み | [[note-insight-type-promotion]] |
| 17 | 演算結果の型 | オペランドの型によって演算結果の型が決まる | [[note-insight-calculation-result-type]] |
| 18 | 混合型の演算式 | 異なる型同士の演算で型変換が起きる | [[note-insight-mixed-type-arithmetic]] |
| 19 | 整数除算の型キャスト | 整数÷整数は整数になる。float除算にはキャストが必要 | [[note-insight-division-type-cast]] |
| 20 | オペランドの型 | 演算子の左右にある値の型 | [[note-insight-operand-type]] |
| 21 | オペランドの型と結果の違い | 型の組み合わせで結果の型が変わるケース | [[note-insight-operand-type-result-diff]] |
| 22 | forループ | 繰り返し処理の基本構文 | [[note-insight-for-loop]] |
| 23 | 無限ループ | 終了条件がない・誤ったループ | [[note-insight-infinite-loop]] |
| 24 | 初期化 | 変数を宣言時に値を設定すること | [[note-insight-initialization]] |
| 25 | 不変条件（invariant） | ループや処理の中で常に成り立つ条件 | [[note-insight-invariant]] |
| 26 | 関数・メソッドの引数 | 呼び出し時に渡す値のルール | [[note-insight-function-method-argument-basics]] |
| 27 | 戻り値 | メソッドが処理結果として返す値 | [[note-insight-return-value]] |
| 28 | 副作用（関数） | 関数が戻り値以外に外部状態を変更すること | [[note-insight-side-effect-function]] |
| 29 | オブジェクト指向プログラミング | クラスとオブジェクトを中心とした設計思想 | [[note-insight-object-oriented-programming]] |
| 30 | オブジェクト基盤言語 | すべてがオブジェクトとして扱われる言語の特徴 | [[note-insight-object-based-language]] |
| 31 | コンソール出力 | System.out.println などでデバッグ・確認する方法 | [[note-insight-console]] |

---

## Javaのデータ型

[[note-insight-primitive-type]]
[[note-insight-int-vs-long-type]]
[[note-insight-integer-data-type]]
[[note-insight-integer-range]]
[[note-insight-32bit-integer]]
[[note-insight-signed-integer-type]]
[[note-insight-unsigned-integer-type]]
[[note-insight-bigint-data-type]]

**ポイント**:
- Javaは静的型付け言語。変数宣言時に型を指定する
- 整数型は `byte(8bit)` → `short(16bit)` → `int(32bit)` → `long(64bit)` の順に範囲が広がる
- int は約±21億。それ以上なら long を使う
- 符号あり（signed）は負の数も表現できる。符号なし（unsigned）は0以上のみで上限が2倍になる

---

## 小数・文字・論理型

[[note-insight-double-type]]
[[note-insight-float-type]]
[[note-insight-fixed-point-type]]
[[note-insight-char-type]]
[[note-insight-boolean-type]]
[[note-insight-string-type]]

**ポイント**:
- 小数はデフォルト `double`（64bit）。精度が低くてよければ `float`（32bit）
- `char` は1文字を Unicode の数値として保持する。文字列は `String`（参照型）
- `boolean` は `true` / `false` のみ。条件分岐や返り値に使う
- 金融計算など精度が重要な場合は `BigDecimal`（fixed-point相当）を使う

---

## 型変換と演算

[[note-insight-cast]]
[[note-insight-type-promotion]]
[[note-insight-calculation-result-type]]
[[note-insight-mixed-type-arithmetic]]
[[note-insight-division-type-cast]]
[[note-insight-operand-type]]
[[note-insight-operand-type-result-diff]]

**ポイント**:
- 型昇格: 小さい型と大きい型の演算では、小さい型が自動的に大きい型に変換される
- `int / int` は小数点以下が切り捨てられる。小数にしたい場合は `(double) a / b` とキャストする
- キャストは明示的な型変換。大きい型から小さい型へのキャストは情報が失われることがある

---

## 制御フローと関数

[[note-insight-for-loop]]
[[note-insight-infinite-loop]]
[[note-insight-initialization]]
[[note-insight-invariant]]
[[note-insight-function-method-argument-basics]]
[[note-insight-return-value]]
[[note-insight-side-effect-function]]

**ポイント**:
- `for` ループは「初期化・条件・更新」の3つをセットで書く
- 無限ループは終了条件の書き忘れや条件の論理ミスで発生する
- 不変条件（invariant）はループが何周しても変わらない性質。アルゴリズムの正しさを確認する道具
- メソッドは引数で入力を受け取り、戻り値で出力を返す。副作用は最小限にするのが原則

---

## オブジェクト指向

[[note-insight-object-oriented-programming]]
[[note-insight-object-based-language]]
[[note-insight-console]]

**ポイント**:
- OOPはクラスでデータと振る舞いをまとめ、オブジェクトとして使う設計思想
- Javaはクラスベースの純粋なOOP言語。すべてのコードはクラス内に書く
- `System.out.println` はコンソールに出力する。デバッグや動作確認に使う

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| 例外処理（try-catch）のノートを作成する | - | - | - |
| インターフェースと抽象クラスの違いを整理する | - | - | - |
| コレクション（ArrayList・HashMapなど）をまとめる | - | - | - |

---

## 関連リンク

- [[map-programming-basics]]
- [[map-type-and-literal-basics]]
- [[map-type-conversion-basics]]
- [[map-operator-and-expression-basics]]
- [[map-data-types-and-binary-basics]]
