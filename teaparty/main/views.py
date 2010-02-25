from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    t = loader.get_template('main/index.html')
    c = Context({
        'hello': 'teaparty',
    })
    return HttpResponse(t.render(c))

