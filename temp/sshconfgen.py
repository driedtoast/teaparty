import boto
import boto.ec2

conn = boto.connect_ec2()
account = 'acountname'

counts = {}

rs = conn.get_all_instances()
for reservation in rs:
        rgroups = reservation.groups
        groupname = None
        count = 0
        rg = rgroups[0]
        groupname = str(rg.id)
        print

        if counts.has_key(groupname):
                count = counts[groupname]
        if count == 0:
                counts[groupname] = 1
        else:
                counts[groupname] = 1 + count
        count = counts[groupname]

        instances = reservation.instances
        for instance in instances:
                if instance.state == 'running':
                        print 'host '+account+'.'+groupname+str(count)
                        print ' IdentityFile ~/.ec2/'+instance.key_name+'.pem'
                        print ' HostName '+instance.public_dns_name
                        print ' User root'
                        print ' ForwardAgent yes'

