# Webセキュリティ基礎マップ

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | インターネットセキュリティ | 通信や情報を不正利用から守る全体像 | [[note-insight-internet-security]] |
| 2 | HTTPS | HTTP通信を TLS で暗号化して保護する仕組み | [[note-insight-https]] |
| 3 | TLS | 現在の HTTPS 通信を保護する暗号化プロトコル | [[note-insight-tls-current-encryption-protocol]] |
| 4 | SSL | 現在は使われない古い通信暗号化プロトコル | [[note-insight-ssl-legacy-encryption-protocol]] |
| 5 | SSL証明書 | 名前は SSL でも現在は TLS 通信で使う証明書を指すことが多い | [[note-insight-ssl-certificate-name-for-tls]] |
| 6 | ファイアウォール | 通信を許可またはブロックする仕組み | [[note-insight-firewall-traffic-control]] |
| 7 | 二要素認証 | 複数の要素で本人確認を強くする仕組み | [[note-insight-two-factor-authentication]] |
| 8 | 中間者攻撃 | 通信の間に入り盗聴や改ざんを行う攻撃 | [[note-insight-man-in-the-middle-attack]] |
| 9 | Cookie Secure属性 | HTTPS のときだけ Cookie を送る属性 | [[note-insight-cookie-secure]] |

---

## セクション1: 通信を守る

[[note-insight-https]]
[[note-insight-tls-current-encryption-protocol]]
[[note-insight-ssl-legacy-encryption-protocol]]
[[note-insight-ssl-certificate-name-for-tls]]

**ポイント**:
- HTTPS は HTTP を TLS で保護した通信方式
- SSL は古い呼び方として残るが、現在の実体は TLS と整理する
- 証明書は、接続先サーバーを確認して安全な通信を始めるために関係する

---

## セクション2: 通信経路の攻撃と対策

[[note-insight-man-in-the-middle-attack]]
[[note-insight-data-tampering]]
[[note-insight-firewall-traffic-control]]

**ポイント**:
- 中間者攻撃やデータ改ざんは、通信経路の安全性と関係する
- TLS による暗号化は、盗聴や改ざんのリスクを下げる
- ファイアウォールは、必要な通信だけを通して不要な通信を減らす

---

## セクション3: ログインと本人確認

[[note-insight-two-factor-authentication]]
[[note-insight-phishing]]
[[note-insight-personal-information-theft]]
[[note-insight-session]]
[[note-insight-session-hijacking]]

**ポイント**:
- 2FA はパスワードだけに依存しない本人確認の仕組み
- フィッシングや個人情報の盗難は、認証情報を狙う攻撃とつながる
- ログイン後はセッションやセッションIDの扱いも安全性に関係する

---

## セクション4: Cookieまわりの安全性

[[note-insight-cookie-secure]]
[[note-insight-cookie-httponly]]
[[note-insight-cookie-samesite]]

**ポイント**:
- `Secure` は HTTPS のときだけ Cookie を送る
- `HttpOnly` は JavaScript から Cookie を読めなくする
- `SameSite` はクロスサイト送信を制御する

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| SSL証明書とTLS証明書の呼び方をどう整理するか | - | - | [[note-insight-ssl-certificate-name-for-tls]] |
| TLSがHTTPS通信のどの部分を守るのか | - | - | [[note-insight-tls-current-encryption-protocol]] |
| ファイアウォールとアプリ側の認証・認可の役割分担は何か | - | - | [[note-insight-firewall-traffic-control]] |
| 2FAとセッション管理はログイン後の安全性にどう関係するか | - | - | [[note-insight-two-factor-authentication]] |

---

## 関連リンク

- [[map-cyber-attack-basics]]
- [[map-cookie-basics]]
- [[note-insight-internet-security]]
- [[note-insight-https]]
- [[note-insight-tls-current-encryption-protocol]]
- [[note-insight-ssl-legacy-encryption-protocol]]
- [[note-insight-ssl-certificate-name-for-tls]]
- [[note-insight-firewall-traffic-control]]
- [[note-insight-two-factor-authentication]]
- [[note-insight-man-in-the-middle-attack]]
- [[note-insight-cookie-secure]]
