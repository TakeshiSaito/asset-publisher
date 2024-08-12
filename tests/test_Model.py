from unittest import TestCase

from AssetPublisher.Model import OptionValue


class TestOptionValue(TestCase):
    def test_option_value(self):
        option_value = OptionValue('test', 'test', True)
        self.assertEqual(option_value.name, 'test')
        self.assertEqual(option_value.value, 'test')
        self.assertTrue(option_value.required)

        with self.assertRaises(ValueError):
            OptionValue('test', '', True)
