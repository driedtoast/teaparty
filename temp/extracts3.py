import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key

prefix='prefixfilename'
bucketname='default'
conn = S3Connection()
bucket = conn.get_bucket(bucketname)


rs = bucket.list()
for key in rs:
    if key.name.find(prefix) != -1:
        name = key.name

        print " extracting ", name
        key.get_contents_to_filename('./extract/'+name)

