from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('404/', views.page404, name='404'),
    path('news/<slug:news>/', views.news_detail, name='news_detail'),
    path('politics/', views.PoliticsView.as_view(), name='politics'),
    path('business/', views.BusinessView.as_view(), name='business'),
    path('sport/', views.SportView.as_view(), name='sport'),
    path('technology/', views.TechnologyView.as_view(), name='technology'),
]
