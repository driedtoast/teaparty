
import sqlalchemy.orm as orm
from datetime import date



### AMI image representation
class AmazonImage(object):
    awsami = None

    def __init__(self, amazon_id, simple_name=None):
        self.amazon_id = amazon_id
        self.simple_name = simple_name
        self.added = date.today()
    
