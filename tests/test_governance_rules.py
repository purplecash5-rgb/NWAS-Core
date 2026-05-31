import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class GovernanceRuleTests(unittest.TestCase):
    def test_governed_answer_links_to_evidence_packet(self):
        answer = json.loads(
            (ROOT / "examples/demo_outputs/synthetic_governed_answer.json").read_text(
                encoding="utf-8"
            )
        )
        packet = json.loads(
            (ROOT / "examples/demo_outputs/synthetic_evidence_packet.json").read_text(
                encoding="utf-8"
            )
        )
        governance = answer["governance"]
        self.assertEqual(packet["id"], governance["evidence_packet_id"])

    def test_warning_flags_prevent_unqualified_direct_answer(self):
        answer = json.loads(
            (ROOT / "examples/demo_outputs/synthetic_governed_answer.json").read_text(
                encoding="utf-8"
            )
        )
        governance = answer["governance"]
        has_warning = any(
            flag["severity"] in {"warning", "blocker"}
            for flag in governance["review_flags"]
        )
        if has_warning:
            self.assertNotEqual("direct", governance["answer_mode"])

    def test_limitations_are_explicit(self):
        answer = json.loads(
            (ROOT / "examples/demo_outputs/synthetic_governed_answer.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertGreaterEqual(len(answer["governance"]["limitations"]), 1)


if __name__ == "__main__":
    unittest.main()
