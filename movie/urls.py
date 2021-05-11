from django.urls import path

from movie.views import MovieRankingView

urlpatterns = [
    path('', MovieRankingView.as_view()),
]
