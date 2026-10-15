from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

MethodId = Literal[
    "all",
    "bubble",
    "selection",
    "insertion",
    "merge",
    "quick",
    "heap",
    "tim",
]


class HealthResponse(BaseModel):
    status: str


class MethodInfo(BaseModel):
    id: str
    name: str


class MethodsResponse(BaseModel):
    methods: list[MethodInfo]


class SortRequest(BaseModel):
    sequence: list[int] = Field(
        default_factory=list,
        max_length=10_000,
        description="Sequência de inteiros a ordenar",
    )
    method: MethodId = Field(
        default="all",
        description="Algoritmo ou 'all' para comparar os sete",
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {"sequence": [5, 3, 8, 1, 9, 2], "method": "all"}
        }
    )


class SortResultItem(BaseModel):
    method: str
    sorted: list[int]
    time_ms: float
    comparisons: int
    swaps: int | None


class SortResponse(BaseModel):
    results: list[SortResultItem]
