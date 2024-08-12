$root_dir = Split-Path -Parent $MyInvocation.MyCommand.Definition

$script_dir = "$root_dir\scripts"
$bin_dir = "$root_dir\bin\pyblish\pyblish"
$env:PYTHONPATH = "$script_dir;$bin_dir;$env:PYTHONPATH"
$env:MAYA_MODULE_PATH = "$root_dir"

Start-Process -FilePath "C:\Program Files\Autodesk\Maya2024\bin\maya.exe"