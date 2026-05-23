---
id: note-insight-database-lock-types
title: データベースロックは読み書きの制御方法で種類が分かれる
created: 2026-05-23
source: [[2026-05-23_insight_database-lock-types.md]]
---

## Summary
- データベースロックは、同じデータへの同時アクセスを制御する仕組みです。
- 排他ロックは更新を独占し、共有ロックは読み取りを共有しつつ更新を制限します。
- トランザクションや Isolation と組み合わせて、同時更新による不整合を防ぎます。

## Tags
#database #sql #transaction #lock #concurrency

## Links
- [[note-insight-database-locking]]
- [[note-insight-exclusive-lock]]
- [[note-insight-shared-lock]]
- [[note-insight-isolation]]
- [[note-insight-database-transaction]]

## Body
データベースロックは、複数の処理が同じデータへ同時にアクセスするとき、読み取りや更新の競合を制御するための仕組みです。特に在庫数や残高のように、同時更新で値がずれると困るデータでは重要になります。

排他ロックは、対象データを自分だけが変更できる状態にして、他の更新を待たせます。共有ロックは、複数の読み取りは許可しつつ、更新を制限します。どちらもトランザクションと一緒に考えると、同時実行時の整合性を保ちやすくなります。

## Example
- 残高更新では排他ロックで同時更新を防ぐ
- 参照中のデータを不用意に書き換えさせたくないときは共有ロックを使う
- 在庫やチケット残数のような競合しやすい値でロックを検討する
