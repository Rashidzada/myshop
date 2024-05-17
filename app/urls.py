from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('blog/',views.blog,name='blog'),
    path('blog_details/',views.blog_details,name='blog_details'),
    path('portfolio_details/',views.portfolio_details,name='portfolio_details'),
    path('services_details/',views.services_details,name='services_details'),
    path('login_view/',views.login_view,name='login_view')
]