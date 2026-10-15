import subprocess
import sys


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "sorting_lab.cli", *args],
        capture_output=True,
        text=True,
        cwd=None,
    )


def test_cli_merge() -> None:
    proc = run_cli("5", "3", "8", "1", "--method", "merge")
    assert proc.returncode == 0
    assert "Merge Sort" in proc.stdout
    assert "Ordenado: [1, 3, 5, 8]" in proc.stdout


def test_cli_default_all() -> None:
    proc = run_cli("2", "1")
    assert proc.returncode == 0
    assert "Bubble Sort" in proc.stdout
    assert "Tim Sort" in proc.stdout


def test_cli_empty_stdin() -> None:
    proc = subprocess.run(
        [sys.executable, "-m", "sorting_lab.cli"],
        input="",
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0
    assert "Ordenado: []" in proc.stdout


def test_cli_non_integer_error() -> None:
    proc = run_cli("1", "abc")
    assert proc.returncode != 0
    assert proc.stderr


def test_cli_oversize_error() -> None:
    from sorting_lab.cli import main

    code = main([str(i) for i in range(10_001)])
    assert code != 0


def test_cli_unknown_method() -> None:
    proc = run_cli("1", "2", "--method", "radix")
    assert proc.returncode != 0
    assert proc.stderr
