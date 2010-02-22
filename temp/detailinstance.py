import boto
conn = boto.connect_ec2()

instanceid='i-xxxxxxxx'

print "instances "
instances = conn.get_all_instances()
for reservation in instances:
        for instance in reservation.instances:
                if instance.id == instanceid:
                        print instance.id, instance.state
                        print instance.public_dns_name
                        print instance.get_console_output().output
