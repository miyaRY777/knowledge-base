---
id: note-insight-active-job-deserialize
title: Active Jobは実行時にシリアライズされた引数を元のオブジェクトに復元する
created: 2026-06-16
source: [[2026-06-16_insight_active-job-enqueue-and-serialization]]
quiz_phase: 1
quiz_streak: 0
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- デシリアライズとは、シリアライズされたデータを使えるオブジェクトに戻す処理です。
- Active Job はジョブ実行時にキューから取り出した引数を自動でデシリアライズします。
- 対象レコードが削除済みの場合は復元できずエラーになることがあります。

## Tags
#rails #active-job #serialization

## Links
- [[note-insight-active-job-serialize]]
- [[note-insight-active-job-global-id]]

## Body
ジョブ実行時、Active Job はキューから取り出した引数をデシリアライズして `perform` メソッドに渡します。Global ID として保存されていたモデルはここで `find` し直されて元のオブジェクトに戻ります。シリアライズと対になる処理で、こちらも Active Job が自動で行います。ただし、enqueue から実行までの間に対象レコードが削除されていると復元に失敗するため、長時間キューに滞留する可能性がある場合は `find_by` で nil を許容する設計を検討する価値があります。

## Example
```ruby
class NotifyUserJob < ApplicationJob
  def perform(user)
    # ここに渡ってくるuserはデシリアライズ済みのActive Recordオブジェクト
    UserMailer.welcome(user).deliver_now
  end
end
```
