from pydantic import BaseModel
from bson import ObjectId


class RequestSchema(BaseModel):
    _id: ObjectId = None
    cadastrial: str
    latitude: float
    longitude: float
    result: bool


class InputRequestSchema(BaseModel):
    cadastrial: str
    latitude: float
    longitude: float
