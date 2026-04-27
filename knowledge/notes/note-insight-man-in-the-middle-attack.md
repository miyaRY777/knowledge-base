---
id: note-insight-man-in-the-middle-attack
title: 中間者攻撃は通信の間に入り盗聴や改ざんを行う攻撃
created: 2026-04-27
source: [[2026-04-27_insight_internet-security-basics.md]]
---

## Summary
- 中間者攻撃は、通信する2者の間に攻撃者が入り込む攻撃。
- 通信内容の盗聴や改ざんが行われる可能性がある。
- 暗号化や相手確認が不十分な通信では特に注意が必要。

## Tags
#security #mitm #network

## Links
- [[note-insight-https]]
- [[note-insight-data-tampering]]
- [[note-insight-internet-security]]

## Body
中間者攻撃は、本来は直接やり取りするはずの利用者とサーバーの間に攻撃者が入り込み、通信内容を盗み見たり書き換えたりする攻撃です。

通信が暗号化されていなかったり、接続先が本物か確認できなかったりすると、利用者は正しい相手と通信しているつもりでも、実際には攻撃者を経由している可能性があります。HTTPSのような暗号化と証明書による確認は、この種の攻撃リスクを下げるために重要です。

