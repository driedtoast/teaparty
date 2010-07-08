import sys, os
from config import Config

## directories
basedir = sys.path[0]
staticdir = basedir + '/static'
confdir = basedir + '/conf'
datadir = basedir + '/data'

## creates data dir if it doesn't exist
def setupdata():
    if(os.path.exists(datadir) == False):
        os.mkdir(datadir)

accountcfg = None

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