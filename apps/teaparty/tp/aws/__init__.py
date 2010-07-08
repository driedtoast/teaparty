import boto


## gets all instances for an account
def instances(account):
    conn = boto.connect_ec2(account.access_key,account.secret_key)
    instancesarr = []
    instances = conn.get_all_instances()
    for reservation in instances:
        for instance in reservation.instances:
            instancesarr.append(instance)
    return instancesarr
    
## gets detail on an ami
def ami(account,amiid):
    conn = boto.connect_ec2(account.access_key,account.secret_key)
    images = conn.get_all_images(image_ids=[amiid])
    for image in images:
        return image
    return image
        
# images = conn.get_all_images()