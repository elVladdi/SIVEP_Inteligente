"""Regresión documental de una revisión bibliográfica científica autónoma.

Ejecutar: python -m unittest discover -s tests -p 'test_literature_review.py'
Sin dependencias ni acceso a red.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIT = ROOT / "docs" / "literature"
EXPECTED = [
    "01-vijayakumar-2025-india.md",
    "02-alqaryouti-2024-dubai.md",
    "03-chan-ng-chung-2023-hong-kong.md",
    "04-alwanin-2026-dxgba.md",
    "05-morgero-macedo-2025-articulo-17.md",
    "06-bayona-2025-transposicion-hs.md",
    "07-kim-kim-choi-2025-the-rag.md",
    "08-outram-swartz-2026-fronteras.md",
    "09-brinkmann-baumann-bizer-2024-wdc-pave.md",
    "10-brinkmann-shraga-bizer-2024-extractgpt.md",
    "11-lee-et-al-2024-explainable-customs.md",
    "12-lee-et-al-2021-sentences-retrieval.md",
    "13-ravi-et-al-text2trade-mnrl-mcd.md",
    "14-pain-2021-clasificacion-transfer-learning.md",
    "15-yang-et-al-2025-hscodecomp.md",
]


class LiteratureReviewTest(unittest.TestCase):
    def test_complete_set_and_main_index(self):
        self.assertTrue((LIT / "README.md").exists())
        actual = sorted(x.name for x in LIT.glob("*.md") if x.name != "README.md")
        self.assertEqual(actual, EXPECTED)
        index = (LIT / "README.md").read_text(encoding="utf-8")
        for name in EXPECTED:
            self.assertIn(name, index)
        self.assertIn("Cuadro comparativo general", index)
        self.assertIn("Cuadro de contribuciones científicas", index)
        self.assertNotIn("SIVEP", index)
        self.assertNotIn("decisiones de implementación", index)
        self.assertIn("quince", index.lower())
        for number in range(1, 16):
            self.assertIn(f"### 2.{number}.", index)
            self.assertIn(f"| **{number}** |", index)
            self.assertIn(f"| {number} |", index)
        root = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("docs/literature/README.md", root)

    def test_each_review_has_substantial_content_and_limitations(self):
        for name in EXPECTED:
            with self.subTest(article=name):
                text = (LIT / name).read_text(encoding="utf-8")
                self.assertGreater(len(text.split()), 650)
                self.assertIn("## ", text)
                self.assertTrue(any(v in text.lower() for v in ("doi", "arxiv", "working paper", "manuscrito", "tesis")), f"Falta tipo o referencia bibliográfica en {name}")
                self.assertTrue(
                    any(word in text.lower() for word in ("limitaciones", "límites", "validez"))
                )
                self.assertNotIn("SIVEP", text)
                self.assertNotRegex(text.lower(), r"nuestro proyecto|nuestra investigación|experimentos propios|propuestas propias")
                sections = [int(n) for n in re.findall(r"^## (\d+)\.", text, flags=re.MULTILINE)]
                self.assertEqual(sections, list(range(1, len(sections) + 1)))

    def test_reproducibility_matrix_covers_each_study(self):
        index = (LIT / "README.md").read_text(encoding="utf-8")
        self.assertIn("## 7. Reproducibilidad y disponibilidad de materiales", index)
        self.assertIn("## 8. Referencias bibliográficas", index)
        section = index.split(
            "## 7. Reproducibilidad y disponibilidad de materiales", 1
        )[1].split("## 8. Referencias bibliográficas", 1)[0]
        rows = re.findall(r"^\| \*\*(\d+)\*\* \|.+$", section, flags=re.MULTILINE)
        self.assertEqual([int(i) for i in rows], list(range(1, 16)))
        for term in ("Alta, condicionada", "Parcial", "Baja / no verificable", "No aplicable"):
            self.assertIn(term, section)
        self.assertIn("No se ha ejecutado ninguno", section)

    def test_internal_markdown_links_resolve(self):
        for path in [LIT / "README.md", *[LIT / x for x in EXPECTED]]:
            content = path.read_text(encoding="utf-8")
            for dest in re.findall(r"\]\(([^)]+)\)", content):
                target = dest.split("#", 1)[0].strip()
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                with self.subTest(file=path.name, destination=dest):
                    resolved = (path.parent / target).resolve()
                    self.assertTrue(resolved.is_file(), f"Broken link: {path} -> {target}")


if __name__ == "__main__":
    unittest.main()
