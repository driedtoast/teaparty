import unittest
from tp import db
import tptests.services

class AllTests(unittest.TestSuite):
	def __init__(self):
		super(AllTests,self).__init__()
		self.addTest(DbTest())
		self.addTest(tptests.services.ImageServiceTest('test_amiunknown'))
		self.addTest(tptests.services.StorageServiceTest('test_acl'))
		self.addTest(tptests.services.StorageServiceTest('test_buckets'))
		self.addTest(tptests.services.DatabaseServiceTest('test_simpledbs'))
		self.addTest(tptests.services.DatabaseServiceTest('test_copy'))
		
		pass



class DbTest(unittest.TestCase):
	
	def setUp(self):
		db.initdb()
	
	def runTest(self):
		self.test_session()
		pass
	
	def test_session(self):
		session = db.session()
		self.assertTrue(session != None)
