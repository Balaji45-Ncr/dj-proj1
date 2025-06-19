from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,FormView,UpdateView,DeleteView,CreateView
from django.views.generic.base import TemplateView
from .models import Post
from django.http import HttpResponseNotFound
from .forms import Contactform,Registerform,Loginform,Newpost
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
class index(ListView):
    model=Post
    template_name='blog/index.html'
    paginate_by = 6

    def get_queryset(self):
        posting=super().get_queryset()
        data=posting.filter(is_published=True)
        return data

class Publish(View):
    def get(self,request,*args,**kwargs):
        id=self.kwargs.get('pk')
        post=Post.objects.get(pk=id)
        post.is_published=True
        post.save()
        return redirect(reverse('blog:dashboard'))



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


class Contact(FormView):
    form_class = Contactform
    template_name = 'blog/contact.html'
    success_url = reverse_lazy('blog:thanks')

    def form_valid(self, form):
        name=form.cleaned_data['name']
        print(name)
        email=form.cleaned_data['email']
        print(email)
        message=form.cleaned_data['message']
        print(message)
        return super().form_valid(form)


class Thanks(TemplateView):
    template_name = 'blog/thanks.html'


class Register(FormView):
    form_class = Registerform
    template_name = 'blog/register.html'
    success_url = reverse_lazy('blog:login')

    def form_valid(self, form):
        form_details=form.save(commit=False)
        user=form.cleaned_data['username']
        print(user)
        email=form.cleaned_data['email']
        print(email)
        password=form.cleaned_data['password']
        form_details.set_password(password)
        form_details.save()

        messages.success(self.request,'your registration was sucessfully done please login')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class Login(FormView):
    form_class = Loginform
    template_name = 'blog/login.html'
    success_url = reverse_lazy('blog:dashboard')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password= form.cleaned_data.get('password')
        user=authenticate(self.request,username=username,password=password)
        if user:
            login(self.request,user)
            messages.success(self.request,'login was successfull')
            return super().form_valid(form)
        else:
            form.add_error(None,'Invalid Username or Password')
            return self.form_invalid(form)


        #return super().form_valid(form)

class Dashboard(ListView):
    model = Post
    template_name = 'blog/dashboard.html'
    paginate_by = 3

    def get_queryset(self):
        querydata=super().get_queryset()
        return querydata.filter(user=self.request.user)




    def get_context_data(self, **kwargs):
        context=super(Dashboard, self).get_context_data()
        context['blog_title']='My Posts'
        return context

class Logout(View):
    def get(self,request):
        return render(request,'blog/logout.html')

    def post(self,request):
            logout(request)
            messages.success(request,'Logged Out Successfully')
            return redirect(reverse('blog:login'))

class New_Post(CreateView):
    model=Post
    form_class = Newpost
    template_name = 'blog/new_post.html'
    success_url = reverse_lazy('blog:dashboard')

    def form_valid(self, form):
        post=form.save(commit=False)
        user=self.request.user
        form.instance.user=user
        return super().form_valid(form)


class Edit_Post(UpdateView):
    model=Post
    fields=['title', 'content', 'img_url','category']
    template_name = 'blog/update.html'
    success_url = reverse_lazy('blog:dashboard')
    context_object_name = 'post'
class Delete_Post(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:dashboard')
