import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"


class SchemaValidationTests(unittest.TestCase):
    def test_schema_files_are_valid_json_objects(self):
        for path in sorted(SCHEMA_DIR.glob("*.schema.json")):
            with self.subTest(path=path.name):
                data = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual("object", data.get("type"))
                self.assertIn("$schema", data)
                self.assertIn("title", data)
                self.assertIn("properties", data)

    def test_synthetic_evidence_packet_shape(self):
        packet_path = ROOT / "examples/demo_outputs/synthetic_evidence_packet.json"
        packet = json.loads(packet_path.read_text(encoding="utf-8"))
        self.assertTrue(packet["id"])
        self.assertTrue(packet["profile_stub"]["synthetic"])
        self.assertGreaterEqual(len(packet["sources"]), 1)
        self.assertGreaterEqual(len(packet["evidence_items"]), 1)

    def test_toy_corpus_is_jsonl_and_synthetic(self):
        corpus_path = ROOT / "examples/toy_corpus/toy_sources.jsonl"
        records = [
            json.loads(line)
            for line in corpus_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        self.assertGreaterEqual(len(records), 1)
        self.assertTrue(all(record["source_type"] == "synthetic" for record in records))


if __name__ == "__main__":
    unittest.main()
