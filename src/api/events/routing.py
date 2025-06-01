from fastapi import APIRouter
import os
from .schemas import (
    EventSchema,
    EventListScheme,
    EventCreateSchema,
    EventUploadSchema,
    )
router = APIRouter()
from api.db.config import DATABASE_URL
# GET DATA HERE
#List View
@router.get("/")
def read_events() -> EventListScheme:
    print(os.environ.get("DATABASE_URL"), DATABASE_URL)
    return {
        "results": [
            {"id": 1}, {"id": 3}, {"id": 2, }
        ],
        "count": 3
    }

# SEND DATA HERE
# Create View
# POST /api/events
@router.post("/")
def create_event(payload: EventCreateSchema) -> EventSchema:
    data = payload.model_dump() #payload -> dict -> pydantic
    return {"id": 123, **data}


@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    # a single row
    return {"id": event_id}


@router.put("/{event_id}")
def update_event(event_id: int, payload: EventUploadSchema) -> EventSchema:
    # a single row
    print(payload.descriptions)
    return {"id": event_id}