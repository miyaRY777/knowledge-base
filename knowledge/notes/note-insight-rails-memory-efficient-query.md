---
id: note-insight-rails-memory-efficient-query
title: "Railsで大量データを効率よく扱うには？"
created: 2026-06-29
updated: 2026-06-29
source: "prep-prompt"
quiz_fail_log: []
---

## Summary
- 大量データを扱うときは「1件を軽くする」と「一度に読む件数を減らす」の2つが基本。
- `pluck` は必要なカラムの値だけ返す（ARオブジェクトを生成しない）。
- `find_each` はバッチ処理で一度にメモリへ載せる件数を制限できる。
- `ActiveRecord::Relation` は遅延評価のため、Arrayに変換するより効率的なことが多い。

## Tags
#rails #activerecord #performance #memory #database

## Links
- [[note-insight-memory-overuse-risk]]
- [[note-insight-gc]]

## Body

### 大量データで起きる問題

必要以上のデータを一度に読み込むと、

- メモリを大量消費する
- Active Recordオブジェクトを大量生成してCPUに負荷がかかる
- 処理速度が遅くなる
- 最悪の場合、メモリ不足でアプリが停止する

という問題が起きる。

---

### ① 1件を軽くする：pluck と select

`User.all` は `SELECT *` を実行し、全カラムをARオブジェクトとして生成する。

使うのが `name` と `age` だけなら、残りのカラムは無駄なメモリを消費している。

#### pluck：値だけ取得（ARオブジェクトを作らない）

```ruby
User.pluck(:name, :age)
# => [["田中", 20], ["佐藤", 30]]
```

- SQL: `SELECT name, age FROM users`
- 戻り値は値の配列（Rubyの配列）
- ARオブジェクトを生成しないのでCPU負荷も低い
- `user.name` とは書けない。`|name, age|` と分解して受け取る

```ruby
labels = User.pluck(:name, :age).map do |name, age|
  "#{name}（#{age}歳）"
end
```

#### select：必要なカラムだけ取得してARオブジェクトを返す

```ruby
User.select(:name, :age)
```

- ARオブジェクトとして返るため `user.update(...)` など通常の操作が使える
- `pluck` より重いが、ARの機能が必要な場合はこちらを使う

#### 使い分けの基準

| 目的 | 使うメソッド |
|------|------------|
| 値だけ欲しい（表示・集計など） | `pluck` |
| ARオブジェクトの機能が必要 | `select` |

---

### ② 一度に読む件数を減らす：find_each

```ruby
User.all.each { |user| ... }
```

これは全件を一度に取得するため、100万件あれば100万件のARオブジェクトがメモリへ乗る。

```ruby
User.find_each(batch_size: 100) do |user|
  user.do_something
end
```

- 100件取得 → 処理 → 不要になればGCが回収 → 次の100件取得、を繰り返す
- 一度に持つオブジェクト数を抑えられる
- 主キー順でバッチ処理するため、独自の並び順には向かない

---

### Array と ActiveRecord::Relation の違い

| 種類 | 特徴 |
|------|------|
| Array | すでにデータを全件持っている |
| ActiveRecord::Relation | 必要になるまでSQLを実行しない（遅延評価） |

```ruby
users = User.where(active: true)  # この時点ではまだSQL未実行
users.each { ... }                # ここで初めてSQLが実行される
```

最初からArrayに変換するより、Relationのまま扱う方が効率的なことが多い。

---

### よくある勘違い

- `pluck` は `select` の完全な上位互換ではない。ARの機能（`update`、`save` など）は使えない。
- `find_each` はいつでも使えるわけではない。主キー順が前提のため、独自ソートには不向き。
- `User.all` が常に悪いわけではない。データ量が少ない場合や全件必要な場面では問題ない。

## Example

```ruby
# 名前と年齢だけ表示する（pluck）
labels = User.pluck(:name, :age).map { |name, age| "#{name}（#{age}歳）" }

# 100万件にメールを送る（find_each）
User.find_each(batch_size: 100) do |user|
  UserMailer.with(user: user).weekly_report.deliver_later
end
```

## 言語化

結論：Railsで大量データを扱うときは「必要なカラムだけ取得する」「一度に読む件数を減らす」の2つを意識することで、メモリとCPUの負荷を抑えられる。

理由：`User.all` のような全件取得はすべてのカラムとARオブジェクトを生成するため、データ量が増えるとメモリを大量消費し、GC多発・スワップ・OOMのリスクがある。必要なデータだけ・必要な件数だけ読み込むことでこの問題を防げる。

具体例：名前と年齢だけ表示したいなら `User.pluck(:name, :age)` で値だけ取得（ARオブジェクト不要）。100万件にメール送信するなら `User.find_each(batch_size: 100)` で100件ずつ処理し、処理済みのオブジェクトをGCに回収させながら進む。

結論（まとめ）：大量データでは「1件を軽くする（pluck / select）」「件数を分割する（find_each）」の2軸で考える。ActiveRecord::Relationの遅延評価も活用し、不要なArrayへの変換は避ける。
