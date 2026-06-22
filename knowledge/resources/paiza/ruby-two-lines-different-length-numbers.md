# 異なる長さの数値を2行に分けて出力

難易度: D
問題ID: stdout_primer__variable_array_step2
参照元: https://paiza.jp/works/mondai/stdout_primer/stdout_primer__variable_array_step2

問題文:
自然数 N, M が与えられます。1 行目には 1 以上 N 以下の数値を半角スペース区切りで出力してください。また、2 行目には 1 以上 M 以下の数値を半角スペース区切りで出力してください。
さらに、各行の末尾には、半角スペースの代わりに改行を入れてください。

入力される値:

```text
N M
```

期待する出力:

```text
1 2 3 ... N
1 2 3 ... M
```

答え:

```ruby
n, m = gets.split.map(&:to_i)

puts (1..n).to_a.join(" ")
puts (1..m).to_a.join(" ")
```

解説:
`gets.split` で入力された `N M` を分けて受け取ります。
`map(&:to_i)` を使うことで、文字列を整数に変換します。
`n, m = ...` と書くことで、1つ目の値を `n`、2つ目の値を `m` に入れています。

`(1..n).to_a` は `1` から `n` までの数値を配列にします。
`join(" ")` を使うことで、配列の中身を半角スペース区切りで文字列にします。

`puts` で出力しているので、各行の末尾には半角スペースではなく改行が入ります。
