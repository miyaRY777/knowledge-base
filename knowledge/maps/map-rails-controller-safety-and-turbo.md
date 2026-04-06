# Railsコントローラ安全性とTurboマップ

> **このMOCで分かること**: Turbo Stream 対応、例外処理、認可の安全なデータ取得をひとまとまりで理解できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | Turbo Stream Accept header | Turbo Stream 形式でレスポンスを受け取る指定 | [[note-insight-turbo-stream-accept-header]] |
| 2 | subject(:request!) | リクエスト処理に名前を付ける RSpec の書き方 | [[note-insight-subject-request-bang]] |
| 3 | flash.now in turbo_stream | 画面遷移なしでメッセージを出す方法 | [[note-insight-format-turbo-stream-flash-now-notice]] |
| 4 | redirect_to + notice | HTML リクエスト時の通常遷移と通知 | [[note-insight-format-html-redirect-notice]] |
| 5 | rescue | 例外を捕まえて graceful に処理する方法 | [[note-insight-rescue]] |
| 6 | scoped find | ログインユーザーに紐づく範囲で安全に取得する方法 | [[note-insight-scoped-room-membership-find]] |
| 7 | direct find の危険 | ID だけで探すと認可漏れの原因になる | [[note-insight-room-membership-find]] |
| 8 | IDOR | 他人のデータに触れてしまう脆弱性 | [[note-insight-idor]] |
| 9 | RecordNotFound | 見つからないときに起きる例外 | [[note-insight-active-record-record-not-found]] |
| 10 | destroy! と destroy | 失敗時に例外を出すかどうかの差 | [[note-insight-destroy-vs-destroy-bang]] |
| 11 | graceful handling | ユーザー体験を壊さずエラー対応する考え方 | [[note-insight-graceful-handling]] |
| 12 | where.not | 除外条件で絞り込むクエリ | [[note-insight-where-not]] |
| 13 | ActiveRecord::Relation | クエリ条件を保持するオブジェクト | [[note-insight-active-record-relation]] |

---

## セクション1: Turbo 対応の分岐

[[note-insight-turbo-stream-accept-header]]
[[note-insight-format-turbo-stream-flash-now-notice]]
[[note-insight-format-html-redirect-notice]]

**ポイント**:
- Turbo Stream では Accept header と `format.turbo_stream` の対応が大事
- 画面遷移なしなら `flash.now`、通常 HTML なら `redirect_to` を使う

---

## セクション2: テストと例外処理

[[note-insight-subject-request-bang]]
[[note-insight-rescue]]
[[note-insight-active-record-record-not-found]]
[[note-insight-destroy-vs-destroy-bang]]
[[note-insight-graceful-handling]]

**ポイント**:
- `subject(:request!)` で request spec を読みやすくできる
- 例外は捕まえる場所と、ユーザーに返す振る舞いを分けて考える

---

## セクション3: 認可と安全な取得

[[note-insight-scoped-room-membership-find]]
[[note-insight-room-membership-find]]
[[note-insight-idor]]
[[note-insight-where-not]]
[[note-insight-active-record-relation]]

**ポイント**:
- 関連をたどる取得は IDOR 対策の基本
- `where.not` や Relation を理解すると安全な絞り込みが書きやすい

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| Turbo Stream の request spec をどこまでテンプレ化するか | - | - | [[note-insight-turbo-stream-accept-header]] |
| `destroy` と `destroy!` の使い分けをコントローラ規約としてどう決めるか | - | - | [[note-insight-destroy-vs-destroy-bang]] |
| IDOR 対策を policy 層で共通化するべきか | - | - | [[note-insight-idor]] |

---

## 関連リンク

- [[note-insight-turbo-stream-accept-header]]
- [[note-insight-subject-request-bang]]
- [[note-insight-format-turbo-stream-flash-now-notice]]
- [[note-insight-format-html-redirect-notice]]
- [[note-insight-rescue]]
- [[note-insight-scoped-room-membership-find]]
- [[note-insight-room-membership-find]]
- [[note-insight-idor]]
- [[note-insight-active-record-record-not-found]]
- [[note-insight-destroy-vs-destroy-bang]]
- [[note-insight-graceful-handling]]
- [[note-insight-where-not]]
- [[note-insight-active-record-relation]]
- [[map-rails-basics]]
