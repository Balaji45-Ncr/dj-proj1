from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from .models import Post
from django.http import HttpResponseNotFound
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
    #context_object_name = 'post'
    #pk_url_kwarg = 'id'
    def get_object(self, queryset=None):
        data=self.kwargs['pk']
        try:
            post_data=Post.objects.get(pk=data)
            # related_posts=Post.objects.filter(category=post_data.category).exclude(pk=post_data.id)
            return post_data
        except Post.DoesNotExist:
            return HttpResponseNotFound('Post does not exists')

    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        related_data= self.get_object()
        related_posts= Post.objects.filter(category=related_data.category).exclude(pk=related_data.id)
        data['related_posts']=related_posts
        return data


def old_url_redirect(request,id):
    return redirect(reverse('blog:new_url',args=[id]))

def new_url_view(request,id):
    return HttpResponse(f'This is the new URL {id}')


