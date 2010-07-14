import tp.db as db
import tp.models as models
import tp.utilize as utilize
import tp.aws as aws
import os

class BaseService(object):
    def __init__(self):
        self.setup()
    
    def setup(self):
        db.initdb()
    
    def session(self):
        return db.session()
    
    def _save(self, obj):        
        session = db.session()
        session.add(obj)
        session.flush()


### Class to manage the ami images
class ImageService(BaseService):
    def __init__(self):
        self.setup()
    
    def save(self,amazonImage):
        self._save(amazonImage)
        
    def get(self,accountname, amiid):
        account = utilize.account(accountname)
        ami = aws.ami(account,amiid)
        amiimage = None 
        try:
            session = self.session()
            amiimage = session.query(models.AmazonImage).filter(models.AmazonImage.amazon_id==amiid).one()
        except Exception, e:
            pass
        if (amiimage == None):
            amiimage = models.AmazonImage(ami.id,'unknown')
        amiimage.awsami = ami
        
        return amiimage


### map/reduce job service
class JobsService(BaseService):
    def __init__(self):
        #self.setup()
        pass
    
    def list(self):
        jdir = utilize.jobdir()
        ## iterate job dir for jobs list
        flowlist = []
        sdir = None
        try:
            for subdir, dirs, files in os.walk(jdir):
                if(subdir != sdir):
                    sdir = subdir
                    bname = os.path.basename(sdir)
                    idx = jdir.find(bname)
                    ## this is sort of hacky
                    ## need to clean it up
                    if(idx == -1 ):
                        flowlist.append(bname)
                continue
        except Exception, e:
            pass
        return flowlist