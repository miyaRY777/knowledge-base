# 直角三角形状に数値を出力

難易度: D
問題ID: stdout_primer__variable_array_step3
参照元: https://paiza.jp/works/mondai/stdout_primer/stdout_primer__variable_array_step3

問題文:
自然数 N が与えられます。1 ≦ i ≦ N の各 i について、i 行目には以下の数列を出力してください。

* 1 以上 i 以下の数値をすべて、半角スペース区切りで出力してください

入力される値:

```text
N
```

期待する出力:

```text
1
1 2
1 2 3
...
1 2 3 ... N-1
1 2 3 ... N-1 N
```

答え:

```ruby
n = gets.to_i

(1..n).each do |i|
  puts (1..i).to_a.join(" ")
end
```

解説:
`gets.to_i` で入力された `N` を整数として受け取ります。

`(1..n).each do |i|` で、`1` から `n` まで順番に処理します。
例えば `n = 4` の場合、`i` は `1`, `2`, `3`, `4` と変化します。

`(1..i).to_a` で、`1` から `i` までの数値を配列にします。
`join(" ")` を使うことで、半角スペース区切りの文字列にします。

`puts` で出力しているため、各行の末尾には半角スペースではなく改行が入ります。
