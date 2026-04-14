"""In-memory storage for challenges."""

from __future__ import annotations

from threading import Lock
from time import monotonic
from typing import Dict, List, Optional

from .schemas import Challenge, ChallengeCreate, Difficulty


class ChallengeStore:
    """An in-memory store for challenges.

    This is intentionally simple to keep the stack small for MLH Hack Week.
    """

    def __init__(self) -> None:
        self._lock = Lock()
        self._next_id = 1
        self._challenges: Dict[int, Challenge] = {}
        self._start = monotonic()
        self._seed_default_challenge()

    def _seed_default_challenge(self) -> None:
        self.create(
            ChallengeCreate(
                title="Welcome challenge",
                description="Create your first challenge by posting to /challenges.",
                difficulty=Difficulty.easy,
                tags=["demo", "starter"],
                published=True,
            )
        )

    def uptime_seconds(self) -> float:
        return monotonic() - self._start

    def list(self) -> List[Challenge]:
        return list(self._challenges.values())

    def get(self, challenge_id: int) -> Optional[Challenge]:
        return self._challenges.get(challenge_id)

    def create(self, payload: ChallengeCreate) -> Challenge:
        with self._lock:
            cid = self._next_id
            self._next_id += 1
            challenge = Challenge(id=cid, **payload.model_dump())
            self._challenges[cid] = challenge
            return challenge


store = ChallengeStore()
