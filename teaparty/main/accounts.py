from django.http import HttpResponse
from django.template import Context, loader
from teaparty.main.models import CloudAccount
from django.http import Http404
from django.shortcuts import render_to_response


####################
##  Index request, lists all accounts
####################
def index(request):
    t = loader.get_template('main/accounts/index.html')
    accounts = CloudAccount.objects.all()
    c = Context({
        'accounts': accounts,
    })
    return HttpResponse(t.render(c))


######################
## Gets a detail of the account
######################
def detail(request, account_id):
    try:
        account = CloudAccount.objects.get(pk=account_id)
    except CloudAccount.DoesNotExist:
        raise Http404
    return render_to_response('main/accounts/detail.html', {'account': account})

######################
## Gets a detail of the account
######################
def create(request):
    return render_to_response('main/accounts/detail.html', {})

