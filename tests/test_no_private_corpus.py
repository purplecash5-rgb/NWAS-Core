import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_DIRS = {".git", ".pytest_cache", "__pycache__"}
POLICY_DOCS = {
    Path("docs/CORPUS_POLICY.md"),
    Path("docs/NO_THIRD_PARTY_CORPUS_INCLUDED.md"),
}


def repo_files():
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        if path.is_file():
            yield path, rel


class NoPrivateCorpusTests(unittest.TestCase):
    def test_no_disallowed_binary_or_data_artifacts(self):
        blocked_suffixes = {
            ".db",
            "." + "sql" + "ite",
            "." + "sql" + "ite3",
            ".e" + "pub",
            ".p" + "df",
            ".ht" + "ml",
            ".h" + "tm",
            ".m" + "p3",
            ".m" + "p4",
            ".w" + "av",
            ".m" + "4a",
            ".o" + "gg",
            ".w" + "ebm",
        }
        offenders = [str(rel) for path, rel in repo_files() if path.suffix.lower() in blocked_suffixes]
        self.assertEqual([], offenders)

    def test_sensitive_terms_are_policy_only(self):
        restricted_terms = [
            "N" + "WT",
            "jw" + ".org",
            "embed" + "ding",
            "vector " + "database",
            "SQL" + "ite",
        ]
        offenders = []
        for path, rel in repo_files():
            if rel in POLICY_DOCS:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for term in restricted_terms:
                if term.lower() in text.lower():
                    offenders.append(f"{rel}: {term}")
        self.assertEqual([], offenders)

    def test_no_credential_or_private_path_markers(self):
        credential_words = [
            "api[_-]?key",
            "tok" + "en",
            "sec" + "ret",
            "pass" + "word",
        ]
        patterns = [
            re.compile(word, re.IGNORECASE)
            for word in credential_words
        ]
        local_path_pattern = re.compile(r"[A-Za-z]:\\\\")
        offenders = []
        for path, rel in repo_files():
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if any(pattern.search(text) for pattern in patterns):
                offenders.append(f"{rel}: credential marker")
            if local_path_pattern.search(text):
                offenders.append(f"{rel}: local path marker")
        self.assertEqual([], offenders)


if __name__ == "__main__":
    unittest.main()
