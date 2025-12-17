from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass
class AgentTools:
    project_path: Path

    def _safe_path(self, rel_path: str) -> Path:
        root = self.project_path.resolve()
        p = (root / rel_path).resolve()
        if root not in p.parents and p != root:
            raise ValueError("Path is outside the project folder.")
        return p

    def read_file(self, rel_path: str) -> str:
        path = self._safe_path(rel_path)
        return path.read_text(encoding="utf-8")

    def write_file(self, rel_path: str, content: str) -> str:
        path = self._safe_path(rel_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return f"Wrote {len(content)} characters to {rel_path}"

    def run_bash(self, command: str) -> str:
        blocked = ["runserver", "python manage.py runserver", "make run"]
        if any(b in command for b in blocked):
            return "Blocked: runserver commands are not allowed from the agent."

        result = subprocess.run(
            command,
            cwd=str(self.project_path.resolve()),
            shell=True,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            return f"ERROR:\n{result.stderr}"

        return result.stdout or "OK"

    def list_files(self, rel_path: str = ".") -> list[str]:
        root = self.project_path.resolve()
        path = self._safe_path(rel_path)

        if not path.exists():
            return []

        return sorted(
            str(p.relative_to(root))
            for p in path.rglob("*")
            if p.is_file()
        )

    def grep(self, pattern: str, rel_path: str = ".") -> list[str]:
        root = self.project_path.resolve()
        path = self._safe_path(rel_path)
        results = []

        for file in path.rglob("*"):
            if not file.is_file():
                continue

            try:
                for i, line in enumerate(
                    file.read_text(encoding="utf-8", errors="ignore").splitlines(),
                    start=1,
                ):
                    if pattern in line:
                        results.append(
                            f"{file.relative_to(root)}:{i}: {line.strip()}"
                        )
            except Exception:
                continue

        return results
