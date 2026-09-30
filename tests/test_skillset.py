import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "bounded-log-triage",
    "docx-stdlib-workflows",
    "guarded-db-mutation",
    "verified-file-deploy",
    "omp-memory-budget",
    "omp-session-usage-audit",
    "omp-ttsr-rule-calibration",
    "omp-plugin-verification",
    "instrument-data-chart",
    "ui-surface-acceptance",
    "ui-interaction-lifecycle",
    "changed-contract-verification",
    "measured-performance-fix",
    "authoritative-write-boundary",
}


def load_skills():
    return {p.parent.name: p.read_text(encoding="utf-8")
            for p in ROOT.glob("*/SKILL.md")}


class SkillsetTests(unittest.TestCase):
    def test_complete_collection(self):
        self.assertEqual(set(load_skills()), EXPECTED)
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for name in EXPECTED:
            self.assertIn(f"`{name}`", readme)

    def test_metadata_language_and_size(self):
        for name, text in load_skills().items():
            with self.subTest(skill=name):
                match = re.match(
                    r'\A---\nname: ([a-z0-9-]+)\ndescription: "([^"\n]+)"\n---\n', text
                )
                self.assertIsNotNone(match)
                self.assertEqual(match.group(1), name)
                self.assertLessEqual(len(match.group(2)), 160)
                self.assertTrue(text.isascii(), "Shareable prose must be English ASCII")
                self.assertLessEqual(len(text[match.end():].split()), 420)
                self.assertTrue(text.endswith("\n"))

    def test_scope_and_portability(self):
        for name, text in load_skills().items():
            with self.subTest(skill=name):
                self.assertIn("smallest useful thing", text.lower())
                self.assertRegex(text.lower(), r"verif|assert|test|check")
                self.assertNotRegex(
                    text,
                    r"(?i)\b[A-Z]:[/\\]Users[/\\]|/Users/|/home/|"
                    r"[\w.+-]+@[\w-]+\.[a-z]{2,}",
                )
        self.assertEqual(
            [p for p in ROOT.rglob("*.py") if "tests" not in p.relative_to(ROOT).parts],
            [],
            "No external private helper scripts should ship",
        )
        for name in ("coverage.json", "usage.json", "ANALYSIS.md", "validation.json"):
            self.assertFalse((ROOT / name).exists(), "Private audit artifacts are not release content")

    def test_original_safeguards(self):
        skills = load_skills()
        cases = {
            "bounded-log-triage": ["Read-only", "retention", "not proof", "Stop"],
            "docx-stdlib-workflows": ["New document", "Existing template", "Fail before writing", "testzip()", "uncompressed bytes", "unresolved fields"],
            "guarded-db-mutation": ["explicitly requested", "parameterized", "transaction", "rollback", "Never restart/reload"],
            "verified-file-deploy": ["separate explicit authorization", "drift", "backup", "SHA256", "Stop on mismatch", "not prove running behavior"],
            "omp-memory-budget": ["shared", "tokenizer", "Concurrent autolearn", "backup", "headroom", "MEMORY.md"],
            "omp-session-usage-audit": ["message.usage", "top-level", "event timestamps", "unknown is not zero", "subtotals", "not elapsed", "confounds"],
            "omp-plugin-verification": ["regression", "full test", "actual changed surface", "resolved plugin path", "Do not publish"],
            "omp-ttsr-rule-calibration": ["held-out", "proxy, not proven failure", "Back up", "--source", "triggered", "notTriggered", "disposable project", "activation separate"],
            "instrument-data-chart": ["Missing is not zero", "Never invent", "zero baseline", "percentage points", "actual output", "data table/text"],
            "ui-surface-acceptance": ["actual application surface", "4.5:1", "3:1", "24 CSS px", "18.7 CSS px", "hover-only", "screenshot proves neither"],
            "ui-interaction-lifecycle": ["Failed loading is not an empty result", "in-flight operation", "restore focus", "late asynchronous", "non-finite", "Preserve shared"],
            "changed-contract-verification": ["producer, consumer", "failing control", "full affected", "direct-save route", "actual application entrypoint", "activation is unresolved"],
            "measured-performance-fix": ["before/after", "N+1", "await/yield", "EXPLAIN", "late snapshots", "idempotency", "unverified"],
            "authoritative-write-boundary": ["every writer", "field=value", "atomically", "double-charge", "both directions", "Never authorize every client difference", "fails closed", "direct-save bypass", "historical rows", "Missing audit entries", "explicit authorization"],
        }
        for name, terms in cases.items():
            for term in terms:
                with self.subTest(skill=name, safeguard=term):
                    self.assertIn(term, skills[name])

    def test_new_skill_portability_and_references(self):
        names = {
            "instrument-data-chart", "ui-surface-acceptance",
            "ui-interaction-lifecycle", "changed-contract-verification",
            "measured-performance-fix", "authoritative-write-boundary",
        }
        for name in names:
            for path in (ROOT / name).rglob("*.md"):
                text = path.read_text(encoding="utf-8")
                with self.subTest(skill=name, file=path.name):
                    self.assertTrue(text.isascii())
                    self.assertNotRegex(
                        text,
                        r"(?i)FiveM|CitizenFX|OneSync|\bNUI\b|\bCEF\b|"
                        r"C:[/\\]Users[/\\]|/Users/|/home/|Wait\(0\)|resmon",
                    )
                    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                        if "://" in target or target.startswith("#"):
                            continue
                        resolved = (path.parent / target).resolve()
                        self.assertTrue(resolved.is_relative_to(ROOT.resolve()))
                        self.assertTrue(resolved.is_file(), target)
        self.assertNotIn("skill-router", load_skills())
        self.assertTrue(
            (ROOT / "instrument-data-chart/references/instrument-style.md").is_file()
        )

    def test_publication_metadata(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("release candidate", readme.lower())
        self.assertIn("OMP-specific workflows", readme)
        self.assertIn("## Use", readme)
        self.assertIn("MIT License", license_text)
        self.assertIn("Permission is hereby granted, free of charge", license_text)
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", readme):
            if "://" in target or target.startswith("#"):
                continue
            self.assertTrue((ROOT / target).is_file(), target)


if __name__ == "__main__":
    unittest.main()
