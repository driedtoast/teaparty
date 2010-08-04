import boto
from boto.s3.key import Key

## TODO make into a provider type interface


def ec2conn(account):
    conn = boto.connect_ec2(account.access_key,account.secret_key)
    return conn

def s3conn(account):
    conn = boto.connect_s3(account.access_key,account.secret_key)
    return conn

def sdbconn(account):
    conn = boto.connect_sdb(account.access_key,account.secret_key)
    return conn


## gets all instances for an account
def instances(account):
    conn = ec2conn(account)
    instancesarr = []
    instances = conn.get_all_instances()
    for reservation in instances:
        for inst in reservation.instances:
            instancesarr.append(inst)
            inst.groups = reservation.groups
            ## print inst.get_console_output()
    return instancesarr
    
## gets detail on an ami
def ami(account,amiid):
    conn = ec2conn(account)
    images = conn.get_all_images(image_ids=[amiid])
    for image in images:
        return image
    return image

## gets all amis
def amis(account):
    conn = ec2conn(account)
    return conn.get_all_images(owners=[account.id])

## get all buckets
def buckets(account):
    conn = s3conn(account)
    rs = conn.get_all_buckets()
    return rs

## gets a bucket
def bucket(account, bucketname, create=False):
    conn = s3conn(account)
    b = None
    try:
        b = conn.get_bucket(bucketname)
    except Exception, e:
        if(create):
            b = conn.create_bucket(bucketname)
    return b


## get all domains
def simpledbs(account):
    conn = sdbconn(account)
    rs = conn.get_all_domains()
    return rs

## get domain
def simpledb(account, domain, create=False):
    conn = sdbconn(account)
    db = None
    try: 
        db = conn.get_domain(domain)
    except Exception, e:
        if(create):
            db = conn.create_domain(domain)
    return db