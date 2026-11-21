"""Pruebas sobre registro íntegro y modo restringido."""
import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "record_ai_interaction", ROOT / "scripts" / "record_ai_interaction.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TestRegisterInteraction(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        self.root = Path(self.t.name)
        self.prompt = self.root / "prompt.txt"
        self.answer = self.root / "response.txt"
        self.prompt.write_text("¿Es una mercancía comparable?", encoding="utf-8")
        self.answer.write_text("Requiere validación experta.", encoding="utf-8")

    def tearDown(self):
        self.t.cleanup()

    def args(self, *extra):
        return MODULE.parse_args([
            "--role", "auditor",
            "--provider", "TestIA",
            "--recorded-by", "test",
            "--prompt-file", str(self.prompt),
            "--response-file", str(self.answer),
            "--output-root", str(self.root),
            *extra,
        ])

    def test_public_requires_explicit_clearance(self):
        with self.assertRaises(ValueError):
            MODULE.record(self.args())

    def test_public_contains_full_prompt_and_answer(self):
        result = MODULE.record(self.args("--confirm-public-safe"))
        content = result.read_text(encoding="utf-8")
        self.assertIn("¿Es una mercancía comparable?", content)
        self.assertIn("Requiere validación experta.", content)
        self.assertIn("Clasificación: PUBLIC", content)
        self.assertIn("## Prompt completo", content)
        self.assertIn("## Respuesta completa visible", content)

    def test_restricted_omits_the_content(self):
        result = MODULE.record(self.args(
            "--confidentiality", "restricted",
            "--custody-ref", "institucional:expediente-interno-001",
        ))
        content = result.read_text(encoding="utf-8")
        self.assertNotIn("¿Es una mercancía comparable?", content)
        self.assertNotIn("Requiere validación experta.", content)
        self.assertIn("institucional:expediente-interno-001", content)

    def test_restricted_needs_custody_ref(self):
        with self.assertRaises(ValueError):
            MODULE.record(self.args("--confidentiality", "restricted"))

    def test_preserves_literal_code_fences(self):
        self.prompt.write_text("Una prueba con ````texto````", encoding="utf-8")
        result = MODULE.record(self.args("--confirm-public-safe"))
        content = result.read_text(encoding="utf-8")
        self.assertIn("Una prueba con ````texto````", content)
        self.assertIn("`````text", content)


if __name__ == "__main__":
    unittest.main()
