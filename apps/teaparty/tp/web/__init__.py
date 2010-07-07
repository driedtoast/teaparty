from bottle import route, run, abort, debug
from bottle import mako_view as view
from bottle import send_file, redirect
import bottle
import os, sys
import tp.utilize as utilize

cfg = None


@route('/static/js/:filename')
def static_file(filename):
    	send_file(filename, root=utilize.staticdir+'/js')

@route('/static/css/:dir/images/:filename')
def static_file(filename):
    	send_file(filename, root=utilize.staticdir+'/css/'+dir+'/images')

@route('/static/css/:dir/:filename')
def static_file(filename):
    	send_file(filename, root=utilize.staticdir+'/css/'+dir)
	




@route('/')
@view('hello')
def index():
	dirname = os.path.dirname( os.path.realpath( __file__ ) )
        return dict(name='Hello World', dir=dirname)


########################
## Starts up the web 
## application
#######################
def startweb(host,port):
	print os.path.dirname( os.path.realpath( __file__ ) )
	print "sys.path[0]:   %s" % sys.path[0]
	bottle.TEMPLATE_PATH.insert(0,os.path.dirname( os.path.realpath( __file__ ))+'/views/')
	run(host=host, port=port)

