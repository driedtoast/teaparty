import boto
from boto.s3.key import Key

## TODO make into a provider type interface


def ec2conn(account):
    conn = boto.connect_ec2(account.access_key,account.secret_key)
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
    conn = boto.connect_ec2(account.access_key,account.secret_key)
    return conn.get_all_images(owners=[account.id])

## get all buckets
def buckets(account):
    conn = boto.connect_s3(account.access_key,account.secret_key)
    rs = conn.get_all_buckets()
    return rs

## get all domains
def simpledbs(account):
    conn = boto.connect_sdb(account.access_key,account.secret_key)
    rs = conn.get_all_domains()
    return rs

## get domain
def simpledb(account, domain, create=False):
    conn = boto.connect_sdb(account.access_key,account.secret_key)
    db = None
    try: 
        db = conn.get_domain(domain)
    except Exception, e:
        if(create):
            db = conn.create_domain(domain)
    return db