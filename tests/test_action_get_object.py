import mock

from get_object import GetObjectAction
from tests.lib.action import InfobloxBaseActionTestCase


class GetObjectTestCase(InfobloxBaseActionTestCase):
    __test__ = True
    action_cls = GetObjectAction

    def test_get_object_that_has_malformed_value(self):
        action = self.get_action_instance(self.full_config)
        check_values = [
            {
                # The case malformed key is in a top level dict value.
                'raw': [{'foo': 'bar', '_ref': 'foo'}, {'hoge': 'fuga'}],
                'exp': [{'foo': 'bar', 'ref': 'foo'}, {'hoge': 'fuga'}]
            },
            {
                # The case malformed key is in a internal dict value.
                'raw': [{'hoge': {'foo': 'bar', '_ref': 'bar'}}],
                'exp': [{'hoge': {'foo': 'bar', 'ref': 'bar'}}]
            },
            {
                # The case malformed key is in a internal list value.
                'raw': [{'fuga': [{'foo': 'bar'}, {'_ref': 'bar'}]}],
                'exp': [{'fuga': [{'foo': 'bar'}, {'ref': 'bar'}]}]
            },
            {
                # The case '_ref' string values in a list, these are harmless.
                'raw': [{'fuga': ['_ref', 'foo']}, '_ref'],
                'exp': [{'fuga': ['_ref', 'foo']}, '_ref'],
            },
            {
                # The case non-list value is returned.
                'raw': None,
                'exp': None,
            }
        ]

        for check_value in check_values:
            with mock.patch('lib.action.connector.Connector.get_object',
                            mock.Mock(return_value=check_value['raw'])):

                # This checks returned value of this action would be inspected and the one
                # that has hamlfull key-value (which has '_ref' key) would be converted
                # to harmless value as expected.
                self.assertEqual(action.run(object_type='record:a'), check_value['exp'])
