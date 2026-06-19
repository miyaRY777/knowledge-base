---
id: note-insight-htmlspecialchars-xss
title: "htmlspecialcharsでユーザー入力をエスケープしてXSSを防ぐ"
created: 2026-05-31
source: [[2026-05-31_insight_cs-basics-data-types-encoding.md]]
quiz_streak: 2
quiz_fail_log: []
---

## Summary
- `htmlspecialchars()` はPHPの関数で、HTMLの特殊文字をエンティティに変換します。
- `<script>` などの危険なタグをそのまま出力せず、ただの文字列として表示させます。
- XSS対策の基本的な手段です。

## Tags
#php #security #xss #web

## Links
- [[note-insight-xss]]
- [[note-insight-internet-security]]

## Body
ユーザーが入力した `<script>` などをHTMLにそのまま出力すると、ブラウザがスクリプトとして実行してしまいます（XSS）。`htmlspecialchars()` を使うと `<` → `&lt;`、`>` → `&gt;` のように変換され、ブラウザはそれをタグではなく文字として表示します。`ENT_QUOTES` を指定するとシングルクォートも変換されます。

## Example
```php
$userComment = "<script>alert('Hacked!');</script>";
echo '<div>' . htmlspecialchars($userComment, ENT_QUOTES, 'UTF-8') . '</div>';
// 出力: <div>&lt;script&gt;alert(&#039;Hacked!&#039;);&lt;/script&gt;</div>
// ブラウザ表示: <script>alert('Hacked!');</script>（文字列として表示）
```
