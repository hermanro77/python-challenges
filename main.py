# This file runs tests on the other challenges

import unittest
import sys

loader = unittest.TestLoader()
suite = loader.discover('tests/', pattern='test_*.py', top_level_dir='.')

runner = unittest.TextTestRunner()
res = runner.run(suite)

sys.exit(0 if res.wasSuccessful() else 1)