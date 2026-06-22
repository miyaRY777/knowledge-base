# 可変長の2次元配列を出力

難易度: C
問題ID: stdout_primer__variable_array_step4
参照元: https://paiza.jp/works/mondai/stdout_primer/stdout_primer__variable_array_step4

問題文:
自然数 N と N 個の要素の数列 M が与えられます。1 ≦ i ≦ N の各 i について、i 行目には以下の数列を出力してください。

* 1 以上 M_i 以下のすべての自然数を昇順、半角スペース区切りで出力してください。

入力される値:

```text
N
M_1 M_2 M_3 ... M_N
```

期待する出力:

```text
1 2 3 4 ... M_1
1 2 3 4 ... M_2
...
1 2 3 4 ... M_N
```

答え:

```ruby
n = gets.to_i
m = gets.split.map(&:to_i)

m.each do |num|
  puts (1..num).to_a.join(" ")
end
```

解説:
`gets.to_i` で、出力する行数である `N` を受け取ります。

`gets.split.map(&:to_i)` で、2 行目の `M_1 M_2 M_3 ... M_N` を整数の配列として受け取ります。

`m.each do |num|` で、配列 `m` の値を1つずつ取り出します。
例えば `m = [2, 4, 3, 1]` の場合、`num` は順番に `2`, `4`, `3`, `1` になります。

`(1..num).to_a` で、`1` から `num` までの数値を配列にします。
`join(" ")` で半角スペース区切りにします。

`puts` で出力しているため、各行の末尾には半角スペースではなく改行が入ります。
