from fastapi import APIRouter
from .schemas import EventSchema
router = APIRouter()

@router.get("/")
def read_events():
    return {
        "item": [1,2,3]
    }

@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    # a single row
    return {"id": event_id}