from request import Request
from route import RouteController
from user import User


# sdk类
class Sdk(RouteController):

    def __init__(self, user: User):
        self._user = user

    def setHost(self, host: str):
        self._host = host
