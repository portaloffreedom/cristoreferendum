from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vote/create/', views.create_new_choice, name='create_choice'),
    url(r'^vote/', views.vote_current_poll, name='vote'),
    url(r'^winner/', views.visualize_last_winner, name='winner'),
]