from django.shortcuts import render_to_response

def notfound(request): 
    return render_to_response('common/404error.html',{});

def systemerror(request): 
    return render_to_response('common/500error.html',{});


