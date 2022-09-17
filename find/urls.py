from django.urls import path
from . import views

urlpatterns = [

    path('bars/', views.BarList.as_view(), name='bar_list'),
    path('bars/<int:pk>', views.BarDetail.as_view(), name='bar_detail'),
    path('comments/<int:pk>', views.CommmentDetail.as_view(), name='comment_detail'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('bar/new', views.BarDetail.as_view(), name='bar_create'),
    path('comment/new', views.CommmentDetail.as_view(), name='comment_create'),
    path('games/new', views.GameDetail.as_view(), name='games_create'),
    path('games/', views.GameList.as_view(), name='game_list'),
    
    # path('bars/<int:pk>/delete', views.bar_delete, name='bar_delete'),
    # path('comments/<int:pk>/delete', views.comment_delete, name='comment_delete'),


]