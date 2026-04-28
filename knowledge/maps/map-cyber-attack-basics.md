# 不正攻撃マップ

## サマリー

不正攻撃は、コンピュータ、ネットワーク、Webサービス、アカウント、データなどに対して行われる悪意ある行為のまとまり。

目的は、情報を盗む、通信を盗み見る、データを書き換える、サービスを止める、端末を不正利用する、などに分けられる。

## マインドマップ

- 不正攻撃
  - 全体像
    - [[note-insight-cyber-attack]]
    - [[note-insight-internet-security]]
  - 情報を盗む
    - [[note-insight-personal-information-theft]]
    - [[note-insight-phishing]]
    - [[note-insight-malware]]
  - 通信を盗み見る・書き換える
    - [[note-insight-man-in-the-middle-attack]]
    - [[note-insight-data-tampering]]
    - [[note-insight-https]]
  - サービスを止める
    - [[note-insight-ddos-attack]]
  - Webアプリを悪用する
    - [[note-insight-xss]]
    - [[note-insight-idor]]
  - Cookie / セッションを狙う
    - [[note-insight-cookie-httponly]]
    - [[note-insight-session-hijacking]]
    - [[note-insight-session-cookie]]

## 代表的な攻撃

| 攻撃 | 狙い | 何が起きるか | ノート |
|---|---|---|---|
| フィッシング | 認証情報・個人情報 | 不正ログイン、金銭被害 | [[note-insight-phishing]] |
| マルウェア | 端末・ファイル・情報 | 情報窃取、暗号化、端末悪用 | [[note-insight-malware]] |
| DDoS攻撃 | サービスの可用性 | 表示遅延、サービス停止 | [[note-insight-ddos-attack]] |
| 中間者攻撃 | 通信経路 | 盗聴、改ざん | [[note-insight-man-in-the-middle-attack]] |
| データ改ざん | 保存中・通信中のデータ | 内容が勝手に変わる | [[note-insight-data-tampering]] |
| XSS | 利用者のブラウザ | Cookie悪用、画面改ざん、なりすまし | [[note-insight-xss]] |
| IDOR | 他人のデータ | 権限外アクセス | [[note-insight-idor]] |

## 覚え方

- **盗む**: フィッシング、マルウェア、個人情報の盗難
- **書き換える**: データ改ざん、中間者攻撃
- **止める**: DDoS攻撃
- **ブラウザで実行させる**: XSS
- **権限外に見る**: IDOR

## Open Questions

- CSRFもこのマップに追加する？
- SQLインジェクションを追加する？
- XSSの種類、反射型・保存型・DOM Basedを分ける？
- Cookie / Session系を別マップに分離する？
