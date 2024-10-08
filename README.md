[![Test](https://github.com/TakeshiSaito/asset-publisher/actions/workflows/run_tests.yml/badge.svg)](https://github.com/TakeshiSaito/asset-publisher/actions/workflows/run_tests.yml)

# asset-publisher

## Description

This tool allows you to build a UI based on a configuration file and run pyblish while passing input to context.

By using this tool...

- You can easily create a UI to pass the necessary context data to the pyblish plugin.
- Developers will no longer need to develop when a simple UI is sufficient.

## Usage

It is available for standalone and Maya use.

The startup commands for the standalone tool are as follows.

```python
from AssetPublisher import Main

Main.run_main()
```

The startup commands for MAYA are as follows.

```python
from AssetPublisherForMaya import Main

Main.run_main()
```

## Setting File

You can add UI construction and pyblish plugin loading locations based on the configuration file.

Change the setting file below to suit your needs.

[asset_publisher_setting.json](resources%2Fasset_publisher_setting.json)

### ui_options

Currently, the following UI elements can be built.
- folder_dialog
- line_edit
- radio

### folder_dialog

A folder dialog and a path entry field can be added.

```json
{
  "ui_options": {
    "Name of the option": {
      "type": "folder_dialog",
      "label": "You can specify the headings to be displayed in the UI.",
      "placeholder_text": "Can set placeholder text. ",
      "default_value": "Default values can be set.",
      "required": "You can specify whether the value is required or not."
    }
  }
}
```

### line_edit

A single line of input fields can be added.

```json
{
  "ui_options": {
    "Name of the option": {
      "type": "line_edit",
      "label": "You can specify the headings to be displayed in the UI.",
      "placeholder_text": "Can set placeholder text. ",
      "default_value": "Default values can be set.",
      "required": "You can specify whether the value is required or not."
    }
  }
}
```

### radio

Multiple-choice radio buttons can be added.

```json
{
  "ui_options": {
    "Name of the option": {
      "type": "radio",
      "label": "You can specify the headings to be displayed in the UI.",
      "variants": [
        "option1",
        "option2"
      ]
    }
  }
}
```

### PYBLISHPLUGINPATH

You can add paths to PYBLISHPLUGINPATH.

```json
{
  "PYBLISHPLUGINPATH": [
    "path/to/pyblish_plugin"
  ]
}
```