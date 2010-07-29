import unittest
from tptests import BaseTest
from tp import services
from tp import models

class ImageServiceTest(BaseTest):

    ### tests default amiimage behavior
    def test_amiunknown(self):
	service = services.ImageService()
	id = 'none'
	amiimage = service.getdbami(amiid=id) 
	self.assertTrue(amiimage != None)
	self.assertEqual(amiimage.simple_name, 'unknown', 'simple name should be unknown')
	self.assertEqual(id, amiimage.amazon_id,'ids don\'t match')
	
    def runTest(self):
	pass

## Tests the storage service test
class StorageServiceTest(BaseTest):
    
    ## test bucket list
    def test_buckets(self):
	
	pass
    
    ## test bucket list
    def test_acl(self):
	accountname = self.testcfg.get('accounts')['acltest1']
	bucketname = self.testcfg.get('buckets')['aclbucket']
	service = services.StorageService()
	service.change_bucket_visibility(accountname,bucketname,recursive=True)
	pass
    
    
    
    def runTest(self):
	print('running test...')
	print(self.testcfg)
	pass
	
    def suite():
	tests = ['test_buckets']	
	return unittest.TestSuite(map(StorageServiceTest(), tests))
    

## Tests the storage service test
class DatabaseServiceTest(BaseTest):
    
    ## test bucket list
    def test_simpledbs(self):
	accountname = self.testcfg.get('accounts')['simpledb_test1']
	service = services.DatabaseService()
	dbslist = service.get_dbs(accountname)
	self.assertTrue(dbslist != None, 'no simple dbs setup for this')
	self.assertTrue(len(dbslist) > 0, 'there is an empty list for dbs')
	for db in dbslist:
	    print(db)
	pass
    
    
    ## test bucket list
    def test_copy(self):
	fromaccountname = self.testcfg.get('accounts')['simpledb_from']
	toaccountname = self.testcfg.get('accounts')['simpledb_to']
	
	fromDomain = self.testcfg.get('simpledb')['fromdb']
	toDomain = self.testcfg.get('simpledb')['todb']
	
	service = services.DatabaseService()
	count = service.copy_db(fromaccountname, fromDomain,toaccountname,toDomain)
	self.assertTrue(count > 0, 'nothing copied')
	print(fromDomain + ' to '  +  toDomain +' items copied ' + str(count))
	
    def runTest(self):
	pass
	
    
    
