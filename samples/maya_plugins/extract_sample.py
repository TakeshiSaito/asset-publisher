import pyblish.api
import time


class SampleExtractor(pyblish.api.Extractor):
    hosts = ['maya', 'mayapy']

    def process(self, context):
        for i in range(5):
            time.sleep(1)
            self.log.info(f'Processing {i + 1}...')
