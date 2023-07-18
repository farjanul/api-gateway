import requests

from apps.apigateway.service.microservice import MicroService
from apps.apigateway.utils.exception import ServiceServerException


class APIGateway:

    def __init__(self, request):
        self.__host = request.get_host()
        self.__method = request.method
        self.__full_path = request.get_full_path()
        self.__headers = request.headers
        __microservice = MicroService(request)
        self.__service_url = __microservice.get_service_url()
        self.__service_name = __microservice.get_service_name()

    def forward_request(self, data=None):
        try:
            headers = {
                'Authorization': self.__headers['Authorization'],
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                # 'Host': self.__host,
            }
            response = requests.request(self.__method, self.__service_url + self.__full_path, headers=headers, data=data)
        except Exception as _:
            raise ServiceServerException({'message': f"{self.__service_name} - service server error {_}"})
        return response

    @staticmethod
    def __get_auth_headers(request):
        # Extract the JWT token from the request
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]

        # Set the JWT token in the Authorization header of the backend API request
        return {'Authorization': 'Bearer ' + token}
