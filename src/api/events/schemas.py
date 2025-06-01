from pydantic import BaseModel, Field
from typing import List, Optional


class EventSchema(BaseModel):
    id: int
    page: Optional[str] = None  #Optional Khong bat buoc mac dinh la chuoi rong
    descriptions: Optional[str] = None


class EventListScheme(BaseModel):
    results: List[EventSchema]
    count: int

class EventCreateSchema(BaseModel):
    path: str
    desscription: Optional[str] = Field(default="my description") #Field de hien thi ngoai scheme doc

class EventUploadSchema(BaseModel):
    descriptions: str