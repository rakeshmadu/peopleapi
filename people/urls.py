from django.urls import path
from.views import get_name,post_fav,get_sample,get_all
urlpatterns = [
    path('name/',get_name),
    path('post/',post_fav),
    path('samp/',get_sample),
    path('all/',get_all)
    
]