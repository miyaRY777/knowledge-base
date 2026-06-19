# セキュリティ基礎マップ

> **このMOCで分かること**: Webセキュリティの主要な脅威と防御策、暗号化・認証の基礎を俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | インターネットセキュリティ | ネット上の情報を守るための考え方と仕組み | [[note-insight-internet-security]] |
| 2 | XSS | 悪意あるスクリプトをページに埋め込む攻撃 | [[note-insight-xss]] |
| 3 | htmlspecialchars とXSS対策 | 特殊文字をエスケープしてXSSを防ぐ方法 | [[note-insight-htmlspecialchars-xss]] |
| 4 | CSRF | ユーザーが意図しないリクエストを送らせる攻撃 | [[note-insight-csrf]] |
| 5 | IDOR | 認可チェックなしに他ユーザーのリソースへアクセスする攻撃 | [[note-insight-idor]] |
| 6 | セッションハイジャック | セッションIDを盗んでなりすます攻撃 | [[note-insight-session-hijacking]] |
| 7 | データ改ざん | 通信途中のデータを不正に書き換える攻撃 | [[note-insight-data-tampering]] |
| 8 | 中間者攻撃 | 通信を傍受・改ざんする攻撃手法 | [[note-insight-man-in-the-middle-attack]] |
| 9 | フィッシング | 偽サイトや偽メールで情報を詐取する攻撃 | [[note-insight-phishing]] |
| 10 | マルウェア | 悪意を持って設計されたソフトウェアの総称 | [[note-insight-malware]] |
| 11 | DDoS攻撃 | 大量リクエストでサービスを停止させる攻撃 | [[note-insight-ddos-attack]] |
| 12 | 個人情報漏洩 | 不正アクセスや設定ミスで個人情報が流出するリスク | [[note-insight-personal-information-theft]] |
| 13 | TLS（現行の暗号化プロトコル） | 通信を暗号化する現在の標準プロトコル | [[note-insight-tls-current-encryption-protocol]] |
| 14 | SSL（旧来の暗号化プロトコル） | TLSの前身。現在は非推奨 | [[note-insight-ssl-legacy-encryption-protocol]] |
| 15 | SSL証明書の名前とTLS | 名称はSSLのままだがTLSを使っている経緯 | [[note-insight-ssl-certificate-name-for-tls]] |
| 16 | HTTPS | TLSで暗号化されたHTTP通信 | [[note-insight-https]] |
| 17 | ファイアウォール | 不正な通信をフィルタリングする防御の仕組み | [[note-insight-firewall-traffic-control]] |
| 18 | 二要素認証 | パスワード以外の認証要素を追加してセキュリティを高める | [[note-insight-two-factor-authentication]] |

---

## Webの主要攻撃手法

[[note-insight-xss]]
[[note-insight-htmlspecialchars-xss]]
[[note-insight-csrf]]
[[note-insight-idor]]
[[note-insight-session-hijacking]]

**ポイント**:
- XSSはユーザーのブラウザで悪意あるスクリプトを実行させる。`htmlspecialchars` でエスケープして防ぐ
- CSRFはログイン済みユーザーに意図しない操作をさせる。CSRFトークンで防ぐ
- IDORは認可チェックの抜け漏れで発生する。URLのIDを変えるだけで他ユーザーのデータが見える状態
- セッションハイジャックはCookieのセッションIDを盗む。Secure・HttpOnly属性で対策する

---

## 通信の傍受・改ざん攻撃

[[note-insight-data-tampering]]
[[note-insight-man-in-the-middle-attack]]
[[note-insight-phishing]]
[[note-insight-malware]]
[[note-insight-ddos-attack]]
[[note-insight-personal-information-theft]]

**ポイント**:
- 中間者攻撃は通信経路に割り込んでデータを盗み見・改ざんする。TLSで防ぐ
- フィッシングは技術的な脆弱性よりも人の判断ミスを狙う社会工学的攻撃
- マルウェアはウイルス・ランサムウェア・スパイウェアなどの総称
- DDoSは大量リクエストでサーバーを過負荷にする。単体のDoSと分散型のDDoSがある

---

## 暗号化と通信の保護

[[note-insight-tls-current-encryption-protocol]]
[[note-insight-ssl-legacy-encryption-protocol]]
[[note-insight-ssl-certificate-name-for-tls]]
[[note-insight-https]]

**ポイント**:
- 現在の標準は TLS（Transport Layer Security）。SSLは廃止済みだが名称だけ残っている
- HTTPS = HTTP + TLS。通信内容の暗号化・改ざん検知・サーバー認証の3つを提供する
- SSL証明書という言葉は今もよく使われるが、実態は TLS 証明書

---

## 防御の仕組み

[[note-insight-firewall-traffic-control]]
[[note-insight-two-factor-authentication]]
[[note-insight-internet-security]]

**ポイント**:
- ファイアウォールは許可ルールに基づいて通信を遮断・許可する。不正アクセスの第一防衛線
- 二要素認証はパスワード漏洩だけではログインできない仕組み。「知っているもの＋持っているもの」
- セキュリティは攻撃を知ることと、多層防御（Defense in Depth）の両方が大切

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| SQLインジェクションのノートを作成する | - | - | - |
| CSPヘッダーによるXSS対策を整理する | - | - | - |
| セキュリティヘッダー（X-Frame-Options など）を整理する | - | - | - |

---

## 関連リンク

- [[map-web-security-basics]]
- [[map-cookie-basics]]
- [[map-session-basics]]
- [[map-network-basics]]
- [[map-http-status-and-methods]]
