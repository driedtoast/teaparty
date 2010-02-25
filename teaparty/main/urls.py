from django.conf.urls.defaults import *


urlpatterns = patterns('teaparty.main',
    # Example:
    (r'^$', 'views.index'),
    (r'^accounts/$', 'accounts.index'),
    (r'^accounts/(?P<account_id>\d+)$', 'accounts.detail'),
    (r'^accounts/new$', 'accounts.create'),

)
