import boto
conn = boto.connect_ec2()

keypair = 'none'
securitygroup = ['Server Group 1']
userdata = 'na'
instancetype = 'm1.small'
kernelid = 'aki-a71cf9ce'
ramdiskid = 'ari-a51cf9cc'
amiid = 'ami-xxxxxxxx'


print "Images are :"
images = conn.get_all_images(image_ids=[amiid])
image = images[0]
print "getting image: ", image.location

## just prints out the security group to check it
rs = conn.get_all_security_groups()
sgroup = None
for securitygroup in rs:
        print securitygroup.name
        if securitygroup.name == securitygroup[0]:
                sgroup = securitygroup

reservation = image.run(1,1,keypair,securitygroup,useradata,None,instancetype,None,kernelid,ramdiskid)

for instance in reservation.instances:
        print instance.id, instance.state
#        instance.updates()

