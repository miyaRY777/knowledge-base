---
id: note-insight-active-job-perform-now
title: perform_nowはジョブをその場で同期実行するメソッド
created: 2026-06-16
source: [[2026-06-16_insight_active-job-enqueue-and-serialization]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
quiz_fail_log: []
---

## Summary
- `perform_now` はキューに入れず、呼んだその場で `perform` を同期実行します。
- 処理が完了するまで呼び出し元はブロックされます。
- 非同期処理が不要な場面や、テストで即時実行したい場合に使います。

## Tags
#rails #active-job #background-job

## Links
- [[note-insight-active-job-perform-later]]
- [[note-insight-active-job-enqueue]]

## Body
`perform_now` はジョブの `perform` メソッドをその場で直接呼び出します。enqueue を介さないため、バックエンドの設定に関係なく動作します。`perform_later` が「後でバックグラウンドで」なのに対し、`perform_now` は「今すぐここで」という使い分けです。テストで確実に実行させたいときや、非同期にする必要がないスクリプトなどで使われます。

## Example
```ruby
ReportJob.perform_now(current_user.id)
# ここで処理が完了するまでブロックする
```
