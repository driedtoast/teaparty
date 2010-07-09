import boto


def ec2conn(account):
    conn = boto.connect_ec2(account.access_key,account.secret_key)
    return conn

## gets all instances for an account
def instances(account):
    conn = ec2conn(account)
    instancesarr = []
    instances = conn.get_all_instances()
    for reservation in instances:
        for instance in reservation.instances:
            instancesarr.append(instance)
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
