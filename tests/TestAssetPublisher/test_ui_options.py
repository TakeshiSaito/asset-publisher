from pathlib import Path
from unittest import TestCase
from tempfile import TemporaryDirectory

import os
import json

from AssetPublisher import UiOptions


class TestUiOptions(TestCase):

    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        setting_contents = {"ui_options": {"root": {"type": "folder_dialog",
                                                    "label": "Project root",
                                                    "placeholder_text": "Select project root",
                                                    "default_value": "",
                                                    "required": True},
                                           "file_name": {"type": "line_edit",
                                                         "label": "File name",
                                                         "placeholder_text": "Enter file name",
                                                         "default_value": "",
                                                         "required": True
                                                         }
                                           }
                            }

        setting_path = Path(self.temp_dir.name) / 'asset_publisher_setting.json'
        with setting_path.open('w') as file:
            json.dump(setting_contents, file)

        os.environ['ASSET_PUBLISHER_RESOURCE_PATH'] = self.temp_dir.name

    def test_get_options(self):
        setting = UiOptions.get_options()
        self.assertEqual(len(setting), 2)

        self.assertEqual(setting['root']['type'], 'folder_dialog')
        self.assertEqual(setting['root']['label'], 'Project root')
        self.assertEqual(setting['root']['placeholder_text'], 'Select project root')
        self.assertEqual(setting['root']['default_value'], '')
        self.assertEqual(setting['root']['required'], True)

        self.assertEqual(setting['file_name']['type'], 'line_edit')
        self.assertEqual(setting['file_name']['label'], 'File name')
        self.assertEqual(setting['file_name']['placeholder_text'], 'Enter file name')
        self.assertEqual(setting['file_name']['default_value'], '')
        self.assertEqual(setting['file_name']['required'], True)

    def tearDown(self):
        self.temp_dir.cleanup()
