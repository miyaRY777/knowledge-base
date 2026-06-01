---
id: note-insight-data-tampering
title: "データの改ざんは保存中や通信中の内容が勝手に書き換えられること"
created: 2026-04-27
source: [[2026-04-27_insight_internet-security-basics.md]]
quiz_streak: 0
---

## Summary
- データの改ざんは、本来の内容が許可なく変更されること。
- 保存中だけでなく、通信中のデータも改ざん対象になる。
- 情報セキュリティでは、完全性を守るために改ざんを防ぐ必要がある。

## Tags
#security #integrity #data

## Links
- [[note-insight-internet-security]]
- [[note-insight-man-in-the-middle-attack]]
- [[note-insight-https]]

## Body
データの改ざんは、作成されたデータや送信中のデータが、許可なく別の内容に書き換えられることです。たとえば送信した金額や宛先が途中で別の値に変えられると、利用者は正しい処理をしたつもりでも結果が変わってしまいます。

この問題は、情報セキュリティの完全性と関係します。データを安全に扱うには、盗み見を防ぐだけでなく、内容が正しいまま保たれていることも確認できる必要があります。

