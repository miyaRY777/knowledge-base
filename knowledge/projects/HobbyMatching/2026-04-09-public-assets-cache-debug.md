# public/assets/ キャッシュ問題のデバッグ記録

**日付:** 2026-04-09
**Issue:** #173
**ステータス:** 解決済み

---

## 問題

JS ソースを変更・リビルドしても、ブラウザに変更が一切反映されなかった。

- ハードリロード（Cmd+Shift+R）→ 変化なし
- DevTools キャッシュ無効化 → 変化なし
- シークレットウィンドウ → 変化なし
- `rails tmp:cache:clear` → 変化なし
- Docker 再起動 → 変化なし

---

## 根本原因

`public/assets/` に古いプリコンパイル済みファイルが残っており、Sprockets をバイパスして古い JS が配信されていた。

```
通常（public/assets/ なし）:
  ブラウザ → Rails → Sprockets → app/assets/builds/jsmind_map.js（最新）

public/assets/ がある場合:
  ブラウザ → Rails → public/assets/jsmind_map-[古いハッシュ].js  ← Sprockets スキップ
```

HTML 内のアセットパスは `public/assets/.sprockets-manifest-*.json` から生成される。Rails サーバーはこのマニフェストをメモリにキャッシュするため、`assets:precompile` 後もサーバー再起動が必要。

---

## 診断の決め手

Network タブで配信されている JS の `last-modified` を確認 → **3月26日**（変更前の日付）が返っていた。

```
Request URL: /assets/jsmind_map-537e421....js
last-modified: Thu, 26 Mar 2026 06:31:14 GMT  ← 古い
```

`public/assets/` に同名ファイルが存在することで確定。

---

## 解決手順

```bash
# 1. public/assets/ を削除
rm -rf public/assets

# 2. 最新コードで再コンパイル
docker compose exec web bundle exec rails assets:precompile

# 3. サーバーを再起動してマニフェストを再読み込み
docker compose restart web
```

---

## 補足

- `public/assets/` は `.gitignore` に含まれているため、git・本番（Render）には影響なし
- Render はデプロイ時に `assets:precompile` を毎回実行するため同じ問題は起きない
- 開発環境で `assets:precompile` を手動実行した後は `public/assets/` を削除しておくと安全
