import abc


class BaseService(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_service_name(self):
        pass

    @abc.abstractmethod
    def get_service_url(self):
        pass
