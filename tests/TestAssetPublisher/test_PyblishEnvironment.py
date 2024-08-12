from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path
import os
import json
from AssetPublisher import PyblishEnvironment


class TestSetup(TestCase):

    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        os.environ['ASSET_PUBLISHER_RESOURCE_PATH'] = self.temp_dir.name

        test_setting_content = {
            'PYBLISHPLUGINPATH': [
                'path/to/plugin1',
                'path/to/plugin2'
            ]
        }
        test_setting_path = Path(self.temp_dir.name) / 'asset_publisher_setting.json'
        with test_setting_path.open('w') as file:
            json.dump(test_setting_content, file)

    def test_environment(self):
        PyblishEnvironment.setup()
        expected = 'path/to/plugin1;path/to/plugin2' if os.name == 'nt' else 'path/to/plugin1:path/to/plugin2'
        self.assertEqual(os.environ['PYBLISHPLUGINPATH'], expected)

    def test_append_to_existing(self):
        os.environ['PYBLISHPLUGINPATH'] = 'existing/path'
        PyblishEnvironment.setup()
        expected = 'path/to/plugin1;path/to/plugin2;existing/path' if os.name == 'nt' else 'path/to/plugin1:path/to/plugin2:existing/path'
        self.assertEqual(os.environ['PYBLISHPLUGINPATH'], expected)

    def tearDown(self):
        del os.environ['PYBLISHPLUGINPATH']
        self.temp_dir.cleanup()
