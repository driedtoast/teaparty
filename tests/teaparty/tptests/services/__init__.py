import unittest
from tptests import BaseTest
from tp import services
from tp import models

class ImageServiceTest(BaseTest):

        ### tests default amiimage behavior
        def test_amiunknown(self):
            service = services.ImageService()
            id = 'none'
            amiimage = service.getdbami(id) 
            self.assertTrue(amiimage != None)
            self.assertEqual(amiimage.simple_name, 'unknown', 'simple name should be unknown')
            self.assertEqual(id, amiimage.amazon_id,'ids don\'t match')
        def runTest(self):
	    pass
	
