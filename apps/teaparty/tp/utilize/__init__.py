import sys, os
from config import Config

## directories
basedir = sys.path[0]
staticdir = basedir + '/static'
confdir = basedir + '/conf'
datadir = basedir + '/data'
jobsdir = None

## configurations
cfg = None
accountcfg = None

## creates data dir if it doesn't exist
def setupdata():
    if(os.path.exists(datadir) == False):
        os.mkdir(datadir)



## gets the account related data
def accountdata():
    global accountcfg
    accountfile = confdir + '/accounts.cfg'
    if(os.path.exists(accountfile) and accountcfg == None):
        f = file(accountfile)
        accountcfg = Config(f)
    return accountcfg

def account(name):
    cfg = accountdata()
    accounts = cfg.accounts
    for account in accounts:
        if(account.name == name):
            return account
    return None

### sets up the job dir
def jobdir():
    global cfg, jobsdir, basedir
    if ( jobsdir != None) :
        return jobsdir
    
    cfgjobdir = cfg.jobs.directory
    jobsdir = None
    if (cfgjobdir[0] == '/') :
        jobsdir = cfgjobdir
    else:
        jobsdir = basedir + '/'+ cfg.jobs.directory
    
    if(os.path.exists(jobsdir) == False):
        os.mkdir(jobsdir)
        
    return jobsdir