import mock

from infoblox_client import exceptions
from tests.lib.action import InfobloxBaseActionTestCase
from update_object import UpdateObjectAction


class UpdateObjectTestCase(InfobloxBaseActionTestCase):
    __test__ = True
    action_cls = UpdateObjectAction

    def test_update_object(self):
        action = self.get_action_instance(self.full_config)

        def side_effect(ref, payload):
            return payload
        action.connection.update_object = mock.Mock(side_effect=side_effect)

        # run action and check expected values are returned
        (is_success, result) = action.run('ref', {'hoge': 'fuga', 'foo': None})
        self.assertTrue(is_success)
        self.assertEqual(result, {'hoge': 'fuga'})

    def test_update_object_with_cannnot_update_exception(self):
        action = self.get_action_instance(self.full_config)

        # When user specifies invalid ref value, infoblox-client raises
        # InfobloxCannotUpdateObject exception.
        def side_effect(ref, payload):
            raise exceptions.InfobloxCannotUpdateObject(**{
                'response': {'result': 'fail'},
                'ref': ref,
                'content': 'hoge',
                'code': 400
            })
        action.connection.update_object = mock.Mock(side_effect=side_effect)

        (is_success, result) = action.run('ref', {'hoge': 'fuga', 'foo': None})
        self.assertFalse(is_success)
        self.assertEqual(str(result), 'Cannot update object with ref ref: hoge [code 400]')
