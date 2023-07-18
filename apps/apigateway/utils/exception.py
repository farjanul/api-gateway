from rest_framework.exceptions import APIException


class ServiceServerException(APIException):
    def __init__(self, message):
        super().__init__(message)

    status_code = 500
