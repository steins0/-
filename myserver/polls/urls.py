from django.urls import path

from . import views

urlpatterns = [
    path('<int:number>', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('movie/<int:number>/', views.movies, name='movie'),
    path('movie/<int:number>/<int:user_id>', views.movies_2, name='movie_id_2'),
    path('movie/<int:number>/<int:user_name>/<int:star>/', views.movies_item, name='movies_item'),
]
