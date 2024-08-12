import pyblish.api
from maya import cmds


class ValidateMeshHistory(pyblish.api.Validator):

    def process(self, context, instance):
        selections = instance.data['selections']

        for selection in selections:
            shape = cmds.listRelatives(selection, shapes=True)[0]

            has_history = len(cmds.listHistory(shape)) > 1
            if has_history:
                raise ValueError(f"Shape {shape} has history: {has_history}")
