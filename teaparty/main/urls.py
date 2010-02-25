from django.conf.urls.defaults import *


urlpatterns = patterns('',
    # Example:
    (r'^$', 'teaparty.main.views.index'),
    (r'^accounts/$', 'teaparty.main.accounts.index'),
)
