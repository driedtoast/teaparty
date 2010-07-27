
import unittest
import testsuite
import os

import tp
from config import Config

class BaseTest(unittest.TestCase):
	
	
	def setUp(self):
		tp.utilize.setupdata()
		tp.utilize.cfg = testsuite.cfg
		
		homedir = os.getenv("HOME")
		testcfgfile = homedir + '/teaparty_test.cfg'
		if(os.path.exists(testcfgfile)):
		    f = file(testcfgfile)
		    self.testcfg = Config(f)