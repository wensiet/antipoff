from repositories.abstract_repository import MongoRepository
from database import REQUEST
from schemas import RequestSchema


class RequestsRepository(MongoRepository):
    model = REQUEST
    schema = RequestSchema
