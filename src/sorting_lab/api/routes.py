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
from sorting_lab.sorting.registry import list_method_meta

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
            MethodInfo(
                id=meta.id,
                name=meta.name,
                complexity_best=meta.complexity_best,
                complexity_average=meta.complexity_average,
                complexity_worst=meta.complexity_worst,
                stable=meta.stable,
                blurb=meta.blurb,
            )
            for meta in list_method_meta()
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
