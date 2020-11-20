from safecustody_sdk.route import RouteController
from safecustody_sdk.user import User


# sdk类
class Sdk(RouteController):

    def __init__(self, user: User):
        self._user = user

    def setHost(self, host: str):
        self._host = host
