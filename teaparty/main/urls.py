from django.conf.urls.defaults import *


urlpatterns = patterns('teaparty.main',
    # Example:
    (r'^$', 'views.index'),
    (r'^accounts/$', 'accounts.index'),
)
