from infoblox_client import exceptions
from lib.action import InfobloxBaseAction

__all__ = [
    'CreateObjectAction',
]


class CreateObjectAction(InfobloxBaseAction):
    def run(self, object_type, **kwargs):
        try:
            return (True, self.connection.create_object(object_type, kwargs))
        except exceptions.InfobloxCannotCreateObject as e:
            return (False, e.response)
