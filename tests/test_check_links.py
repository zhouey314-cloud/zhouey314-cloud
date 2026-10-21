from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_links import check


class LinkCheckerTests(unittest.TestCase):
    def run_case(self, markdown, files=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(markdown, encoding="utf-8")
            for name, content in (files or {}).items():
                (root / name).write_text(content, encoding="utf-8")
            return check(root)[0]

    def test_missing_file_and_heading_are_reported(self):
        failures = self.run_case("[file](missing.md) [heading](#missing)\n# Present\n")
        self.assertEqual(len(failures), 2)
        self.assertTrue(any("missing file" in x for x in failures))
        self.assertTrue(any("missing fragment" in x for x in failures))

    def test_github_heading_punctuation_and_duplicates(self):
        self.assertEqual(self.run_case(
            "# Website / Contact\n# Repeat\n# Repeat\n"
            "[contact](#website--contact) [second](#repeat-1)\n"
        ), [])

    def test_html_resources_and_ids_are_checked(self):
        self.assertEqual(self.run_case(
            '<a href="target.html#proof"><img src="asset.svg"></a>',
            {"target.html": '<p id="proof">Evidence</p>', "asset.svg": '<svg id="art"></svg>'},
        ), [])
        self.assertTrue(self.run_case('<img src="missing.svg">'))

    def test_path_escape_is_rejected(self):
        self.assertIn("escapes repository", self.run_case("[outside](../README.md)")[0])

    def test_fenced_examples_and_remote_links_are_not_local_targets(self):
        self.assertEqual(self.run_case(
            "```md\n[example](missing.md)\n```\n"
            "[source](https://github.com/zhouey314-cloud) [email](mailto:example@example.com)\n"
        ), [])
