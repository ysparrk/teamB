from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('ott/', views.ott_list, name='ott_list'),  # ott 리스트 보내기
    path('tmdb/<str:initial>', views.tmdb_movie_list, name='tmdb_movie_list'), # initial 받아서, 해당하는 ott리스트 보내주기
    path('detail/<int:movie_id>', views.movie_detail, name='movie_detail'), 
    path('<int:movie_id>/likes/', views.likes, name='likes'), # 좋아요 기능

    # comment
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:movie_pk>/comments/', views.comment_create),

    ############################################
    ############################################
    path('search/<str:query>/', views.search_movies, name='search_movies'),
    ############################################
    ############################################

]
