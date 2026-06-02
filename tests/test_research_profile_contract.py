import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE_DIR = ROOT / "examples/research_profiles"
PROFILE_PATHS = [
    PROFILE_DIR / "default_fast.json",
    PROFILE_DIR / "deep_research.json",
]

REQUIRED_FIELDS = {
    "profile_id",
    "display_name",
    "description",
    "intended_use",
    "source_connectors",
    "iterations",
    "questions_per_iteration",
    "max_results",
    "export_formats",
    "requires_network",
    "risk_notes",
    "audit_requirements",
}


def load_profile(path):
    return json.loads(path.read_text(encoding="utf-8"))


class ResearchProfileContractTests(unittest.TestCase):
    def test_example_profiles_include_required_fields(self):
        for path in PROFILE_PATHS:
            with self.subTest(path=path.name):
                profile = load_profile(path)
                self.assertEqual(REQUIRED_FIELDS, set(profile))
                self.assertTrue(profile["profile_id"])
                self.assertGreaterEqual(len(profile["source_connectors"]), 1)
                self.assertGreaterEqual(len(profile["export_formats"]), 1)
                self.assertGreaterEqual(len(profile["audit_requirements"]), 1)

    def test_iteration_and_result_values_are_bounded(self):
        for path in PROFILE_PATHS:
            with self.subTest(path=path.name):
                profile = load_profile(path)
                self.assertGreaterEqual(profile["iterations"], 1)
                self.assertLessEqual(profile["iterations"], 10)
                self.assertGreaterEqual(profile["questions_per_iteration"], 1)
                self.assertLessEqual(profile["questions_per_iteration"], 12)
                self.assertGreaterEqual(profile["max_results"], 1)
                self.assertLessEqual(profile["max_results"], 100)

    def test_examples_do_not_contain_private_markers(self):
        credential_markers = [
            "api" + "_key",
            "api" + "-key",
            "tok" + "en",
            "sec" + "ret",
            "pass" + "word",
        ]
        blocked_suffixes = [
            "." + "db",
            "." + "sql" + "ite",
            "." + "wav",
            "." + "mp3",
            "." + "mp4",
            "." + "gguf",
            "." + "safetensors",
        ]
        local_path_pattern = re.compile(r"[A-Za-z]:\\")
        offenders = []

        for path in PROFILE_PATHS:
            text = path.read_text(encoding="utf-8").lower()
            if local_path_pattern.search(text):
                offenders.append(f"{path.name}: local path marker")
            for marker in credential_markers:
                if marker in text:
                    offenders.append(f"{path.name}: credential marker")
            for suffix in blocked_suffixes:
                if suffix in text:
                    offenders.append(f"{path.name}: blocked artifact suffix")

        self.assertEqual([], offenders)


if __name__ == "__main__":
    unittest.main()
