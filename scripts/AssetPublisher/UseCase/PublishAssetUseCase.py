from typing import List

import pyblish.api
import pyblish.util
from AssetPublisher.Model import OptionValue
from AssetPublisher.UseCase import ContextUtils
from AssetPublisher.UseCase.ContextUtils import get_step_results, results_contains_error


def execute(options: List[OptionValue],
            bypass_validation: bool,
            update_progress_bar: callable,
            show_confirm_dialog: callable):
    context = pyblish.api.Context()
    for option in options:
        context.data[option.name] = option.value

    pyblish.api.deregister_all_paths()

    plugins = pyblish.api.discover()
    if not plugins:
        show_confirm_dialog('Result', 'No plugins found.')
        raise ValueError('No plugins found.')

    # Collection---------------------------------------------------------------------

    update_progress_bar(0 / 4 * 100, 'Collecting')
    context = pyblish.util.collect(context, plugins)

    # Validation---------------------------------------------------------------------

    update_progress_bar(1 / 4 * 100, 'Validating')
    context = pyblish.util.validate(context, plugins)

    if not bypass_validation:
        validator_results = get_step_results(plugins, context, pyblish.api.ValidatorOrder)
        if validator_results and results_contains_error(validator_results):
            report = ContextUtils.get_report(context)
            show_confirm_dialog('Validation Error', report)
            raise ValueError('Error Occurred during Validation')

    # Extraction---------------------------------------------------------------------

    update_progress_bar(2 / 4 * 100, 'Extracting')
    context = pyblish.util.extract(context, plugins)

    extractor_results = get_step_results(plugins, context, pyblish.api.ExtractorOrder)
    if extractor_results and results_contains_error(extractor_results):
        report = ContextUtils.get_report(context)
        show_confirm_dialog('Extraction Error', report)
        raise ValueError('Error Occurred during Extraction')

    # Integration---------------------------------------------------------------------

    update_progress_bar(3 / 4 * 100, 'Integrating')
    context = pyblish.util.integrate(context, plugins)

    # Report---------------------------------------------------------------------
    report = ContextUtils.get_report(context)
    show_confirm_dialog('Publish Asset', report)
    update_progress_bar(100, '')
