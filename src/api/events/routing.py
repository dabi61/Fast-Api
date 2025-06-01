from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from api.db.session import get_session
import os



from .model import (
    EventModel,
    EventListScheme,
    EventCreateSchema,
    EventUploadSchema,
    )
router = APIRouter()
from api.db.config import DATABASE_URL
# GET DATA HERE
#List View
@router.get("/", response_model=EventListScheme)
def read_events(session: Session = Depends(get_session)):
    query = select(EventModel)
    results = session.exec(query).all()
    return {
        "results": results,
        "count": len(results)
    }

# SEND DATA HERE
# Create View
# POST /api/events
@router.post("/", response_model=EventModel)
def create_event(
    payload: EventCreateSchema,
    session: Session = Depends(get_session)):
    data = payload.model_dump() #payload -> dict -> pydantic
    obj = EventModel.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj


@router.get("/{event_id}", response_model=EventModel)
def get_event(event_id: int, session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    results = session.exec(query).first()
    if not results:
        raise HTTPException(status_code=404, detail="Event Not Found")
    # a single row
    return results


@router.put("/{event_id}", response_model=EventModel)
def update_event(
    event_id: int,
    payload: EventUploadSchema,
    session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    obj = session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Event Not Found")

    data = payload.model_dump()
    for k, v in data.items():
        # if k == 'id':  #Mo len de tranh cap nhat field id Nhung minh thiet ke payload kia thi khong can thiet
        #     continue
        setattr(obj, k, v)

    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj

