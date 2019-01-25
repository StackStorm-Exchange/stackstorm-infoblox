from infoblox_client import exceptions
from lib.action import InfobloxBaseAction

__all__ = [
    'UpdateObjectAction',
]


class UpdateObjectAction(InfobloxBaseAction):
    def run(self, ref, payload):
        _keys = list(payload.keys())
        for k in _keys:
            if payload[k] is None:
                del payload[k]

        try:
            result = self.connection.update_object(ref, payload)
        except exceptions.InfobloxException as e:
            return (False, e)

        return (True, result)
