---
id: note-insight-shared-lock
title: 共有ロックは複数の読み取りを許可しつつ更新を制限する
created: 2026-05-23
source: [[2026-05-23_insight_database-lock-types.md]]
---

## Summary
- 共有ロックは、複数の処理による読み取りを許可するロックです。
- 読み取り中のデータを他の処理が変更することは制限します。
- 参照の安全性を高めたい読み取り中心の処理で使われます。

## Tags
#database #sql #transaction #lock #shared-lock #concurrency

## Links
- [[note-insight-database-lock-types]]
- [[note-insight-database-locking]]
- [[note-insight-isolation]]
- [[note-insight-database-transaction]]

## Body
共有ロックは、対象データを複数の処理が同時に読めるようにしながら、更新は制限するロックです。読み取り同士は共存できますが、同じデータを書き換えようとする処理は待たされる場合があります。

このロックは、参照中のデータが途中で変わると困る場面で役立ちます。たとえば複数の処理が同じデータを確認している間、別の処理が内容を書き換えると、読み取り結果と後続処理の前提がずれることがあります。共有ロックを使うと、読み取りの安全性を保ちつつ、更新タイミングを制御できます。

## Example
- AさんとBさんが同じデータを同時に参照する
- 参照中は、そのデータを書き換える処理を待たせる
- 読み取りが終わったあと、更新処理を進める
