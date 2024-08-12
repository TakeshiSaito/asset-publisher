import os
from pathlib import Path

import pyblish.api

from AssetPublisher import UiOptions, PyblishEnvironment
from AssetPublisherForMaya.MayaMainWindow import MayaMainWindow


def run_main():
    pyblish.api.register_host("maya")
    pyblish.api.register_host('mayapy')

    project_root = Path(__file__).parent.parent.parent
    resource_path = project_root / 'resources'
    os.environ['ASSET_PUBLISHER_RESOURCE_PATH'] = resource_path.as_posix()

    PyblishEnvironment.setup()
    options = UiOptions.get_options()

    window = MayaMainWindow()
    window.setup(options)
    window.show()


if __name__ == '__main__':
    run_main()
