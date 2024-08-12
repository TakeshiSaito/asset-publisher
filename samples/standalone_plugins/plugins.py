import pyblish.api


class SampleCollectorPlugin(pyblish.api.Collector):

    def process(self, context):
        context.data["test"] = "test"


class SampleValidatorPlugin(pyblish.api.Validator):

    def process(self, context):
        assert "test" in context.data, "test not in context"


class SampleExtractorPlugin(pyblish.api.Extractor):

    def process(self, context):
        pass


class SampleIntegratorPlugin(pyblish.api.Integrator):

    def process(self, context):
        pass
