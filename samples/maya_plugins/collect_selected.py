import pyblish.api
from maya import cmds


class SelectedCollector(pyblish.api.Collector):
    hosts = ['maya', 'mayapy']

    def process(self, context):
        instance = context.create_instance('Selected', family='selected')
        instance.data['selections'] = cmds.ls(sl=True)
