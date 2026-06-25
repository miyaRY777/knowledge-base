---
id: note-insight-ssl-legacy-encryption-protocol
title: "SSLは現在は使われない古い通信暗号化プロトコル"
created: 2026-04-29
source: [[2026-04-29_insight_ssl-tls-security-basics.md]]
review_streak: 1
last_reviewed_on: 2026-04-30
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- SSL は、Webサイトとブラウザ間の通信を暗号化するために使われていた古いプロトコル。
- 現在の安全なWeb通信では、SSLそのものではなく後継の TLS が使われる。
- 「SSL化」や「SSL証明書」という言い方は残っているが、実体は TLS と整理するとわかりやすい。

## Tags
#web #security #ssl #tls #https

## Links
- [[note-insight-https]]
- [[note-insight-tls-current-encryption-protocol]]
- [[note-insight-ssl-certificate-name-for-tls]]
- [[2026-05-08_insight_ssl-tls-basics]]

## Body
SSL は、通信内容を第三者に読まれたり書き換えられたりしにくくするために使われていた暗号化プロトコルです。昔はWebサイトとブラウザの通信を安全にする仕組みとして使われていました。

ただし、現在のWeb通信で実際に使われているのは SSL ではなく、後継の TLS です。それでも実務や説明では「SSL化」「SSL証明書」のような言い方が残っているため、名前としての SSL と、現在使われる技術としての TLS を分けて理解する必要があります。

`SSL/TLS` とまとめて呼ばれる場合もありますが、これは古い呼び名の SSL と現在主に使われる TLS をまとめた表現です。ログイン画面や決済画面で通信を安全にする文脈では、実体としては TLS による HTTPS 通信を指していることが多いです。

## Example
- `http://example.com` は通信が暗号化されていない
- `https://example.com` は TLS によって通信が保護される
- 慣習的には、この HTTPS 化を「SSL化」と呼ぶことがある
- ログイン画面や決済画面では、パスワードやカード情報を守るために HTTPS が使われる


## 言語化

結論：
理由：
具体例：
結論（まとめ）：

## Action
- [ ] SSL と TLS の違いを HTTPS の仕組みとつなげて復習する

<!-- review_log: 2026-05-02 -->
