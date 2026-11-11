#!/usr/bin/env python3
# Copyright 2026 Google LLC.
# SPDX-License-Identifier: Apache-2.0

"""Build an isolated ChatGPT web archive from canonical EGM skills."""

import argparse
import importlib.util
import json
from pathlib import Path
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    output = parser.parse_args().output.resolve()
    archive = output / "egm-full-lite-preview.zip"
    if archive.exists():
        raise SystemExit(f"Refusing to overwrite {archive}")

    spec = importlib.util.spec_from_file_location(
        "egm_pack_plugin", ROOT / "scripts/pack_plugin.py"
    )
    if spec is None or spec.loader is None:
        raise SystemExit("Could not load the canonical EGM packager")
    packer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(packer)

    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="egm-full-lite-") as temporary:
        runtime, _ = packer.build(ROOT, "openai", Path(temporary))
        manifest = json.loads((SOURCE / "plugin.json").read_text(encoding="utf-8"))
        manifest_path = runtime / "plugin.json"
        manifest_path.write_text(
            json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
        )
        host_manifest = runtime / ".codex-plugin/plugin.json"
        host_manifest.unlink()
        lite = runtime / "skills/egm-lite/SKILL.md"
        lite.parent.mkdir(parents=True)
        lite.write_bytes((SOURCE / "skills/egm-lite/SKILL.md").read_bytes())

        with zipfile.ZipFile(archive, "x", zipfile.ZIP_DEFLATED) as bundle:
            for path in sorted(runtime.rglob("*")):
                if path.is_file():
                    bundle.write(path, path.relative_to(runtime))

    with zipfile.ZipFile(archive) as bundle:
        names = set(bundle.namelist())
        assert "plugin.json" in names
        assert ".codex-plugin/plugin.json" not in names
        assert "skills/egm-lite/SKILL.md" in names
        assert all(f"skills/{name}/SKILL.md" in names for name in packer.SKILLS)
        packaged = json.loads(bundle.read("plugin.json"))
        assert "requires_local_executor" not in packaged.get(
            "extensions", {}
        ).get("com.openai", {})
    print(f"Created {archive}")


if __name__ == "__main__":
    main()
