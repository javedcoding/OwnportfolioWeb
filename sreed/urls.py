from django.urls import path
from . import views

app_name = 'sreed'
urlpatterns = [
    path('', views.sreedConf, name='sreedConf'),
    # path('<int:blog_id>/', views.detail, name='detail'),
]
