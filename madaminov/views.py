from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, DetailView, DeleteView


# Create your views here.
class HomePageView(View):
    def get(self, request):
        return render(request, "blog/home.html")

class AboutPageView(TemplateView):
    template_name = "blog/about.html"

class PostFormView(FormView):
    template_name = "blog/post_form.html"

class PostDetailView(ListView):
    template_name = "blog/post_detail.html"

class PostConfirmDeleteView(DeleteView):
    template_name = "blog/post_confirm_delete.html"

class RegisterView(FormView):
    template_name = "blog/register.html"

class UserPostsView(ListView):
    template_name = "blog/user_posts.html"

class LoginView(View):
    template_name = "blog/login.html"


