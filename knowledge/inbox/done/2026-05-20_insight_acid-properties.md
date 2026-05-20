* [ ] `Atomicity（原子性）`とは？

👉 **トランザクション内の処理を、全部成功するか全部なかったことにする性質**

**解説：**
`Atomicity（原子性）` は、複数のデータベース操作を1つのまとまりとして扱う考え方です。
途中でエラーが起きた場合、一部だけ保存されず、すべて元の状態に戻ります。
Railsの `transaction` も、複数のSQLを「1つのまとまり」として成功・失敗させるために使います。Rails公式APIでも、トランザクションは「すべて成功したときだけSQLが永続化される保護ブロック」と説明されています。
([Ruby on Rails API][1])

```ruby
ActiveRecord::Base.transaction do
  user.update!(points: user.points - 100)
  item.update!(stock: item.stock - 1)
end
```

このコードでは、ポイントの減少と在庫の減少をまとめて成功させるために `Atomicity（原子性）` が関係しています。

---

* [ ] `Consistency（一貫性）`とは？

👉 **トランザクション後も、データベースのルールが壊れないようにする性質**

**解説：**
`Consistency（一貫性）` は、トランザクションの前後でデータベースの整合性が保たれることです。
たとえば、NOT NULL制約、外部キー制約、ユニーク制約などに違反したデータが保存されないようにします。
PostgreSQL公式用語集では、ACIDは並行処理やエラー時にもトランザクションの正当性を保証する性質として説明されています。
([PostgreSQL][2])

**具体例：**

* `email` が必須なのに、空のままユーザーを作成しない
* 存在しない `user_id` を使って投稿を作成しない
* 同じメールアドレスのユーザーを重複登録しない

この例では、データベースのルールを守った状態に保つために `Consistency（一貫性）` が関係しています。

---

* [ ] `Isolation（独立性）`とは？

👉 **同時に複数のトランザクションが動いても、互いに悪影響を与えにくくする性質**

**解説：**
`Isolation（独立性）` は、複数の処理が同時に実行されても、データが中途半端な状態で見えたり、競合によって不正な結果になったりしないようにする考え方です。
たとえば、2人が同時に最後の1個の商品を購入しようとしたとき、在庫がマイナスにならないように制御する場面で重要です。
PostgreSQL公式ドキュメントでも、ACIDには `Isolation` が含まれると説明されています。
([PostgreSQL][2])

**具体例：**

* AさんとBさんが同時に同じ商品を購入する
* 在庫が1個しかない場合、両方の購入を成功させない
* 片方の処理が終わるまで、もう片方の処理に影響が出ないようにする

この例では、同時実行によるデータのズレを防ぐために `Isolation（独立性）` が関係しています。

---

* [ ] `Durability（永続性）`とは？

👉 **トランザクションが成功した結果を、消えないように保存する性質**

**解説：**
`Durability（永続性）` は、トランザクションが完了したあと、その結果がデータベースに残り続けることです。
保存が成功した後は、アプリを再起動しても、基本的にその変更は残ります。
PostgreSQL公式用語集では、ACIDはエラーや電源障害などがあってもトランザクションの妥当性を保証する性質として説明されています。
([PostgreSQL][2])

```ruby
user.update!(name: "新しい名前")
```

このコードでは、更新が成功したあとにユーザー名をデータベースへ保存し続けるために `Durability（永続性）` が関係しています。

[1]: https://api.rubyonrails.org/classes/ActiveRecord/Transactions/ClassMethods.html?utm_source=chatgpt.com "ActiveRecord::Transactions::ClassMethods - Rails API"
[2]: https://www.postgresql.org/docs/current/glossary.html?utm_source=chatgpt.com "Documentation: 18: Appendix M. Glossary"
