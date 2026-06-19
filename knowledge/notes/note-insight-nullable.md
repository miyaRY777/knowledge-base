---
id: note-insight-nullable
title: nullableは値がnullになる可能性があることを示す
created: 2026-06-05
source: [[2026-06-05_insight_null-and-related-values]]
quiz_streak: 0
quiz_fail_log: []
---

## Summary
- nullable とは、変数やカラムが null を持つ可能性があることを表す考え方です。
- TypeScript では `string | null` のように型で表現します。
- DBでは NOT NULL 制約を付けないカラムが nullable になります。

## Tags
#javascript #typescript #database

## Links
- [[note-insight-null-js]]
- [[note-insight-null-value]]
- [[note-insight-null-check]]

## Body
nullable は特定の言語機能ではなく、「null が入りうる」という設計上の概念です。TypeScript では `strictNullChecks` を有効にすると null と undefined が別の型として扱われ、nullable な変数には `string | null` のように明示が必要になります。DBではカラムに NOT NULL 制約がなければそのカラムは nullable です。

## Example
```ts
let nickname: string | null = null;
nickname = "Taro"; // OK
```
