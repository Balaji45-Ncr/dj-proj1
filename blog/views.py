from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.
class index(ListView):
    model=Post
    template_name='blog/index.html'
    context_object_name = 'Latest'


class detail(View):
    template_name='blog/detail.html'
    def get(self,request,id):
        return render(request,self.template_name)

class Detail(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    #pk_url_kwarg = 'id'

def old_url_redirect(request,id):
    return redirect(reverse('blog:new_url',args=[id]))

def new_url_view(request,id):
    return HttpResponse(f'This is the new URL {id}')


