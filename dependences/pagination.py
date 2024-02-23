from typing import Annotated

from fastapi import Depends, Query
from pydantic import BaseModel


class PaginationParams(BaseModel):
    offset: int
    limit: int


def get_pagination_params(
    page: int = Query(1, ge=1), page_size: int = Query(10, ge=1, le=100)
) -> PaginationParams:
    offset = (page - 1) * page_size
    limit = page_size
    return PaginationParams(offset=offset, limit=limit)


PaginationDeps = Annotated[PaginationParams, Depends(get_pagination_params)]
