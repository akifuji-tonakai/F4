from django.urls import path
from . import views


app_name = 'favo4'
urlpatterns = [
    path('', views.HomeView.as_view(), name="index"),
    path('home/', views.F4ListView.as_view(), name="F4-list"),
    path('F4/<int:pk>-detail/', views.F4DetailView.as_view(), name="F4-detail"),
    path('new/', views.add_content, name="F4-create"),
    path('home/<int:pk>/', views.F4DetailView.as_view(), name="F4-detail"),
    path('home/post/<int:pk>/', views.f4_post_twi_view, name="F4-post-twi"),
]