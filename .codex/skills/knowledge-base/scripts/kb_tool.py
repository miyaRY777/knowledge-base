#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import random
import re
import sys
from pathlib import Path


ROOT = Path("/Users/miyary777/workspace/miyaRY777/knowledge-base")
KNOWLEDGE = ROOT / "knowledge"
INBOX = KNOWLEDGE / "inbox"
DONE = INBOX / "done"
NOTES = KNOWLEDGE / "notes"
MAPS = KNOWLEDGE / "maps"
PROJECTS = KNOWLEDGE / "projects"


def today_str() -> str:
    return dt.date.today().isoformat()


def slugify(text: str) -> str:
    value = text.strip().lower()
    value = re.sub(r"`", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "untitled"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


def all_markdown_files() -> list[Path]:
    roots = [NOTES, MAPS, PROJECTS, INBOX]
    files: list[Path] = []
    for root in roots:
        files.extend(sorted(root.rglob("*.md")))
    return files


def extract_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("title:"):
            return line.split(":", 1)[1].strip()
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def extract_section(text: str, name: str) -> str:
    pattern = rf"^## {re.escape(name)}.*?\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else ""


def extract_tags(text: str) -> list[str]:
    section = extract_section(text, "Tags")
    return re.findall(r"#([^\s#]+)", section)


def extract_summary_lines(text: str) -> list[str]:
    section = extract_section(text, "Summary")
    if not section:
        section = extract_section(text, "Summary（3行）")
    lines = [line.strip()[2:].strip() for line in section.splitlines() if line.strip().startswith("- ")]
    return lines


def parse_note(path: Path) -> dict[str, object]:
    text = read_text(path)
    return {
        "path": path,
        "name": path.stem,
        "title": extract_title(text, path.stem),
        "summary_lines": extract_summary_lines(text),
        "tags": extract_tags(text),
        "text": text,
    }


def extract_created_date(text: str) -> dt.date | None:
    created = re.search(r"^created:\s*(.+)$", text, flags=re.MULTILINE)
    if not created:
        return None
    try:
        return dt.date.fromisoformat(created.group(1).strip())
    except ValueError:
        return None


def normalize_text(text: str) -> str:
    value = text.lower()
    value = re.sub(r"`+", "", value)
    value = re.sub(r"\s+", " ", value)
    value = re.sub(r"[^\w一-龠ぁ-んァ-ヴー ]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def find_note_by_name(name: str) -> Path | None:
    direct = NOTES / f"{name}.md"
    if direct.exists():
        return direct
    matches = sorted(NOTES.glob(f"*{name}*.md"))
    return matches[0] if matches else None


def replace_tags_section(text: str, tags: list[str]) -> str:
    rendered = " ".join(f"#{tag}" for tag in tags)
    pattern = r"(^## Tags\s*\n)(.*?)(?=^## |\Z)"
    if re.search(pattern, text, flags=re.MULTILINE | re.DOTALL):
        return re.sub(
            pattern,
            lambda match: f"{match.group(1)}{rendered}\n\n",
            text,
            flags=re.MULTILINE | re.DOTALL,
        )
    return text.rstrip() + f"\n\n## Tags\n{rendered}\n"


def replace_frontmatter_field(text: str, key: str, value: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    frontmatter = text[: end + 5]
    body = text[end + 5 :]
    pattern = rf"(?m)^{re.escape(key)}:\s*.*$"
    replacement = f"{key}: {value}"
    if re.search(pattern, frontmatter):
        frontmatter = re.sub(pattern, replacement, frontmatter, count=1)
    else:
        frontmatter = frontmatter[:-5] + f"{replacement}\n---\n"
    return frontmatter + body


def extract_review_streak(text: str) -> int:
    match = re.search(r"^review_streak:\s*(\d+)$", text, flags=re.MULTILINE)
    return int(match.group(1)) if match else 0


def render_quiz_question(title: str) -> str:
    stripped = title.strip()
    if stripped.endswith("とは何か"):
        return f"Q. {stripped}？"
    return f"Q. {stripped} とは何ですか？"


def update_review_state(path: Path, status: str) -> tuple[list[str], int]:
    text = read_text(path)
    tags = extract_tags(text)
    review_tag = "要復習"
    streak = extract_review_streak(text)

    if status == "correct":
        if review_tag in tags:
            streak += 1
            if streak >= 2:
                tags = [tag for tag in tags if tag != review_tag]
                streak = 0
        else:
            streak = 0
    else:
        if review_tag not in tags:
            tags.append(review_tag)
        streak = 0

    updated = replace_tags_section(text, tags)
    updated = replace_frontmatter_field(updated, "review_streak", str(streak))
    if updated != text:
        write_text(path, updated)
    return tags, streak


def judge_quiz_answer(answer: str, note: dict[str, object]) -> tuple[str, str]:
    normalized_answer = normalize_text(answer)
    if normalized_answer in {"", "わからない", "わかりません", "skip", "スキップ"}:
        return "skip", "回答をスキップしました。"

    summaries = [normalize_text(line) for line in note["summary_lines"] if normalize_text(line)]
    reference = " ".join(summaries) if summaries else normalize_text(str(note["title"]))
    ratio = difflib.SequenceMatcher(None, normalized_answer, reference).ratio()

    keyword_hits = 0
    for summary in summaries:
        if len(summary) >= 4 and (summary in normalized_answer or normalized_answer in summary):
            keyword_hits += 2
        elif any(token and token in normalized_answer for token in re.findall(r"[a-z0-9_+-]+|[一-龠]{2,}|[ぁ-んァ-ヴー]{3,}", summary)):
            keyword_hits += 1

    if ratio >= 0.55 or keyword_hits >= 2:
        return "correct", f"要点が十分に含まれています（類似度 {ratio:.2f}）。"
    if ratio >= 0.28 or keyword_hits >= 1:
        return "partial", f"一部は合っていますが、要点がまだ足りません（類似度 {ratio:.2f}）。"
    return "incorrect", f"要点との一致が弱いです（類似度 {ratio:.2f}）。"


def search_files(keyword: str) -> list[dict[str, object]]:
    needle = keyword.lower()
    results: list[dict[str, object]] = []
    for path in all_markdown_files():
        text = read_text(path)
        score = text.lower().count(needle) + path.name.lower().count(needle) * 3
        if score == 0:
            continue
        title = extract_title(text, path.stem)
        match_section = "Body"
        if needle in title.lower():
            match_section = "Title"
        elif needle in " ".join(extract_tags(text)).lower():
            match_section = "Tags"
        elif needle in "\n".join(extract_summary_lines(text)).lower():
            match_section = "Summary"
        excerpt = ""
        for line in text.splitlines():
            stripped = line.strip()
            if not stripped or stripped in {"---"} or stripped.startswith(("id:", "title:", "created:", "source:")):
                continue
            if needle in line.lower():
                excerpt = line.strip()
                break
        results.append(
            {
                "path": path,
                "title": title,
                "score": score,
                "match_section": match_section,
                "excerpt": excerpt,
            }
        )
    return sorted(results, key=lambda item: (-int(item["score"]), str(item["path"])))


def tokenize_question(question: str) -> list[str]:
    normalized = re.sub(r"[？?、。!！「」『』（）()]", " ", question.lower())
    stop_words = {
        "とは",
        "です",
        "ます",
        "について",
        "注意点",
        "教えて",
        "何",
        "どこ",
        "なぜ",
        "どう",
        "ください",
        "は",
        "が",
        "を",
        "に",
        "の",
        "と",
    }
    tokens = []
    raw_tokens = re.findall(r"[a-z0-9_+-]+|[一-龠ぁ-んァ-ヴー]+", normalized)
    for token in raw_tokens:
        if token in stop_words:
            continue
        if len(token) == 1 and re.fullmatch(r"[a-z]", token):
            continue
        tokens.append(token)
    return tokens


def search_question(question: str) -> list[dict[str, object]]:
    exact = search_files(question)
    if exact:
        return exact

    scores: dict[Path, dict[str, object]] = {}
    for token in tokenize_question(question):
        for result in search_files(token):
            path = Path(result["path"])
            if path not in scores:
                scores[path] = dict(result)
            else:
                scores[path]["score"] = int(scores[path]["score"]) + int(result["score"])
                if not scores[path]["excerpt"] and result["excerpt"]:
                    scores[path]["excerpt"] = result["excerpt"]
    return sorted(scores.values(), key=lambda item: (-int(item["score"]), str(item["path"])))


def cmd_capture(args: argparse.Namespace) -> int:
    date_str = args.date or today_str()
    short_title = slugify(args.title)
    path = INBOX / f"{date_str}_insight_{short_title}.md"
    if path.exists() and not args.force:
        print(f"File already exists: {path}")
        return 1
    title = args.title.replace("-", " ").strip()
    body = (
        f"# {title}\n\n"
        f"**日時**: {date_str}\n"
        f"**情報源**: Raycast学習メモ\n\n"
        "---\n\n"
        "ここにメモを貼る\n"
    )
    write_text(path, body)
    print(path)
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    results = search_files(args.keyword)
    print(f"## 「{args.keyword}」の検索結果（{len(results)}件）\n")
    if not results:
        print("該当するノートが見つかりませんでした。")
        return 0
    print("| ノート | タイトル | マッチ箇所 |")
    print("|--------|---------|-----------|")
    for result in results[: args.limit]:
        path = Path(result["path"])
        print(f"| [[{path.stem}]] | {result['title']} | {result['match_section']} |")
    print("\n---\n")
    print("### 詳細\n")
    for result in results[: args.limit]:
        path = Path(result["path"])
        print(f"#### [[{path.stem}]]")
        if result["excerpt"]:
            print(f"> {result['excerpt']}")
        print()
    return 0


def cmd_ask(args: argparse.Namespace) -> int:
    question = args.question.strip()
    tag_match = re.search(r"#([^\s#]+)", question)
    if tag_match:
        tag = tag_match.group(1)
        tagged = [parse_note(path) for path in sorted(NOTES.glob("*.md")) if tag in extract_tags(read_text(path))]
        print(f"## #{tag} のノート一覧（{len(tagged)}件）\n")
        print("| ノート | タイトル | 作成日 |")
        print("|--------|---------|--------|")
        for note in tagged:
            text = str(note["text"])
            created = re.search(r"^created:\s*(.+)$", text, flags=re.MULTILINE)
            created_at = created.group(1) if created else "-"
            print(f"| [[{note['name']}]] | {note['title']} | {created_at} |")
        return 0

    results = search_question(question)
    if not results:
        print("## 回答できない理由\n関連する情報が見つかりませんでした。\n")
        print("## 不足している情報\n- この質問に対応するノートやメモ\n")
        print("## 作るべきノート\n- [ ] 質問テーマに対応するノート")
        return 0

    top = results[: min(3, len(results))]
    print("## 結論")
    print(f"{top[0]['title']} に関する情報が最も近く、関連ノートから要点をたどれます。\n")
    print("## 根拠")
    for result in top:
        note = parse_note(Path(result["path"]))
        summary = " / ".join(note["summary_lines"][:2]) if note["summary_lines"] else str(result["excerpt"])
        print(f"- [[{Path(result['path']).stem}]]: {summary}")
    print("\n## 補足")
    print("上位ヒットを中心に確認してください。必要なら inbox や project ノートまで広げて追加整理できます。\n")
    print("## 次アクション")
    print("- 参照ノートを開いて detail を確認する")
    print("- 情報が弱い場合は `/distill` 相当の整理で補完する\n")
    refs = ", ".join(f"[[{Path(item['path']).stem}]]" for item in top)
    print(f"---\n**参照ノート**: {refs}")
    return 0


def split_inbox_entries(text: str) -> list[dict[str, str]]:
    pattern = re.compile(
        r"- \[ \] `(?P<title>[^`]+)`とは？\n\n👉\s*(?P<lead>.*?)(?=\n---\n|\Z)",
        flags=re.DOTALL,
    )
    entries: list[dict[str, str]] = []
    for match in pattern.finditer(text):
        block = match.group("lead").strip()
        concept = match.group("title").strip()
        body = re.sub(r"^(\*\*解説：\*\*)", "", block, flags=re.MULTILINE).strip()
        entries.append({"concept": concept, "body": body})
    return entries


def infer_tags(text: str, concept: str) -> list[str]:
    sample = f"{concept} {text}".lower()
    tags = []
    if "rails" in sample:
        tags.append("#rails")
    if "active record" in sample or "activerecord" in sample:
        tags.append("#activerecord")
    if "database" in sample or "sql" in sample or "unique" in sample or "null" in sample:
        tags.append("#database")
    if "http" in sample or "api" in sample:
        tags.append("#http")
    if "callback" in sample:
        tags.append("#callbacks")
    return tags or ["#insight"]


def build_note(source_file: str, concept: str, body: str, created: str) -> tuple[str, str]:
    slug = slugify(concept)
    note_id = f"note-insight-{slug}"
    sentences = [item.strip() for item in re.split(r"(?<=[。.!?])\s+", body) if item.strip()]
    summary_lines = sentences[:3] or [body[:60]]
    while len(summary_lines) < 3:
        summary_lines.append(summary_lines[-1])
    summary = "\n".join(f"- {line}" for line in summary_lines[:3])
    tags = " ".join(infer_tags(body, concept))
    content = (
        "---\n"
        f"id: {note_id}\n"
        f"title: {concept}の要点\n"
        f"created: {created}\n"
        f"source: [[{source_file}]]\n"
        "---\n\n"
        "## Summary（3行）\n"
        f"{summary}\n\n"
        "## Tags\n"
        f"{tags}\n\n"
        "## Links\n"
        "- [[関連ノート]]\n\n"
        "## Body\n"
        f"{body.strip()}\n"
    )
    return note_id, content


def cmd_distill(args: argparse.Namespace) -> int:
    source = INBOX / args.file_name
    if not source.exists():
        print(f"Missing inbox file: {source}")
        return 1
    text = read_text(source)
    entries = split_inbox_entries(text)
    if not entries:
        print("抽出できるエントリが見つかりませんでした。")
        return 1
    created = re.search(r"\*\*日時\*\*:\s*(.+)", text)
    created_at = created.group(1) if created else today_str()
    print(f"## /distill 結果\n\n### 抽出したノート（{len(entries)}件）\n")
    generated: list[tuple[str, str, Path]] = []
    for index, entry in enumerate(entries, start=1):
        note_id, body = build_note(args.file_name, entry["concept"], entry["body"], created_at)
        target = NOTES / f"{note_id}.md"
        generated.append((note_id, body, target))
        summary = " / ".join(extract_summary_lines(body)[:3])
        print(f"{index}. **{note_id}** - {entry['concept']}")
        print(f"   - Summary: {summary}")
        print("   - Links: [[関連ノート]]\n")
    if args.write:
        for _, body, target in generated:
            write_text(target, body)
        print(f"### 保存完了\n{len(generated)}件を knowledge/notes/ に保存しました。")
    else:
        print("### 確認")
        print("`--write` を付けると knowledge/notes/ に保存します。")
    return 0


def group_notes_for_theme(theme: str, notes: list[dict[str, object]]) -> list[dict[str, object]]:
    theme_lower = theme.lower()
    filtered = []
    for note in notes:
        blob = f"{note['title']} {' '.join(note['tags'])} {' '.join(note['summary_lines'])}".lower()
        if theme_lower in blob:
            filtered.append(note)
    if filtered:
        return filtered
    return notes


def build_moc(theme: str, notes: list[dict[str, object]]) -> str:
    title = theme.replace("-", " ").title()
    summary_rows = []
    detail_links = []
    for index, note in enumerate(notes, start=1):
        overview = note["summary_lines"][0] if note["summary_lines"] else str(note["title"])
        summary_rows.append(
            f"| {index} | {note['title']} | {overview} | [[{note['name']}]] |"
        )
        detail_links.append(f"[[{note['name']}]]")
    related_links = "\n".join(f"- [[{note['name']}]]" for note in notes[:8])
    return (
        f"# {title}マップ\n\n"
        f"> **このMOCで分かること**: {title} に関するノートの全体像\n\n"
        "---\n\n"
        "## サマリー\n\n"
        "| # | 項目 | 概要 | ノート |\n"
        "|---|------|------|--------|\n"
        f"{chr(10).join(summary_rows)}\n\n"
        "---\n\n"
        "## セクション1: 関連ノート\n\n"
        f"{chr(10).join(detail_links)}\n\n"
        "---\n\n"
        "## 未決事項（Open Questions）\n\n"
        "| 項目 | 期限 | 担当 | ノート |\n"
        "|------|------|------|--------|\n"
        f"| {title} について追加で整理したい点 | - | - | - |\n\n"
        "---\n\n"
        "## 関連リンク\n\n"
        f"{related_links}\n"
    )


def cmd_moc(args: argparse.Namespace) -> int:
    notes = [parse_note(path) for path in sorted(NOTES.glob("*.md"))]
    selected = group_notes_for_theme(args.theme, notes)
    content = build_moc(args.theme, selected)
    target = MAPS / f"map-{slugify(args.theme)}.md"
    if args.write:
        write_text(target, content)
        print(target)
    else:
        print(content)
        print("\n`--write` を付けると保存します。")
    return 0


def cmd_quiz(args: argparse.Namespace) -> int:
    notes = [parse_note(path) for path in sorted(NOTES.glob("*.md"))]
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    if args.tag:
        notes = [note for note in notes if args.tag.lstrip("#") in note["tags"]]
    if args.today_only:
        notes = [
            note for note in notes if extract_created_date(str(note["text"])) == today
        ]
    if args.yesterday:
        target_day = today - dt.timedelta(days=1)
        notes = [
            note for note in notes if extract_created_date(str(note["text"])) == target_day
        ]
    if not notes:
        print("出題対象のノートが見つかりませんでした。")
        return 1
    random.seed(args.seed)
    picks = random.sample(notes, k=min(args.count, len(notes)))
    for index, note in enumerate(picks, start=1):
        print(f"（{index}/{len(picks)}問目）\n")
        print("## 問題\n")
        print(f"**{render_quiz_question(str(note['title']))}**\n")
        print(f"note_id: `{note['name']}`\n")
        if args.show_answer:
            answer = " / ".join(note["summary_lines"][:2]) if note["summary_lines"] else "要約なし"
            print("## 正解\n")
            print(answer)
            print(f"\n## 参照ノート\n[[{note['name']}]]\n")
    return 0


def cmd_quiz_answer(args: argparse.Namespace) -> int:
    path = find_note_by_name(args.note_id)
    if path is None:
        print(f"ノートが見つかりませんでした: {args.note_id}")
        return 1

    note = parse_note(path)
    status, reason = judge_quiz_answer(args.answer, note)
    if status == "correct":
        if args.write:
            tags, streak = update_review_state(path, status="correct")
        else:
            streak = extract_review_streak(str(note["text"]))
            tags = note["tags"]
            if "要復習" in tags:
                streak += 1
                if streak >= 2:
                    tags = [tag for tag in tags if tag != "要復習"]
                    streak = 0
        print("## 結果\n")
        print("✅ 正解\n")
    elif status == "partial":
        if args.write:
            tags, streak = update_review_state(path, status="partial")
        else:
            tags = list(note["tags"]) if "要復習" in note["tags"] else list(note["tags"]) + ["要復習"]
            streak = 0
        print("## 結果\n")
        print("🔺 惜しい\n")
    elif status == "skip":
        if args.write:
            tags, streak = update_review_state(path, status="skip")
        else:
            tags = list(note["tags"]) if "要復習" in note["tags"] else list(note["tags"]) + ["要復習"]
            streak = 0
        print("## 正解\n")
    else:
        if args.write:
            tags, streak = update_review_state(path, status="incorrect")
        else:
            tags = list(note["tags"]) if "要復習" in note["tags"] else list(note["tags"]) + ["要復習"]
            streak = 0
        print("## 結果\n")
        print("❌ 不正解\n")

    answer = " / ".join(note["summary_lines"][:2]) if note["summary_lines"] else str(note["title"])
    if status == "skip":
        print(answer)
        print("\n## 解説")
        print(str(note["text"]).split("## Body", 1)[-1].strip())
        print(f"\n## 復習ポイント\nこのノートをもう一度読んでおきましょう → [[{note['name']}]]")
    else:
        print(reason)
        print("\n## 正解")
        print(answer)
        print("\n## 解説")
        print(str(note["text"]).split("## Body", 1)[-1].strip())
        print(f"\n## 参照ノート\n[[{note['name']}]]")

    if args.write:
        print(f"\n## タグ更新\n現在のタグ: {' '.join(f'#{tag}' for tag in tags)}")
        print(f"連続正解回数: {streak}")
    else:
        print("\n## タグ更新")
        print("`--write` を付けると `#要復習` の付け外しを保存します。")
    return 0


def cmd_weekly_review(args: argparse.Namespace) -> int:
    today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
    since = today - dt.timedelta(days=6)
    inbox_files = sorted(path for path in INBOX.glob("*.md") if path.is_file())
    recent_notes = []
    for path in sorted(NOTES.glob("*.md")):
        text = read_text(path)
        created = re.search(r"^created:\s*(.+)$", text, flags=re.MULTILINE)
        if not created:
            continue
        created_at = dt.date.fromisoformat(created.group(1))
        if since <= created_at <= today:
            recent_notes.append(parse_note(path))
    open_questions = []
    for path in sorted(MAPS.glob("*.md")):
        text = read_text(path)
        section = extract_section(text, "未決事項（Open Questions）")
        if not section:
            continue
        rows = [line for line in section.splitlines() if line.startswith("|") and "------" not in line and "項目" not in line]
        for row in rows:
            cols = [col.strip() for col in row.strip("|").split("|")]
            if cols:
                open_questions.append((cols[0], path.stem))
    print(f"# 週次レビュー（{today.isoformat()}）\n")
    print("## inbox 棚卸し\n")
    print("### Distill候補（要処理）")
    for path in inbox_files:
        print(f"- [ ] {path.name}")
    print("\n## 今週覚えた概念")
    print("\n| 日付 | 概念 | タグ | ノート |")
    print("|------|------|------|--------|")
    for note in recent_notes:
        text = str(note["text"])
        created = re.search(r"^created:\s*(.+)$", text, flags=re.MULTILINE)
        tags = " ".join(f"#{tag}" for tag in note["tags"][:2]) or "-"
        print(f"| {created.group(1) if created else '-'} | {note['title']} | {tags} | [[{note['name']}]] |")
    print("\n## 未解決のOpen Questions\n")
    print("| 項目 | MOC |")
    print("|------|-----|")
    for item, moc in open_questions:
        print(f"| {item} | [[{moc}]] |")
    print("\n## 来週やること")
    print("- [ ] inbox に溜まったメモを distill する")
    print("- [ ] open question を 1 つ選んでノート化する")
    print("- [ ] MOC を 1 つ更新する")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="knowledge-base helper CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    capture = sub.add_parser("capture")
    capture.add_argument("title")
    capture.add_argument("--date")
    capture.add_argument("--force", action="store_true")
    capture.set_defaults(func=cmd_capture)

    search = sub.add_parser("search")
    search.add_argument("keyword")
    search.add_argument("--limit", type=int, default=10)
    search.set_defaults(func=cmd_search)

    ask = sub.add_parser("ask")
    ask.add_argument("question")
    ask.set_defaults(func=cmd_ask)

    distill = sub.add_parser("distill")
    distill.add_argument("file_name")
    distill.add_argument("--write", action="store_true")
    distill.set_defaults(func=cmd_distill)

    moc = sub.add_parser("moc")
    moc.add_argument("theme")
    moc.add_argument("--write", action="store_true")
    moc.set_defaults(func=cmd_moc)

    quiz = sub.add_parser("quiz")
    quiz.add_argument("--tag")
    quiz.add_argument("--count", type=int, default=1)
    quiz.add_argument("--seed", type=int, default=7)
    quiz.add_argument("--today-only", action="store_true")
    quiz.add_argument("--yesterday", action="store_true")
    quiz.add_argument("--today")
    quiz.add_argument("--show-answer", action="store_true")
    quiz.set_defaults(func=cmd_quiz)

    quiz_answer = sub.add_parser("quiz-answer")
    quiz_answer.add_argument("note_id")
    quiz_answer.add_argument("answer")
    quiz_answer.add_argument("--write", action="store_true")
    quiz_answer.set_defaults(func=cmd_quiz_answer)

    weekly = sub.add_parser("weekly-review")
    weekly.add_argument("--today")
    weekly.set_defaults(func=cmd_weekly_review)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
