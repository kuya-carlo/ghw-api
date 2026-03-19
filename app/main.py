"""Entry point for the GHW API."""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from .schemas import Challenge, ChallengeCreate, HealthCheck
from .storage import store


def create_app() -> FastAPI:
    app = FastAPI(
        title="GHW API",
        description="A lightweight API for MLH Global Hack Week.",
        version="0.1.0",
        openapi_tags=[
            {"name": "health", "description": "Health checks and runtime info."},
            {"name": "challenges", "description": "Endpoints to manage hack week challenges."},
        ],
    )

    @app.get("/", tags=["health"], response_model=HealthCheck)
    def root() -> HealthCheck:
        """Simple health endpoint."""
        return HealthCheck(uptime_seconds=store.uptime_seconds())

    @app.get("/challenges", tags=["challenges"], response_model=list[Challenge])
    def list_challenges() -> list[Challenge]:
        """List all available challenges."""
        return store.list()

    @app.get(
        "/challenges/{challenge_id}",
        tags=["challenges"],
        response_model=Challenge,
        responses={404: {"description": "Challenge not found."}},
    )
    def get_challenge(challenge_id: int) -> Challenge:
        """Retrieve a single challenge by ID."""
        challenge = store.get(challenge_id)
        if challenge is None:
            raise HTTPException(status_code=404, detail="Challenge not found")
        return challenge

    @app.post(
        "/challenges",
        tags=["challenges"],
        response_model=Challenge,
        status_code=201,
    )
    def create_challenge(payload: ChallengeCreate) -> Challenge:
        """Create a new challenge."""
        return store.create(payload)

    @app.get("/debug", include_in_schema=False)
    def debug() -> JSONResponse:
        # Simple debug info (not meant for production)
        payload = {
            "uptime_seconds": store.uptime_seconds(),
            "challenges_count": len(store.list()),
        }
        return JSONResponse(content=payload)

    return app


app = create_app()
