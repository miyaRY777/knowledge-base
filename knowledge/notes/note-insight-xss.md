---
id: note-insight-xss
title: "XSSは悪意あるスクリプトを他ユーザーのブラウザで実行させる攻撃"
created: 2026-04-25
source: [[2026-04-25_insight_cookie-session-security-basics.md]]
quiz_streak: 1
quiz_fail_log: []
---

## Summary
- XSS は、ページに悪意あるスクリプトが混ざって実行される攻撃。
- ユーザー入力を適切に扱わず表示したときに起こりやすい。
- 画面改ざんだけでなく Cookie 悪用やなりすましにもつながる。

## Tags
#http #web #security #xss

## Links
- [[note-insight-cookie-httponly]]
- [[note-insight-session-cookie]]
- [[note-insight-internet-security]]

## Body
XSS は、Web アプリが入力値を適切に検証したりエスケープしたりせずに表示したときに、悪意あるスクリプトがページへ入り込んでしまう攻撃です。その結果、別のユーザーのブラウザでスクリプトが実行され、画面の書き換えやセッション情報の悪用、なりすましにつながることがあります。対策としては、出力時のエスケープを基本にして、危険な HTML をそのまま表示しないことが重要です。

## Example
```erb
<p><%= params[:name] %></p>
```

このコードでは、入力値の扱いを誤ると XSS につながる可能性がある場面を表しています。

安全に表示する場合は、ユーザー入力をそのままHTMLとして扱わず、出力時にエスケープします。

```erb
<p><%= h(params[:name]) %></p>
```

このコードでは、入力値をHTMLとして実行させず、文字列として表示することでXSSのリスクを下げています。


## 言語化

結論：
理由：
具体例：
結論（まとめ）：
