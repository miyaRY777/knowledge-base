---
id: note-insight-active-job-perform-later
title: perform_laterはジョブをenqueueするメソッド
created: 2026-06-16
source: [[2026-06-16_insight_active-job-enqueue-and-serialization]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- `perform_later` を呼ぶと、Active Job がジョブをキューに登録（enqueue）します。
- 実際の実行は設定しているバックエンドが適切なタイミングで行います。
- Active Job の「作る→enqueue→実行」という非同期フローの入口にあたるメソッドです。

## Tags
#rails #active-job #background-job

## Links
- [[note-insight-active-job-enqueue]]
- [[note-insight-active-job-perform-now]]

## Body
`perform_later` はジョブクラスに対して呼び出すクラスメソッドです。呼んだ時点ではジョブは実行されず、キューに登録だけされます。その後、Sidekiq や Solid Queue などのバックエンドがワーカープロセスとしてジョブを取り出して実行します。`perform_now` との最大の違いは「呼び出し元の処理をブロックしない」点で、レスポンスを返しながら重い処理をバックグラウンドに任せる場面で使います。

## Example
```ruby
ReportJob.perform_later(current_user.id)
# キューに登録して即座にリターン。実行はバックエンドに委ねる
```
