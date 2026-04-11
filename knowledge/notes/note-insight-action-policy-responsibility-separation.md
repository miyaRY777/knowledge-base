---
id: note-insight-action-policy-responsibility-separation
title: ActionPolicyは認可をコントローラから分離する
created: 2026-04-11
source: [[2026-04-11_insight_action-policy-and-duration-review]]
---

## Summary
- ActionPolicy は認可ロジックをコントローラに直接書かず、ポリシーへ分離する考え方です。
- 誰が何をできるかを専用クラスに寄せることで責務が明確になります。
- コントローラは処理の流れに集中しやすくなります。

## Tags
#rails #authorization #actionpolicy

## Links
- [[2026-04-11-action-policy-shares-controller]]
- [[note-insight-authorize-and-allowed-to-difference]]
- [[note-insight-hard-block-and-soft-block]]

## Body
ActionPolicy を使うと、認可の条件分岐をコントローラから切り離して、ポリシークラスにまとめられます。これにより、コントローラはリクエストを受けて流れを進める役割に集中し、認可の判断はポリシーが担当する形になります。どこに責務を書くべきかが見えやすくなるのが大きな利点です。

## Example
```ruby
class SharesController < ApplicationController
  def show
    authorize! share_link, to: :show?
  end
end
```

このコードでは、認可の詳細な条件をコントローラに直接書かず、ポリシーへ委譲しています。

## Action
- [ ] `policy(@post)` がどこで生成されるかを別ノート候補として整理する
- [ ] ActionPolicy の controller -> policy -> view の流れ図を作る
