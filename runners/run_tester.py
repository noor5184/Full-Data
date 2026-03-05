"""
-------------------------------------------------------
[Run any CP164 tester from the repo root while emulating the IDE "referenced project" path. Usage (from repo root):python runners/run_tester.py coursework/noor5184_a03/src/t05.py]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2024-09-11"
-------------------------------------------------------
"""
# Imports
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
# Constants

def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """
"""

"""



def run_tester(script_rel_path: str) -> int:
    root = Path(__file__).resolve().parents[1]
    script_path = (root / script_rel_path).resolve()
    ds_src = (root / "noor5184_data_structures" / "src").resolve()

    if not script_path.exists():
        print(f"Tester not found: {script_path}")
        return 2

    if not ds_src.exists():
        print(f"Data structures src not found: {ds_src}")
        return 2

    env = dict(os.environ)
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = str(ds_src) if existing == "" else str(ds_src) + os.pathsep + existing

    print(f"Running: {script_path}")
    print(f"PYTHONPATH: {env['PYTHONPATH']}")

    proc = subprocess.run([sys.executable, str(script_path)], cwd=str(script_path.parent), env=env)
    return int(proc.returncode)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python runners\\run_tester.py <relative path to tester .py>")
        return 2
    return run_tester(argv[1])


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))