from django.urls import path
from . import views


app_name = 'favo4'
urlpatterns = [
    path('', views.HomeView.as_view(), name="index"),
    path('home/', views.F4ListView.as_view(), name="F4-list"),
    path('new/', views.add_content, name="F4-create"),
    path('home/post/<int:pk>/', views.f4_post_twi_view, name="F4-post-twi"),
    path('mypage/<slug:username>/', views.F4UserPageView.as_view(), name="F4-user-page"),
    path('regulations/', views.F4RegulationsView.as_view(), name="F4-regulations"),
    path('inquiry/', views.F4InquiryView.as_view(), name="F4-inquiry"),
    path('withdrawal/<int:pk>/', views.F4WithdrawalView.as_view(), name="F4-withdrawal"),
]
