from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Difficulty(str, Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"


class Challenge(BaseModel):
    id: int
    title: str = Field(..., example="Build a TODO API")
    description: str
    difficulty: Difficulty = Difficulty.easy
    tags: list[str] = Field(default_factory=list)
    published: bool = True


class ChallengeCreate(BaseModel):
    title: str = Field(..., example="Build a TODO API")
    description: str
    difficulty: Difficulty = Difficulty.easy
    tags: list[str] = Field(default_factory=list)
    published: Optional[bool] = True


class HealthCheck(BaseModel):
    status: str = Field("ok", example="ok")
    uptime_seconds: float
