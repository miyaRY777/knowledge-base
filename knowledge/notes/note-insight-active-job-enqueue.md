---
id: note-insight-active-job-enqueue
title: enqueueはジョブをキューに登録して後で実行する操作
created: 2026-06-16
source: [[2026-06-16_insight_active-job-enqueue-and-serialization]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- enqueue とは、ジョブをその場で実行せず、バックグラウンドで処理できるようにキューへ登録することです。
- Active Job では `perform_later` を呼んだ時点でジョブが enqueue されます。
- 即時実行する `perform_now` と対比して理解すると違いが明確になります。

## Tags
#rails #active-job #background-job

## Links
- [[note-insight-active-job-perform-later]]
- [[note-insight-active-job-perform-now]]

## Body
enqueue は「キューへ入れる」という動作そのものを指します。ジョブをその場で動かすのではなく、後で実行できるように待ち行列へ登録しておく操作です。Active Job ではバックエンド（Sidekiq、Solid Queue など）がキューを管理し、登録されたジョブを適切なタイミングで取り出して実行します。`perform_later` が enqueue の入口で、`perform_now` は enqueue を介さずに直接実行する手段です。

## Example
```ruby
NotifyUserJob.perform_later(User.find(1))
# ↑ この呼び出しが enqueue にあたる
```
