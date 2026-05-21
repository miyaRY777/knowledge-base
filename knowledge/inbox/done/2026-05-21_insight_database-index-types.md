* [ ] `B-treeインデックス`とは？

👉 **並び順を使って、検索・範囲検索・並び替えを速くするインデックス**

**解説：**
`B-treeインデックス` は、データを木構造で整理して、目的の値を効率よく探せるようにする仕組みです。
`=` の検索だけでなく、`>`, `<`, `BETWEEN`, `ORDER BY` のような範囲検索や並び替えにも向いています。
多くのDBでは標準的によく使われるインデックスですが、実際の挙動はDBMSによって異なります。([MySQL Developer Zone][1])

```sql
CREATE INDEX index_users_on_email ON users (email);
```

このコードでは、`users.email` を検索しやすくするために `B-treeインデックス` を使っています。

---

* [ ] `ハッシュインデックス`とは？

👉 **完全一致検索を速くするためのインデックス**

**解説：**
`ハッシュインデックス` は、値からハッシュ値を作り、その値を手がかりにデータを探すインデックスです。
`email = 'example@example.com'` のような完全一致検索に向いています。
一方で、大小比較や範囲検索には向かないため、`BETWEEN` や `ORDER BY` では `B-treeインデックス` の方が使いやすい場合があります。DBMSやストレージエンジンによって対応状況は異なります。([MySQL Developer Zone][1])

```sql
CREATE INDEX index_users_on_email_hash ON users USING hash (email);
```

このコードでは、`email` の完全一致検索を速くするために `ハッシュインデックス` を使っています。

---

* [ ] `全文検索インデックス`とは？

👉 **文章の中から単語やキーワードを高速に検索するためのインデックス**

**解説：**
`全文検索インデックス` は、長い文章や説明文の中から、特定の単語を含むデータを探しやすくするためのインデックスです。
通常の `LIKE '%キーワード%'` より、文章検索に適した仕組みを使える場合があります。
PostgreSQLでは全文検索に `GIN` や `GiST` インデックスが使われ、MySQLのInnoDBでは転置インデックス構造の `FULLTEXT` インデックスが使われます。([PostgreSQL][2])

```sql
CREATE INDEX index_articles_on_content ON articles USING GIN (to_tsvector('simple', content));
```

このコードでは、`articles.content` の文章検索を速くするために `全文検索インデックス` を使っています。

[1]: https://dev.mysql.com/doc/refman/9.6/en/index-btree-hash.html?utm_source=chatgpt.com "10.3.9 Comparison of B-Tree and Hash Indexes"
[2]: https://www.postgresql.org/docs/current/textsearch-indexes.html?utm_source=chatgpt.com "18: 12.9. Preferred Index Types for Text Search"
