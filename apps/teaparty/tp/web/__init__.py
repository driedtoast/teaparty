from bottle import route, run, abort, debug
from bottle import mako_view as view
from bottle import send_file, redirect
from bottle import PasteServer
import bottle
import os, sys,  traceback
import tp.utilize as utilize
import tp.aws as aws

cfg = None


@route('/static/js/:filename')
def static_file_js(filename):
    	send_file(filename, root=utilize.staticdir+'/js')

@route('/static/css/:dir/images/:filename')
def static_file_css_images(dir,filename):
    	send_file(filename, root=utilize.staticdir+'/css/'+dir+'/images')

@route('/static/css/:dir/:filename')
def static_file_cc(dir,filename):
	send_file(filename, root=utilize.staticdir+'/css/'+dir)

### dashboard
@route('/')
@view('dashboard')
def index():
	accountdata = utilize.accountdata()
	accounts = []
	if( accountdata != None):
		## add account info
		accounts = accountdata.accounts
	return dict(name='dashboard', accounts=accounts)

### account instances
@route('/account/:accountname')
@view('account_instances')
def accountinstances(accountname):
	account = utilize.account(accountname)
	instances = []
	if( account != None):
		## add account info
		instances = aws.instances(account)
        return dict(name='account instances', account=account, instances=instances)

### ami image detail
@route('/ami/:accountname/:amiid')
@view('ami_details')
def amidetails(accountname,amiid):
	account = utilize.account(accountname)
	ami = aws.ami(account,amiid)
	return dict(name='ami details', account=account, ami=ami)

### ami image list
@route('/amis/:accountname')
@view('amis')
def amilist(accountname):
	account = utilize.account(accountname)
	amis = aws.amis(account)
	return dict(name='ami list', account=account, amis=amis)

	
### start instance
@route('/startinstance/:accountname')
@view('start_instance')
def startinstance(accountname):
	account = utilize.account(accountname)
	## TODO get the details
	return dict(name='start instance', account=account)


########################
## Starts up the web 
## application
#######################
def startweb(host,port):
	bottle.TEMPLATE_PATH.insert(0,os.path.dirname( os.path.realpath( __file__ ))+'/views/')
	run(server=PasteServer,host=host, port=port)


