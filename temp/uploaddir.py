import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key

bucketname = 'default'
conn = S3Connection()
bucket = conn.get_bucket(bucketname)

dirpath = '/temp'


## interact with s3 for particular file
def pushtoS3(filename,name):
   print filename
   try:
        key = bucket.get_key(name)
   except Exception, e:
        print e

   if key == None:
        key = Key(bucket)
        key.key = name
        key.set_contents_from_filename(filename)




## loop through the directory
for subdir, dirs, files in os.walk(repopath):
    for file in files:
        if file.rfind('.gz') > 0 or file.rfind('.xml') > 0 or file.rfind('.rpm') > 0:
                fullpath = os.path.join(subdir, file)
                pushtoS3(fullpath,file)
                print file
                print fullpath

