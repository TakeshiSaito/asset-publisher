from AssetPublisher import PyblishEnvironment, UiOptions
from AssetPublisher.View.AssetPublisherMainWindow import MainWindow
from PySide2.QtWidgets import QApplication
from pathlib import Path
import sys
import os


def run_main():
    project_root = Path(__file__).parent.parent.parent
    resource_path = project_root / 'resources'

    app = QApplication(sys.argv)
    os.environ['ASSET_PUBLISHER_RESOURCE_PATH'] = resource_path.as_posix()

    PyblishEnvironment.setup()
    options = UiOptions.get_options()

    window = MainWindow()
    window.show(**options)

    sys.exit(app.exec_())
