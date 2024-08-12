from unittest import TestCase

from AssetPublisher.UseCase.ContextUtils import get_step_results, results_contains_error
from resources.TestPlugins import CollectorTestPlugin, ValidatorTestPlugin, ExtractorTestPlugin, IntegratorTestPlugin, ErrorValidatorTestPlugin
from pyblish import api, util


class TestContextUtils(TestCase):

    def test_get_step_results(self):
        plugins = [CollectorTestPlugin, ValidatorTestPlugin, ExtractorTestPlugin, IntegratorTestPlugin]
        context = api.Context()
        context = util.publish_all(context, plugins)
        validator_results = get_step_results(plugins, context, api.ValidatorOrder)

        self.assertEqual(len(validator_results), 1)

        result = validator_results[0]
        plugin_class = result['plugin']

        self.assertEqual(plugin_class, ValidatorTestPlugin)

    def test_result_contains_error(self):
        plugins = [ErrorValidatorTestPlugin]
        context = api.Context()
        context = util.publish_all(context, plugins)

        results = context.data['results']
        self.assertTrue(results_contains_error(results))
