"""Verifica que ninguna instrucción operativa se active durante CONFIGURACIÓN."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class AgentActivationPolicyTest(unittest.TestCase):
    def text(self, relative):
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_role_prompts_guard_against_implicit_activation(self):
        for name in ("COORDINATOR", "DEVELOPER", "AUDITOR"):
            with self.subTest(role=name):
                content = self.text(f"prompts/{name}.md")
                self.assertIn("Condición de activación formal", content)
                self.assertIn("CONFIGURACIÓN", content)
                self.assertIn("OPERACIÓN", content)
                self.assertIn("orden expresa", content)
                self.assertIn("SOLO EN OPERACIÓN", content)

    def test_no_formal_sessions_listed_before_activation(self):
        index = self.text("docs/operations/SESSION_INDEX.md")
        self.assertIn("Sin sesiones operativas", index)
        self.assertIn("NO sesiones operativas", index)
        self.assertIn("coord-20261121-001", index)

    def test_historical_records_are_marked_pre_activation(self):
        for idx in range(1, 7):
            with self.subTest(log=idx):
                text = self.text(f"docs/ai-logs/2026-11-21/coordinator-{idx:04}.md")
                self.assertIn("RECTIFICACIÓN RETROSPECTIVA", text)
                self.assertIn("CONFIGURACIÓN", text)
        for idx in range(1, 4):
            with self.subTest(checkpoint=idx):
                text = self.text(
                    "docs/operations/checkpoints/2026-11-21/"
                    f"coord-20261121-001-CP{idx:02}.md"
                )
                self.assertIn("RECTIFICACIÓN RETROSPECTIVA", text)

    def test_policy_separates_configuration_from_operation(self):
        activation = self.text("docs/operations/ACTIVATION_PROTOCOL.md")
        self.assertIn("CONFIGURACIÓN", activation)
        self.assertIn("OPERACIÓN", activation)
        self.assertIn("responde", activation)
        self.assertIn("activación", self.text("docs/decisions/ADR-0008-AGENT-ACTIVATION.md"))


if __name__ == "__main__":
    unittest.main()
