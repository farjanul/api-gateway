from apps.apigateway.service.base_service import BaseService

from apps.apigateway.service.config import Config


class MicroService(BaseService):

    def __init__(self, request):
        self.__request_service_name = request.META.get('HTTP_SERVICE')
        self.__config = Config(self.__request_service_name).get()

    def get_service_name(self):
        return self.__config[0]

    def get_service_url(self):
        return self.__config[1]
