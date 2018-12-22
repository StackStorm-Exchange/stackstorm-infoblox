import yaml

from st2tests.base import BaseActionTestCase

__all__ = [
    'InfobloxBaseActionTestCase',
]


class InfobloxBaseActionTestCase(BaseActionTestCase):
    __test__ = False

    def setUp(self):
        super(InfobloxBaseActionTestCase, self).setUp()

        self.full_config = self.load_yaml('full.yaml')
        self.blank_config = self.load_yaml('blank.yaml')

    def load_yaml(self, filename):
        return yaml.safe_load(self.get_fixture_content(filename))
