import tp.db as db
import tp.web as web
import tp.utilize as utilize
from bottle import route, run, abort, debug


debug(True)

#############
### start method
#############
def start(argv=None,config=None):
	utilize.cfg = config
	db.cfg = config.db
	print db.check()
	## TODO put startup logic here
	web.cfg = config
 	web.startweb(host=config.server.hostname, port=config.server.port)
