---
id: note-insight-function-method-argument-basics
title: "関数とメソッドと引数と呼び出しの基本"
created: 2026-04-12
source: [[2026-04-12_insight_stimulus-and-javascript-basics]]
---

## Summary
- 関数は処理をまとめて再利用できる仕組みで、引数はその受け取り口です。
- メソッドはオブジェクトやクラスに属している関数です。
- 呼び出しは定義した関数やメソッドを実際に実行することで、`if` や `()` はその処理の流れを組み立てる基本になります。

## Tags
#javascript #basics

## Links
- [[map-2026-04-learning]]

## Body
関数は、ひとまとまりの処理を名前付きで定義して何度も使えるようにしたものです。`function 名前(引数)` の形で定義でき、`()` の中に受け取りたい値の名前を書きます。オブジェクトやクラスの中に属している関数はメソッドと呼ばれます。定義しただけでは動かず、`greet("Miya")` のように呼び出してはじめて実行されます。また `if (条件)` は条件が合うときだけ処理を進める書き方で、`(1 + 2) * 3` のような `()` はグループ化演算子として評価の順番を変える役割も持ちます。

## Example
```js
function greet(name) {
  console.log(`${name}さん、こんにちは`)
}

const user = {
  greet(name) {
    console.log(`${name}さん、こんにちは`)
  }
}

if ((1 + 2) === 3) {
  greet("Miya")
  user.greet("Miya")
}
```

このコードでは、関数とメソッドを定義し、条件が成り立つときだけ呼び出しています。`name` は引数で、`(1 + 2)` の `()` は先に評価したい式をまとめるために使っています。

## Action
- [ ] 戻り値の考え方も別ノートで整理する
