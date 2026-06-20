# Active Job基礎マップ

> **このMOCで分かること**: Active Jobのジョブ登録・実行・引数の受け渡しの仕組みを整理できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | enqueue | ジョブをキューに登録して後で実行する操作 | [[note-insight-active-job-enqueue]] |
| 2 | perform_later | ジョブをenqueueするメソッド | [[note-insight-active-job-perform-later]] |
| 3 | perform_now | ジョブを即時実行するメソッド | [[note-insight-active-job-perform-now]] |
| 4 | シリアライズ | ジョブ引数をキューに保存できる形式に変換する | [[note-insight-active-job-serialize]] |
| 5 | デシリアライズ | キューからジョブを取り出すときに引数を復元する | [[note-insight-active-job-deserialize]] |
| 6 | Global ID | Active RecordオブジェクトをJobに渡すための仕組み | [[note-insight-active-job-global-id]] |

---

## セクション1: ジョブの登録と実行

[[note-insight-active-job-enqueue]]
[[note-insight-active-job-perform-later]]
[[note-insight-active-job-perform-now]]

**ポイント**:
- `perform_later` はジョブをキューに積む（非同期）
- `perform_now` はその場で実行する（同期）
- enqueue は「予約」、perform は「実行」と覚える

```mermaid
flowchart LR
    subgraph Register["【登録時：リクエスト中】"]
        A["Controller<br>例: UsersController#create"]
        B["Active Job<br>何をするかを決める"]
        C["Queue Adapter<br>保存先へ橋渡し"]
        D["Queue<br>Redis / DB など<br>ジョブを保存"]
    end

    subgraph Execute["【実行時：別プロセス】"]
        E["Worker<br>キューを監視"]
        F["Queue<br>保存済みジョブ"]
        G["Active Job<br>デシリアライズ・実行管理"]
        H["Jobクラス<br>perform(user)"]
        I["実際の処理<br>メール送信 / 画像処理 / API連携"]
    end

    A -->|"perform_later(user)"| B
    B -->|"引数をシリアライズ<br>例: user → Global ID"| C
    C -->|"設定された保存先へ渡す"| D

    E -->|"監視する"| F
    F -->|"ジョブを取り出す"| E
    E -->|"Active Jobに実行を依頼"| G
    G -->|"デシリアライズ<br>例: Global ID → User.find(id)"| H
    H -->|"perform(user)を実行"| I
```

---

## セクション2: 引数の保存と復元

[[note-insight-active-job-serialize]]
[[note-insight-active-job-deserialize]]
[[note-insight-active-job-global-id]]

**ポイント**:
- Active Recordオブジェクトはそのままキューに保存できない
- Global IDを使ってオブジェクトをIDに変換して保存する
- 実行時にIDからオブジェクトを復元（デシリアライズ）する

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| perform_later と perform_now の使い分け基準は？ | - | - | [[note-insight-active-job-perform-later]] |
| Global IDでオブジェクトが削除されていた場合の挙動は？ | - | - | [[note-insight-active-job-global-id]] |

---

## 関連リンク

- [[note-insight-active-job-enqueue]]
- [[note-insight-active-job-perform-later]]
- [[note-insight-active-job-perform-now]]
- [[note-insight-active-job-serialize]]
- [[note-insight-active-job-deserialize]]
- [[note-insight-active-job-global-id]]
- [[map-rails-active-job-email-flow]] — 非同期メール送信の全フロー（シーケンス図）
- [[map-rails-basics]]
