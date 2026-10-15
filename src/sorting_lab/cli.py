import argparse
import sys

from sorting_lab.sorting.engine import SequenceValidationError, sort_sequence
from sorting_lab.sorting.registry import METHOD_NAMES


def _parse_tokens(tokens: list[str]) -> list[int]:
    if not tokens:
        raw = sys.stdin.read()
        if not raw.strip():
            return []
        tokens = raw.split()
    values: list[int] = []
    for token in tokens:
        try:
            if "." in token or "e" in token.lower():
                raise ValueError
            values.append(int(token))
        except ValueError as exc:
            raise SequenceValidationError(
                f"Valor inválido (esperado inteiro): {token!r}"
            ) from exc
    return values


def _expand_args(sequence_args: list[str]) -> list[str]:
    tokens: list[str] = []
    for arg in sequence_args:
        tokens.extend(arg.split())
    return tokens


def _format_swaps(swaps: int | None) -> str:
    return "-" if swaps is None else str(swaps)


def _print_table(results) -> None:
    col_method = 12
    col_time = 12
    col_comp = 13
    col_swaps = 7
    header = (
        f"{'Método':<{col_method}}"
        f"{'Tempo (ms)':>{col_time}}"
        f"{'Comparações':>{col_comp}}"
        f"{'Trocas':>{col_swaps}}"
    )
    sep = "─" * (col_method + col_time + col_comp + col_swaps)
    print(header)
    print(sep)
    for run in results:
        label = METHOD_NAMES.get(run.method, run.method)
        print(
            f"{label:<{col_method}}"
            f"{run.time_ms:>{col_time}.3f}"
            f"{run.comparisons:>{col_comp}}"
            f"{_format_swaps(run.swaps):>{col_swaps}}"
        )
    if results:
        print(f"\nOrdenado: {results[0].sorted}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Ordena uma sequência de inteiros com algoritmos clássicos.",
    )
    parser.add_argument(
        "sequence",
        nargs="*",
        help='Inteiros separados por espaço ou string "5 3 8 1"',
    )
    parser.add_argument(
        "--method",
        default="all",
        help="bubble, selection, insertion, merge, quick, heap, tim ou all",
    )
    args = parser.parse_args(argv)

    try:
        tokens = _expand_args(args.sequence)
        sequence = _parse_tokens(tokens)
        results = sort_sequence(sequence, args.method)
    except SequenceValidationError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    _print_table(results)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
