from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import View
# Create your views here.
class index(View):
    template_name='blog/index.html'
    context_data='Latest Posts'
    def get(self,request):
        return render(request,self.template_name,{'context':self.context_data})



class detail(View):
    template_name='blog/detail.html'
    def get(self,request,id):
        return render(request,self.template_name)

def old_url_redirect(request,id):
    return redirect(reverse('blog:new_url',args=[id]))

def new_url_view(request,id):
    return HttpResponse(f'This is the new URL {id}')


