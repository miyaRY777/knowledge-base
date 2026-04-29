# セッション基礎マップ

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | セッション | ユーザーごとの状態を一時的に管理する仕組み | [[note-insight-session]] |
| 2 | セッションID | どのユーザーのセッションかを見分ける識別子 | [[note-insight-session-id]] |
| 3 | セッションCookie | 主にブラウザを閉じるまで保持される一時的な Cookie | [[note-insight-session-cookie]] |
| 4 | セッションとCookie | 状態本体をどこに保存するかの違い | [[note-insight-session-vs-cookie]] |
| 5 | セッションタイムアウト | 無操作時にセッションを無効化する考え方 | [[note-insight-session-timeout]] |
| 6 | セッション終了 | ログアウトなどでセッション状態を破棄すること | [[note-insight-session-termination]] |
| 7 | セッションハイジャック | 盗んだセッションIDで本人になりすます攻撃 | [[note-insight-session-hijacking]] |

---

## セクション1: セッションが必要になる理由

[[note-insight-session]]
[[note-insight-session-vs-cookie]]
[[note-insight-session-cookie]]

**ポイント**:
- HTTP はリクエストごとの状態を自動では覚えない
- セッションはログイン状態やカート情報などを維持するために使われる
- Cookie はブラウザ側に値を持たせる仕組みで、セッションIDの保存にも使われる

---

## セクション2: セッションIDとリクエストの流れ

[[note-insight-session-id]]
[[note-insight-session]]
[[note-insight-session-cookie]]

**ポイント**:
- セッション本体はサーバー側にあり、ブラウザは識別用のセッションIDを持つ構成が一般的
- セッションID は Cookie 経由でブラウザに保存され、次回以降のリクエストで送られる
- セッションID が漏れると、本人になりすまされる危険がある

---

## セクション3: 終了と期限

[[note-insight-session-timeout]]
[[note-insight-session-termination]]

**ポイント**:
- セッションタイムアウトは、放置されたログイン状態の悪用リスクを下げる
- ログアウト時にはセッション情報を削除またはリセットする
- セッションを適切に破棄しないと、意図しないログイン状態が残ることがある

---

## セクション4: セッションの安全性

[[note-insight-session-hijacking]]
[[note-insight-session-id]]
[[note-insight-cookie-secure]]
[[note-insight-cookie-httponly]]
[[note-insight-cookie-samesite]]

**ポイント**:
- セッションハイジャックは、有効なセッションIDを盗んで本人になりすます攻撃
- HTTPS や Cookie 属性は、セッションIDを守るための重要な対策になる
- ログイン時のセッション再生成など、アプリ側の対策も必要になる

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| Rails の `session` が内部で Cookie とどう連携するか | - | - | [[note-insight-session]] |
| セッション固定化攻撃とセッションハイジャックの違いを整理する | - | - | [[note-insight-session-hijacking]] |
| `reset_session` と `session.delete` の使い分けを整理する | - | - | [[note-insight-session-termination]] |
| idle timeout と absolute timeout の違いを追加する | - | - | [[note-insight-session-timeout]] |

---

## 関連リンク

- [[map-cookie-basics]]
- [[map-web-security-basics]]
- [[note-insight-session]]
- [[note-insight-session-id]]
- [[note-insight-session-cookie]]
- [[note-insight-session-vs-cookie]]
- [[note-insight-session-timeout]]
- [[note-insight-session-termination]]
- [[note-insight-session-hijacking]]
- [[note-insight-cookie-secure]]
- [[note-insight-cookie-httponly]]
- [[note-insight-cookie-samesite]]
