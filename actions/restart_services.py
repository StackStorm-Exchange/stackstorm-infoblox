from lib.action import InfobloxBaseAction

__all__ = [
    'RestartAllMemberServicesAction',
]


class RestartAllMemberServicesAction(InfobloxBaseAction):
    def run(self):
        return [self.connection.call_func(**{
            'func_name': 'restartservices',
            'ref': x['_ref'],
            'payload': {
                'restart_option': 'RESTART_IF_NEEDED',
                'service_option': 'ALL'
            }
        }) for x in self.connection.get_object('member') if x and '_ref' in x]
