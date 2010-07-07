import tp.db as db
import tp.web as web
from bottle import route, run, abort, debug



#############
### start method
#############
def start(argv=None,config=None):
   	print argv
	print config
	print config.db
	print db.check()
	## TODO put startup logic here
	web.cfg = config
 	web.startweb(host=config.server.hostname, port=config.server.port)
