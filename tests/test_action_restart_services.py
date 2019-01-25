import mock

from tests.lib.action import InfobloxBaseActionTestCase
from restart_services import RestartAllMemberServicesAction


class RestartServicesTestCase(InfobloxBaseActionTestCase):
    __test__ = True
    action_cls = RestartAllMemberServicesAction

    def test_restart_member_services(self):
        action = self.get_action_instance(self.full_config)

        # This assumes that the result of get_object doens't contain reference of member
        action.connection.get_object = mock.Mock(return_value=[
            {'ref': 'foo'},
            {'result': 'invalid_data'},
            None
        ])

        # Setting side_effect which pass through the parameters to check whether they are
        # passed it expectedly.
        def side_effect(**kwargs):
            return kwargs

        action.connection.call_func = mock.Mock(side_effect=side_effect)

        result = action.run()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['ref'], 'foo')
