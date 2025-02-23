from django.urls import path
from base import views

urlpatterns=[
  path('',views.home,name='home'),
  path('article_details/<int:detail_id>',views.article_details,name='article_details'),
  path('about/',views.about,name='about'),
  path('read/<int:pk>',views.read,name='read'),
  path('news',views.news,name='news'),
  path('news_post/<int:id>',views.news_post,name='news_post'),
  path('events/',views.events,name='events'),
  path('events_details/<int:event_id>',views.events_details,name='events_details'),
]