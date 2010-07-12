import tp.db as db
import tp.models as models


### Class to manage the ami images
class ImageService(object):
    def __init__(self):
        db.initdb()
    
    def save(self,amazonImage):
        session = db.session()
        session.add(amazonImage);
        session.flush()
        
    def get(self,amiid):
        session = db.session()
        try:
            return session.query(models.AmazonImage).filter(models.AmazonImage.amazon_id==amiid).one()
        except Exception, e:
            return None
