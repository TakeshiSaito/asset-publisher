import os
import json
from pathlib import Path


def setup():
    resource_path = Path(os.environ['ASSET_PUBLISHER_RESOURCE_PATH'])
    setting_path = resource_path / 'asset_publisher_setting.json'

    with setting_path.open('r') as file:
        setting = json.load(file)

    pyblish_plugin_paths = setting['pyblish_plugin_paths']
    env_value = os.pathsep.join(pyblish_plugin_paths)
    os.environ['PYBLISHPLUGINPATH'] = env_value
