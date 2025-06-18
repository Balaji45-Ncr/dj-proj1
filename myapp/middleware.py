#from blog.models import
from django.http import HttpResponseRedirect
from django.shortcuts import redirect,reverse
class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        redirect_urls = [
            reverse('blog:login'),
            reverse('blog:register'),
        ]

        # If the user is authenticated and trying to access login/register
        if request.user.is_authenticated and request.path in redirect_urls:
            return redirect(reverse('blog:dashboard'))

        # Always call the next middleware/view and return response
        response = self.get_response(request)
        return response


class RedirectUnAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        protected_urls = [
            reverse('blog:dashboard'),
        ]

        # If not logged in and trying to access protected URL
        if not request.user.is_authenticated and request.path in protected_urls:
            return redirect(reverse('blog:login'))

        # Always call the next middleware/view and return response
        response = self.get_response(request)
        return response

