try:
    from infoblox_client import connector
except ImportError:
    message = ('Missing "infoblox-client", please install it using pip:\n'
               'pip install infoblox-client')
    raise ImportError(message)

from st2common.runners.base_action import Action

__all__ = [
    'InfobloxBaseAction',
]


class InfobloxConnector(connector.Connector):
    CONVERTING_KEY_MAP = {
        '_ref': 'ref'
    }

    def _inspect_and_interchane_dict(self, dict_value):
        if not isinstance(dict_value, dict):
            # When non-dict value is specified, this returns it without inspection
            return dict_value

        for key in dict_value.keys():
            # This routine also inspect every leaf elements.
            if isinstance(dict_value[key], dict):
                dict_value[key] = self._inspect_and_interchane_dict(dict_value[key])
            elif isinstance(dict_value[key], list):
                dict_value[key] = [self._inspect_and_interchane_dict(x) for x in dict_value[key]]

            # This detoxifies returned value when returned value has harmful key-value pairs
            # for st2 (e.g. '_ref' key)
            if key in self.CONVERTING_KEY_MAP:
                dict_value[self.CONVERTING_KEY_MAP[key]] = dict_value.pop(key)

        return dict_value

    def get_object(self, *args, **kwargs):
        """
        The original method returns dict value that st2 doens't take care (e.g. '_ref'
        key-value pairs). This method interchanges this key to another harmless one.
        """
        results = super(InfobloxConnector, self).get_object(*args, **kwargs)

        # The get_object method of infoblox-client returns list of Infoblox objects.
        # But when there is no Infoblox object to be returned, this method returns None.
        if isinstance(results, list):
            return [self._inspect_and_interchane_dict(x) for x in results]
        else:
            return results


class InfobloxBaseAction(Action):
    def __init__(self, config):
        super(InfobloxBaseAction, self).__init__(config)
        _hostname = self.config['hostname']
        _username = self.config['username']
        _password = self.config['password']

        opts = {
            'host': _hostname,
            'username': _username,
            'password': _password,
            'ssl_verify': self.config['verify_ssl'],
            'silent_ssl_warnings': (not self.config['verify_ssl'])
        }

        self.connection = InfobloxConnector(opts)
