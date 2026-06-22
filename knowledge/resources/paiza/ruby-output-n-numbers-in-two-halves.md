# N 個の数値を前半・後半に分けて出力

難易度: D
問題ID: stdout_primer__variable_array_step1
参照元: https://paiza.jp/works/mondai/stdout_primer/stdout_primer__variable_array_step1

問題文:
偶数 N が入力されます。まず、1 行目には 1 以上 N / 2 以下の数値を半角スペース区切りですべて出力してください。次に、2 行目には N / 2 + 1 以上 N 以下の数値を半角スペース区切りですべて出力してください。
各行の末尾には、半角スペースの代わりに改行を入れてください。

入力される値:
N

期待する出力:

```text
1 2 3 ... N/2
N/2+1 N/2+2 ... N
```

答え:

```ruby
n = gets.to_i

first_half = (1..n / 2).to_a
second_half = (n / 2 + 1..n).to_a

puts first_half.join(" ")
puts second_half.join(" ")
```

解説:
`gets.to_i` で入力された N を整数として受け取ります。
`1..n / 2` で前半の数値、`n / 2 + 1..n` で後半の数値を作ります。
`to_a` で配列に変換し、`join(" ")` を使って半角スペース区切りの文字列にします。
最後に `puts` で出力することで、各行の末尾は半角スペースではなく改行になります。
