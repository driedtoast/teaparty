
import sqlalchemy.orm as orm
from datetime import date



class AmazonImage(object):
    def __init__(self, amazon_id, simple_name):
        self.amazon_id = amazon_id
        self.simple_name = simple_name
        self.added = date.today()
