#from blog.models import
from django.http import HttpResponseRedirect
from django.shortcuts import redirect,reverse
class RedirectAuthenticatedUserMiddleware:
    def __init__(self,get_response):
        self.request=get_response

    def __call__(self,request):
        #checks if user is authenticated or not
        if request.user.is_authenticated:
            redirect_urls=[
                reverse('blog:login'),reverse('blog:register')
            ]
            if request.path in redirect_urls:
               return redirect(reverse('blog:dashboard'))
            response=self.request(request)
            return response


