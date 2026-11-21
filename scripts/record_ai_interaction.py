#!/usr/bin/env python3
"""Registrar un intercambio visible de IA en la bitácora versionable.

Nunca conecta con servicios externos, no extrae conversaciones y no garantiza
que un texto sea seguro para publicación: la comprobación humana es obligatoria.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
import re
import sys
import uuid


ROLES = ("coordinator", "developer", "auditor")
CONFIDENTIALITY = ("public", "restricted")


def parse_args(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--role", choices=ROLES, required=True)
    p.add_argument("--provider", required=True)
    p.add_argument("--model", default="not-documented")
    p.add_argument("--issue", default="not-assigned")
    p.add_argument("--base-commit", default="not-documented")
    p.add_argument("--recorded-by", required=True)
    p.add_argument("--prompt-file", type=Path, required=True)
    p.add_argument("--response-file", type=Path, required=True)
    p.add_argument("--confidentiality", choices=CONFIDENTIALITY, default="public")
    p.add_argument("--confirm-public-safe", action="store_true")
    p.add_argument("--custody-ref", default="")
    p.add_argument("--previous-interaction", default="none")
    p.add_argument("--output-root", type=Path, default=Path(__file__).resolve().parents[1])
    return p.parse_args(argv)


def safe_metadata(value: str) -> str:
    # Metadata uses one Markdown line, not user-controlled Markdown structures.
    return re.sub(r"[\r\n]+", " ", value).strip()


def fenced(value: str) -> str:
    runs = [len(x) for x in re.findall(r"`+", value)]
    fence = "`" * max(4, max(runs, default=0) + 1)
    return f"{fence}text\n{value}\n{fence}"


def record(args) -> Path:
    if args.confidentiality == "public" and not args.confirm_public_safe:
        raise ValueError("La publicación íntegra requiere --confirm-public-safe tras revisar confidencialidad.")
    if args.confidentiality == "restricted" and not args.custody_ref:
        raise ValueError("Un registro restringido requiere --custody-ref de custodia institucional autorizada.")

    # Se leen para comprobar que ambos artefactos existen; en el modo restringido
    # su contenido NO se transfiere al archivo público.
    prompt = args.prompt_file.read_text(encoding="utf-8")
    response = args.response_file.read_text(encoding="utf-8")
    if not prompt.strip() or not response.strip():
        raise ValueError("El prompt y la respuesta visible no pueden estar vacíos.")

    now = datetime.now(timezone.utc)
    identifier = now.strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:10]
    directory = args.output_root / "docs" / "ai-logs" / now.strftime("%Y-%m-%d")
    path = directory / f"{identifier}.md"

    meta = [
        f"# Interacción {identifier}",
        "",
        f"- Fecha UTC: {now.isoformat(timespec='seconds')}",
        f"- Rol: {safe_metadata(args.role)}",
        f"- Proveedor: {safe_metadata(args.provider)}",
        f"- Modelo: {safe_metadata(args.model)}",
        f"- Issue/tarea: {safe_metadata(args.issue)}",
        f"- Commit base: {safe_metadata(args.base_commit)}",
        f"- Registrado por: {safe_metadata(args.recorded_by)}",
        f"- Interacción anterior: {safe_metadata(args.previous_interaction)}",
        f"- Clasificación: {args.confidentiality.upper()}",
        "",
    ]
    if args.confidentiality == "public":
        meta += [
            "## Prompt completo",
            "",
            fenced(prompt),
            "",
            "## Respuesta completa visible",
            "",
            fenced(response),
            "",
            "## Resultados y verificación",
            "",
            "Pendiente de enlazar a commits/PR y pruebas según corresponda.",
        ]
    else:
        meta += [
            "## Custodia del intercambio íntegro",
            "",
            "Texto original restringido: NO PUBLICADO en GitHub.",
            f"Referencia autorizada de custodia: {safe_metadata(args.custody_ref)}",
            "Responsable de validar integridad y accesos: registrado por (ver metadatos).",
            "",
            "## Resultados y verificación",
            "",
            "Pendiente de enlazar a commits/PR sin divulgar contenido sensible.",
        ]
    directory.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(meta) + "\n", encoding="utf-8")
    return path


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        path = record(args)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"Registro creado: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
