from fastapi import APIRouter, HTTPException

from sorting_lab.api.schemas import (
    HealthResponse,
    MethodInfo,
    MethodsResponse,
    SortRequest,
    SortResponse,
    SortResultItem,
)
from sorting_lab.sorting.engine import SequenceValidationError, sort_sequence
from sorting_lab.sorting.registry import METHOD_IDS, METHOD_NAMES

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Verificação de saúde",
)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@router.get(
    "/methods",
    response_model=MethodsResponse,
    summary="Listar algoritmos",
)
def methods() -> MethodsResponse:
    return MethodsResponse(
        methods=[
            MethodInfo(id=method_id, name=METHOD_NAMES[method_id])
            for method_id in METHOD_IDS
        ]
    )


@router.post(
    "/sort",
    response_model=SortResponse,
    summary="Ordenar sequência",
)
def sort_numbers(body: SortRequest) -> SortResponse:
    try:
        runs = sort_sequence(body.sequence, body.method)
    except SequenceValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

    return SortResponse(
        results=[
            SortResultItem(
                method=run.method,
                sorted=run.sorted,
                time_ms=run.time_ms,
                comparisons=run.comparisons,
                swaps=run.swaps,
            )
            for run in runs
        ]
    )
