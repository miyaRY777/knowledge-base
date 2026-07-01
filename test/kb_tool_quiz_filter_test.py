#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KB_TOOL = ROOT / ".codex" / "skills" / "knowledge-base" / "scripts" / "kb_tool.py"


def load_kb_tool():
    spec = importlib.util.spec_from_file_location("kb_tool_under_test", KB_TOOL)
    if spec is None or spec.loader is None:
        raise RuntimeError("kb_tool.py を読み込めませんでした")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_note(notes_dir: Path, name: str, fail_log: str) -> None:
    notes_dir.mkdir(parents=True, exist_ok=True)
    (notes_dir / f"{name}.md").write_text(
        "\n".join(
            [
                "---",
                f"id: {name}",
                f"title: {name} title",
                "created: 2026-06-15",
                f"quiz_fail_log: {fail_log}",
                "---",
                "",
                "## Summary",
                f"- {name} summary",
                "",
                "## Tags",
                "#rails",
                "",
                "## Body",
                f"{name} body",
                "",
            ]
        ),
        encoding="utf-8",
    )


class NoteExtractionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.kb_tool = load_kb_tool()

    def test_extract_summary_lines_from_prep_sections(self) -> None:
        text = "\n".join(
            [
                "## 背景",
                "背景の説明です。",
                "",
                "## 結論",
                "**これは結論です。**",
                "",
                "## 理由",
                "理由の説明です。",
                "",
                "## 具体例",
                "具体例です。",
                "",
                "## まとめ",
                "まとめの説明です。",
            ]
        )

        self.assertEqual(
            self.kb_tool.extract_summary_lines(text),
            ["これは結論です。", "まとめの説明です。", "背景の説明です。"],
        )

    def test_extract_explanation_from_prep_sections_without_body(self) -> None:
        text = "\n".join(
            [
                "## 背景",
                "背景の説明です。",
                "",
                "## 結論",
                "結論です。",
                "",
                "## 言語化",
                "- 何のためにある？：確認用",
            ]
        )

        explanation = self.kb_tool.extract_explanation(text)

        self.assertIn("## 背景\n背景の説明です。", explanation)
        self.assertIn("## 結論\n結論です。", explanation)
        self.assertIn("## 言語化\n- 何のためにある？：確認用", explanation)


class QuizFailLogFilterTest(unittest.TestCase):
    def run_quiz(self, argv: list[str]) -> str:
        kb_tool = load_kb_tool()
        with tempfile.TemporaryDirectory() as tmp:
            notes_dir = Path(tmp) / "notes"
            write_note(notes_dir, "note-zero", "[]")
            write_note(notes_dir, "note-one", "[2026-06-10]")
            write_note(notes_dir, "note-two", "[2026-06-10, 2026-05-01]")
            write_note(notes_dir, "note-june-two", "[2026-06-01, 2026-06-20, 2026-05-03]")
            kb_tool.NOTES = notes_dir

            args = kb_tool.build_parser().parse_args(["quiz", "--count", "10", "--seed", "1", *argv])
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = kb_tool.cmd_quiz(args)

            self.assertEqual(result, 0)
            return output.getvalue()

    def test_filters_by_total_fail_count_with_claude_style_argument(self) -> None:
        output = self.run_quiz(["fail>=2"])

        self.assertIn("note_id: `note-two`", output)
        self.assertIn("note_id: `note-june-two`", output)
        self.assertNotIn("note_id: `note-one`", output)
        self.assertNotIn("note_id: `note-zero`", output)

    def test_filters_by_monthly_fail_count_with_claude_style_argument(self) -> None:
        output = self.run_quiz(["fail-in:2026-06=2"])

        self.assertIn("note_id: `note-june-two`", output)
        self.assertNotIn("note_id: `note-two`", output)
        self.assertNotIn("note_id: `note-one`", output)
        self.assertNotIn("note_id: `note-zero`", output)


if __name__ == "__main__":
    unittest.main()
