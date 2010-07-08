import tp.db as db
import tp.models as models


### Class to manage the ami images
class ImageService(object):
    def __init__():
        db.initdb()
    
    def save(amazonImage):
        session = db.session()
        session.add(amazonImage);
        session.flush()
        
    def get(amiid):
        session = db.session()
        return session.query(models.AmazonImage).filter(AmazonImage.id==amiid).one()
