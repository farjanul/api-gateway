from rest_framework.exceptions import ParseError

from apps.apigateway.service.service import Service


class Config:

    def __init__(self, service: str):
        self.service = service

    def get(self) -> tuple[str, str]:
        if self.service and self.service.upper() == Service.BUSINESS.value.name:
            return Service.BUSINESS.value.name, Service.BUSINESS.value.base_url

        raise ParseError({'message': 'Unknown service request'})

