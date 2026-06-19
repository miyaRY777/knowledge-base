---
id: note-insight-active-job-global-id
title: Global IDはActive Recordオブジェクトをジョブ引数として渡すための仕組み
created: 2026-06-16
source: [[2026-06-16_insight_active-job-enqueue-and-serialization]]
quiz_phase: 1
quiz_streak: 1
quiz_fail_streak: 0
---

## Summary
- Global ID により、モデルオブジェクトをジョブ引数としてそのまま渡せます。
- enqueue 時に `gid://app/User/1` 形式の文字列に変換され、実行時に元のオブジェクトへ復元されます。
- 実行前にレコードが削除されると復元できずエラーになるため注意が必要です。

## Tags
#rails #active-job #global-id

## Links
- [[note-insight-active-job-enqueue]]
- [[note-insight-active-job-serialize]]

## Body
Active Job はジョブ引数をキューに保存する際、Active Record オブジェクトをそのまま保存するのではなく、Global ID という識別子に変換します。Global ID は `gid://アプリ名/モデル名/ID` という形式の文字列で、ジョブ実行時にこの文字列から元のレコードを `find` し直して復元します。フロントマターに `_aj_global_id` キーが付いている場合はその値が Global ID です。復元タイミングでレコードが存在しないと `ActiveRecord::RecordNotFound` になるため、削除される可能性があるレコードを渡す際は考慮が必要です。

## Example
```ruby
# enqueue時: User.find(1) → { "_aj_global_id" => "gid://app/User/1" }
# 実行時:    { "_aj_global_id" => "gid://app/User/1" } → User.find(1) 相当で復元
NotifyUserJob.perform_later(User.find(1))
```
