from django.shortcuts import render ,render_to_response
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import BlogsPost

# Create your views here.
def archive(request):
    posts = BlogsPost.objects.order_by('-timestamp')
    t = loader.get_template("bootstrap.html")
    c = Context({'posts':posts,'times':posts})
    return HttpResponse(t.render(c))

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            posts = BlogsPost.objects.filter(title__icontains=q).order_by('-timestamp')
            return render_to_response('bootstrap_search.html',
                {'books': posts,'times': posts})     
    return render_to_response('bootstrap_search.html'
        )

def single(request):
    t =  loader.get_template('single.html')
    c = Context({})
    return HttpResponse(t.render(c))