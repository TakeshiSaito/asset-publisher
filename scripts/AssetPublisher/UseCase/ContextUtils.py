from pyblish import lib
from pyblish.plugin import Context


def get_report(context: Context):
    header = "{:<10}{:<40} -> {}".format("Success", "Plug-in", "Instance")
    result = "{success:<10}{plugin.__name__:<40} -> {instance}"
    error = "{:<10}+-- EXCEPTION: {:<70}"
    record = "{:<10}+-- {level}: {message:<70}"

    results = list()
    for r in context.data["results"]:
        # Format summary
        results.append(result.format(**r))

        # Format log records
        for lr in r["records"]:
            results.append(record.format("", level=lr.levelname, message=lr.msg))

        # Format exception (if any)
        if r["error"]:
            results.append(error.format("", r["error"].__class__.__name__))

    report = '{header}\n{line}\n{results}\n'
    return report.format(header=header, line="-" * 70, results="\n".join(results))


def get_step_results(plugins, context, order):
    extractors = [p for p in plugins if lib.inrange(number=p.order, base=order)]
    results = context.data['results']
    return [result for result in results if result['plugin'] in extractors]


def results_contains_error(results):
    return not any(result['success'] for result in results)
