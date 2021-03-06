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
    def get_account(self,accountname):
        return utilize.account(accountname)
        


### Class to manage the ami images
class ImageService(BaseService):
    def __init__(self):
        self.setup()
    
    ## saves db object to db
    def save(self,amazonImage):
        self._save(amazonImage)
        
    ## gets just the db object
    def getdbami(self,amiid):
        amiimage = None 
        try:
            session = self.session()
            amiimage = session.query(models.AmazonImage).filter(models.AmazonImage.amazon_id==amiid).one()
        except Exception, e:
            pass
        if (amiimage == None):
            amiimage = models.AmazonImage(amiid,'unknown')
        return amiimage
        
    def get(self,accountname, amiid):
        account = self.get_account(accountname)
        ami = aws.ami(account,amiid)
        amiimage = self.getdbami(amiid)
        amiimage.awsami = ami
        return amiimage

### Class to manage the s3 and ebs
class StorageService(BaseService):
    def __init__(self):
        self.setup()
    
    ## gets just the db object
    def get_storage_container(self,accountname, bucketname, create=False):
        account = self.get_account(accountname)
        bucket = aws.bucket(account,bucketname,create)
        return bucket
    
    
    ## gets just the db object
    def get_storage_containers(self,accountname):
        account = self.get_account(accountname)
        ## todo more stuff
        return aws.buckets(account)
    
    ## change the bucket visibility
    def change_bucket_visibility(self,accountname, bucketname, recursive=False,type='public'):
        scope = 'public-read'
        account = self.get_account(accountname)
        b = aws.bucket(account,bucketname)
        b.set_acl(scope)
        if(recursive):
            rs = b.list()
            for key in rs:
                key.set_acl(scope)
                
    ## Copies data from one bucket to another            
    def copy_bucket(self,from_accountname, from_bucket, to_accountname, to_bucket=None,override=False):
        fromaccount = self.get_account(from_accountname)
        toaccount = self.get_account(to_accountname)
        frombucket = aws.bucket(account,from_bucket)
        tobucket = aws.bucket(toaccount,to_bucket,True)
        rs = frombucket.list()
        for key in rs:
                name = key.name
                filename = './'+ name
                dir = os.path.dirname(filename)
                if (os.path.exists(dir) != True):
                        try:
                                os.makedirs(dir)
                        except Exception, e:
                                pass
                if (os.path.exists(filename) == True):
                        os.remove(filename)
                key.get_contents_to_filename(filename)
                print( ' moving ' + name + ' from ' + frombucket.name)
                try:
                        bucket.delete_key(name)
                except Exception, e:
                        pass
                tokey = Key(bucket)
                tokey.key = name
                tokey.set_acl(key.get_acl())
                tokey.metadata = key.metadata
                tokey.set_contents_from_filename(filename)
                os.remove(filename)


### Class to manage the database stores
class DatabaseService(BaseService):
    def __init__(self):
        self.setup()

    ## gets a list of dbs
    def get_dbs(self,accountname):
        account = self.get_account(accountname)
        ## todo combine into a variety of types
        return aws.simpledbs(account)
    
    ## copies one domain to another
    def copy_db(self,from_accountname, from_domain, to_accountname, to_domain=None,override=False):
        todomain = to_domain
        if(todomain == None):
            todomain = from_domain
        fromaccount = self.get_account(from_accountname)
        toaccount = self.get_account(to_accountname)
        fromdb = aws.simpledb(fromaccount,from_domain)
        todb = aws.simpledb(toaccount,todomain,create=True)
        count = 0
        for item in fromdb:
                name = item.name
                toitem = None
                try:
                        toitem = todb.get_item(name)
                        if (override == True):
                            todb.delete_item(toitem)
                            toitem = None
                        else:
                            print(' item exists already ' + name + ' in ' + domainname)
                except Exception, e:
                        pass
                if (toitem == None):
                        attrs = fromdb.get_attributes(name)
                        todb.put_attributes(name,attrs)
                        print(' adding item : ' + name)
                        count = count + 1
        return count

        



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