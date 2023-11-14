import random
import time
from fastapi import HTTPException

from repositories import RequestsRepository
from schemas import InputRequestSchema, RequestSchema


class RequestsService:

    def __init__(self, request_repository: RequestsRepository):
        self.repository = request_repository

    @staticmethod
    def _validate_input_request_schema(input_form: InputRequestSchema):
        if -90 <= input_form.latitude <= 90 and -180 <= input_form.longitude <= 180:
            return True
        return False

    async def accept_request(self, input_form: InputRequestSchema):
        if not RequestsService._validate_input_request_schema(input_form):
            raise HTTPException(400, {"message": "Latitude or longitude is incorrect"})
        wait_time = random.randint(0, 5)
        external_service_answer = bool(random.randint(0, 1))
        print(f"External service request emulation (time = {wait_time}sec) with result {external_service_answer}")
        resulting_schema = RequestSchema(cadastrial=input_form.cadastrial,
                                         latitude=input_form.latitude,
                                         longitude=input_form.longitude,
                                         result=external_service_answer)
        await self.repository.add_one(resulting_schema)
        time.sleep(wait_time)
        return external_service_answer

    async def get_requests_history(self):
        return await self.repository.find_many()
