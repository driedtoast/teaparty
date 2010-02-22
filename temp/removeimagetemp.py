import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import sys



bucketname = 'default'
conn = S3Connection()
bucket = conn.get_bucket(bucketname)



imagename = 'na'
if len(sys.argv) > 1:
        imagename = sys.argv[1]
rs = bucket.list()
for key in rs:
        if key.name.startswith(imagename):
                print key.name
                bucket.delete_key( key.name)

