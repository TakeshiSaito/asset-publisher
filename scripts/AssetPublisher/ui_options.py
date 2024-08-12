import os
import json
from pathlib import Path


def get_options():
    resource_path = Path(os.environ['ASSET_PUBLISHER_RESOURCE_PATH'])
    setting_path = resource_path / 'asset_publisher_setting.json'

    with setting_path.open('r') as file:
        setting = json.load(file)

    return setting['ui_options']
