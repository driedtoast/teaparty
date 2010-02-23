import os
import sys
import json
import fileinput
import re

## updates the configuration
configfile='general.config'
settingsfile='settings.py'
if len(sys.argv) > 1:
        configfile = sys.argv[1]
        settingsfile = sys.argv[2]

basedir = os.path.join(os.path.dirname(configfile),'../')
print " Base directory is ", basedir

## load configfile json
print "loading file ", configfile
print " from directory ", os.path.dirname(configfile)


def loadConfig():
   f = open(configfile)
   config = json.load(f)
   f.close()
   return config;

## creates a map of the config
## map is used for settings replacement
def configMap(config):
   map={}
   map['@ADMIN_USER@'] = config['admin'][0]
   map['@ADMIN_EMAIL@'] = config['admin'][1]
   map['@TEMPLATE_DIR@'] = os.path.join(os.path.abspath(basedir),'teaparty/templates')
   map['@MEDIA_ROOT@'] = os.path.join(os.path.abspath(basedir),'static')
   dbengine = config['db']['engine']
   map['@DATABASE_ENGINE@']=dbengine
   if dbengine == 'sqlite3':
	map['@DATABASE_NAME@'] = os.path.join(os.path.abspath(basedir),'data', config['db']['name']) 
	map['@DATABASE_HOST@'] = ''
        map['@DATABASE_PORT@'] = ''
        map['@DATABASE_USER@'] = ''
        map['@DATABASE_PASSWORD@'] = ''
   else: 
   	map['@DATABASE_NAME@'] = config['db']['name']
   	map['@DATABASE_HOST@'] = config['db']['host']
   	map['@DATABASE_PORT@'] = config['db']['port']
   	map['@DATABASE_USER@'] = config['db']['user']
   	map['@DATABASE_PASSWORD@'] = config['db']['password']
   map['@SECRET_KEY@']=config['server']['secret_key']
   mediaurl = 'http://'+config['server']['host']+':'+config['server']['port']+'/static/'
   map['@MEDIA_URL@']=mediaurl
   return map 

def replaceInFile(filename, cfgMap):
   rc = re.compile('|'.join(map(re.escape, cfgMap)))
   def translate(match):
        return cfgMap[match.group(0)]
   for line in fileinput.FileInput(filename,inplace=1):
	line = rc.sub(translate,line)
	print line


## load up config
config = loadConfig()
cfgMap = configMap(config)
replaceInFile(settingsfile, cfgMap)

