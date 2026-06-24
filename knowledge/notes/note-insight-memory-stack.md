---
id: note-insight-memory-stack
title: "スタックはメソッド呼び出し中の一時情報を管理するメモリ領域"
created: 2026-06-24
source: [[2026-06-24_insight_ruby-memory-and-gc-basics.md]]
quiz_fail_log: []
---

## Summary
- スタックは、実行中のメソッドのローカル変数や引数を管理するメモリ領域です。
- メソッドが呼ばれると情報が積まれ、終わると自動的に取り除かれます。
- 一時的な処理の流れを管理する場所です。

## Tags
#ruby #memory #language

## Links
- [[note-insight-memory-as-workspace]]
- [[note-insight-memory-heap]]
- [[note-insight-memory-static-area]]

## Body
スタックは、メソッド呼び出しのたびにローカル変数・引数・戻り先などの情報を積み上げていくメモリ領域です。メソッドが終わると、その情報は自動的にスタックから取り除かれます。

ヒープと異なり、GCによる回収を待たずにメソッド終了と同時に解放されるため、管理コストが低い領域です。

## Example
```ruby
def greet(name)
  message = "こんにちは、#{name}さん"  # name・messageはスタックで管理
  puts message
end

greet("田中")
```

## Action
