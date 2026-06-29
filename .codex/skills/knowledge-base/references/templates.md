# knowledge-base Templates

## ask

```markdown
## 結論
1〜2文で回答

## 根拠
- [[note-xxx]]: このノートから分かること

## 補足
追加文脈

## 次アクション
推奨ステップ
```

## search

```markdown
## 「キーワード」の検索結果（X件）

| ノート | タイトル | マッチ箇所 |
|--------|---------|-----------|
| [[note-...]] | タイトル | Body |
```

## capture

```markdown
# タイトル

**日時**: YYYY-MM-DD
**情報源**: Raycast学習メモ

---
ここにメモを貼る
```

## distill

```markdown
---
id: note-{category}-{short-name}
title: タイトル
created: YYYY-MM-DD
source: [[inbox-file-name]]
---

## Summary
- 要点1
- 要点2
- 要点3

## Tags
#tag1 #tag2

## Links
- [[関連ノート]]

## Body
要点と背景を自分の言葉で要約する
```

## prep-note

```markdown
---
id: note-insight-{topic}
title: "{トピック}とは？"
created: YYYY-MM-DD
updated: YYYY-MM-DD
source: "prep-prompt"
quiz_fail_log: []
---

## Summary（3行）
- 要点1
- 要点2
- 要点3

## Tags
#tag1 #tag2

## Links
- [[関連ノート]]

## Body
PREP ノートの内容をコピペせず、自分の言葉で要約する。
```

## moc

```markdown
# テーママップ

## サマリー

| # | 項目 | 概要 | ノート |
|---|------|------|--------|
| 1 | ... | ... | [[note-...]] |

## 未決事項（Open Questions）

| 項目 | 期限 | 担当 | ノート |
|------|------|------|--------|
| ... | ... | ... | [[note-open-...]] |
```

## journal

```markdown
# YYYY-MM-DD 日誌

## 今日学んだこと

### {その日登録したnoteのタイトル}

~~~md
#### 結論

#### 理由

#### 具体例

#### まとめ
~~~

## 気づき・感想
（一言でもOK）

## 明日やること
- 
```

## monthly-learning-map

```markdown
# YYYY年M月学習マップ

> **このMOCで分かること**: 今月学んだ内容の全体像、テーマ別の入口、重要概念

---

## 今月のサマリー

| 項目 | 内容 |
|------|------|
| 期間 | YYYY-MM |
| 主なテーマ | テーマ1 / テーマ2 / テーマ3 |
| 入口ノート | [[YYYY-MM-DD_insight_xxx.md]] |
| 既存基礎マップ | [[map-...]] |

---

## テーマ別マップ

| # | テーマ | 概要 | MOC |
|---|--------|------|-----|
| 1 | ... | ... | [[map-...]] |

---

## 今月の重要概念

[[note-...]]
[[note-...]]

**ポイント**:
- ...

---

## 今月追加した代表ノート

| 分野 | ノート |
|------|--------|
| ... | [[note-...]], [[note-...]] |

---

## 未決事項（Open Questions）

| 項目 | 関連MOC |
|------|---------|
| ... | [[map-...]] |

---

## 次回の回し方

1. Raycast のメモを `knowledge/inbox/` に入れる
2. `distill` でノート化する
3. 関連テーマの MOC を更新する
4. 月次 MOC に追記する

---

## 関連リンク

- [[map-...]]
- [[note-...]]
```

## knowledge-file-audit

```markdown
## 結論
- 判定: {正しい / 概ね正しいが補足が必要 / 誤りまたは誤解を招く / 一次ソース未確認}
- 要約: {1〜2文で総評}

## 根拠ファイル
- `path/to/file.md`: 確認した内容

## 一次ソース
- {公式資料名}: {URL または参照先}

## 指摘
- 重大度: {高 / 中 / 低}
- 対象: {ノート名 or セクション名}
- 内容: {何が問題か}
- 理由: {なぜ問題か}

## 修正案
- 対象ファイル:
- 修正文案:
- 保存確認: 上記の修正を保存しますか？
```
