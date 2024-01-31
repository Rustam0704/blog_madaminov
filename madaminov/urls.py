from django.urls import path

from madaminov.views import HomePageView, AboutPageView, LoginView, PostFormView, PostDetailView,PostConfirmDeleteView, UserPostsView, RegisterView

app_name = "blog"
urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('about/', AboutPageView.as_view(), name='about-page'),
    path('register/', RegisterView.as_view(), name='register-page'),
    path('login',LoginView.as_view(), name='login-page'),
    path('post/', PostFormView.as_view(), name='post-page'),
    path('post1/', PostDetailView.as_view(), name='post-detail-page'),
    path('post/confirm', PostConfirmDeleteView.as_view(), name='post-confirm-delete-page'),
    path('post/form/', PostFormView.as_view(), name='post-form-page'),
    path('user/posts/', UserPostsView.as_view(), name='user-posts-page'),

]