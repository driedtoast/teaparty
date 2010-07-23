import unittest
from tp import db
import tptests.services

class AllTests(unittest.TestSuite):
	def __init__(self):
		super(AllTests,self).__init__()
		self.addTest(DbTest())
		self.addTest(tptests.services.ImageServiceTest())
		pass



class DbTest(unittest.TestCase):
	
	def setUp(self):
		db.initdb()
	
	def runTest(self):
		pass
	
	def test_session(self):
		session = db.session()
		self.assertTrue(session != None)
