# 可変長で分割した配列を出力

難易度: B
問題ID: stdout_primer__variable_array_boss
参照元: https://paiza.jp/works/mondai/stdout_primer/stdout_primer__variable_array_boss

問題文:
自然数 N, M と N 個の自然数からなる数列 A と M 個の自然数からなる数列 B が与えられます。
1 行目には数列 A の最初の B_1 個の値を出力し、2 行目にはその次から B_2 個の値を出力します。
このように、数列 A の値を B_1 個、B_2 個、...、B_M 個で分割し、それぞれの数列を改行区切りで出力してください。

入力される値:

```text
N M
A_1 A_2 A_3 ... A_N
B_1 B_2 B_3 ... B_M
```

期待する出力:

```text
A_1 ... A_{B_1}
A_{B_1+1} ... A_{B_1+B_2}
A_{B_1+B_2+1} ... A_{B_1+B_2+B_3}
...
```

末尾に改行を入れ、余計な文字や空行を含めてはいけません。

答え:

```ruby
n, m = gets.split.map(&:to_i)
a = gets.split.map(&:to_i)
b = gets.split.map(&:to_i)

index = 0

b.each do |count|
  puts a[index, count].join(" ")
  index += count
end
```

解説:
`A` の配列を、`B` に書かれている個数ずつ取り出して出力します。

たとえば `B = [2, 6, 1, 1]` の場合、
最初に `A` から 2 個、次に 6 個、次に 1 個、最後に 1 個取り出します。

`a[index, count]` は、配列 `a` の `index` 番目から `count` 個取り出す書き方です。
`index += count` で、次に取り出す開始位置を進めています。
