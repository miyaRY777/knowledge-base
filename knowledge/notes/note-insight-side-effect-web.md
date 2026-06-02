---
id: note-insight-side-effect-web
title: 副作用はサーバー側の状態を変える処理のこと
created: 2026-06-01
source: [[2026-06-01_insight_html-css-js-and-data-types-basics]]
---

## Summary
- Web開発の「副作用」とは、処理の結果としてサーバー側のデータや状態が変わることです。
- POSTリクエストでフォームを送信すると、DBへの保存や更新が起き、副作用が発生します。
- 同じリクエストを繰り返すと同じデータが複数作成される可能性があるため注意が必要です。

## Tags
#http #web #form #backend

## Links
- [[note-insight-form-method-attribute]]
- [[note-insight-html-form]]

## Body
「副作用」は、関数型プログラミングや副作用のない操作（冪等性）の文脈でも使われる言葉ですが、Web開発では「リクエストを処理した結果、サーバー側の状態が変わること」を指します。GETリクエストはページを取得するだけで状態を変えないのに対し、POSTリクエストはデータの保存・更新・削除を伴うため副作用があります。同じPOSTを何度も送ると重複データができるリスクがあることを覚えておくと、フォームの二重送信対策の必要性も理解しやすくなります。
