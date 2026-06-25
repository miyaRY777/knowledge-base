# LinuxとOS基礎マップ

> **このMOCで分かること**: OS・Linuxカーネル・Linuxディストリビューションの関係を俯瞰できる

---

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | OS | ハードウェアとアプリの間に入って資源を管理するソフトウェア | [[note-insight-os]] |
| 2 | Linux | OSの中心部分であるカーネルを指す | [[note-insight-linux-kernel]] |
| 3 | Linuxディストリビューション | カーネルにツールを組み合わせてすぐ使える形にしたOS | [[note-insight-linux-distribution]] |

---

## OSとは

[[note-insight-os]]

**ポイント**:
- CPU・メモリ・ファイル・入出力機器などの資源を管理する
- ハードウェアとアプリの間に入り、アプリが直接ハードウェアを操作しなくて済む仕組みを提供する
- Windows・macOS・Linux・iOS・Android が代表例

---

## LinuxとLinuxカーネル

[[note-insight-linux-kernel]]

**ポイント**:
- 厳密にはLinux = Linuxカーネル（OSの中心部分）
- カーネルはCPU・メモリ・周辺機器を管理するOSの中核
- 日常的にはOS全体を「Linux」と呼ぶことが多い

---

## Linuxディストリビューション

[[note-insight-linux-distribution]]

**ポイント**:
- カーネル単体ではOSとして不十分 → ツールを組み合わせた配布版がディストリビューション
- Ubuntu（開発環境向け）・Debian（安定性重視）・Fedora（新技術）・RHEL（企業向け）が代表例
- Rails開発では Docker上のLinux・サーバーへのデプロイで関係する

---

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| GNUプロジェクトとLinuxの関係を整理する | - | - | - |
| Linuxのファイル権限・パーミッションをまとめる | - | - | - |

---

## 関連リンク

- [[map-docker-basics]]
- [[map-computer-architecture-basics]]
