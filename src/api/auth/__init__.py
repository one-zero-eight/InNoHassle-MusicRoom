__all__ = ["router"]

from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

import src.api.auth.routes  # noqa: E402, F401
