from enum import Enum
from collections import namedtuple
from conf import settings

ServiceModel = namedtuple('Service', ['name', 'base_url'])


class Service(Enum):
    BUSINESS = ServiceModel('BUSINESS', settings.env.str('BUSINESS_URL'))
