import mock

from create_object import CreateObjectAction
from infoblox_client import exceptions
from tests.lib.action import InfobloxBaseActionTestCase


class CreateObjectTestCase(InfobloxBaseActionTestCase):
    __test__ = True
    action_cls = CreateObjectAction

    def test_create_object(self):
        action = self.get_action_instance(self.full_config)

        action.connection = mock.Mock()
        action.connection.create_object.return_value = 'result'

        (is_success, value) = action.run(object_type='record:host', name='name', ipv4addrs=[])
        self.assertTrue(is_success)
        self.assertEqual(value, 'result')

    def test_create_object_with_exception(self):
        action = self.get_action_instance(self.full_config)

        def side_effect(*args, **kwargs):
            raise exceptions.InfobloxCannotCreateObject(
                response={'Error': 'Message'},
                obj_type='object_type',
                content='hoge',
                args={},
                code=400)

        action.connection = mock.Mock()
        action.connection.create_object.side_effect = side_effect

        (is_success, value) = action.run(object_type='record:host', name='name', ipv4addrs=[])
        self.assertFalse(is_success)
        self.assertEqual(value, {'Error': 'Message'})
