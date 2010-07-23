
import unittest
import testsuite

import tp

class BaseTest(unittest.TestCase):
	
	def setUp(self):
		tp.utilize.setupdata()
		tp.utilize.cfg = testsuite.cfg
