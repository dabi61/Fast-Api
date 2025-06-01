# from pydantic import BaseModel, Field
from sqlmodel import SQLModel, Field
from typing import List, Optional


class EventModel(SQLModel, table=True):  #table= True
    id: Optional[int] = Field(default=None, primary_key=True)
    # id: int
    page: Optional[str] = None  #Optional Khong bat buoc mac dinh la chuoi rong
    descriptions: Optional[str] = None


class EventListScheme(SQLModel):
    results: List[EventModel]
    count: int

class EventCreateSchema(SQLModel):
    path: str
    desscription: Optional[str] = Field(default="my description") #Field de hien thi ngoai scheme doc

class EventUploadSchema(SQLModel):
    descriptions: str