from pyblish.api import Collector, Validator, Extractor, Integrator, CollectorOrder, ValidatorOrder, ExtractorOrder, IntegratorOrder


class CollectorTestPlugin(Collector):

    def process(self, context):
        context.data["test"] = "test"


class ValidatorTestPlugin(Validator):
    order = ValidatorOrder

    def process(self, context):
        assert "test" in context.data, "test not in context"


class ErrorValidatorTestPlugin(Validator):

    def process(self, context):
        raise ValueError()


class ExtractorTestPlugin(Extractor):

    def process(self, context):
        pass


class IntegratorTestPlugin(Integrator):

    def process(self, context):
        pass
