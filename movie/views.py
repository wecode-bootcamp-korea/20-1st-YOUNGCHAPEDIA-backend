import json, re

from django.http  import JsonResponse, HttpResponse
from django.views import View

from movie.models import Movie, Category, Genre

class MovieRankingView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            Movie.objects.create(
                    kor_title      = data['korean_title'],
                    eng_title      = data['engish_title'],
                    country        = data['country'],
                    release_date   = data['release_date'],
                    running_time   = data['running_time'],
                    discription    = data['discription'],
                    audience_count = data['audience_count'],
                    category       = Category.objects.get(name = data['category']),
                    genre          = Genre.objects.get(name = data['genre'])
            )
            return JsonResponse({'MESSAGE': 'SUCCESS'}, status = 200)

        except KeyError:
            return JsonResponse({'MESSAGE' 'KEY_ERROR'}, status = 400)


    def get(self, request):
        LIMIT = 10
        movie_limit = re.compoile('\d{%d}' % (LIMIT))
        
        #Movie.objects.all().order_by('audience_count')
        movie_ranking_data = Movie.objects.value()

        return JsonResponse({'movie_ranking_data top%d' % (LIMIT): movie_ranking_data, 'MESSAGE': 'SUCCESS'}, status = 200)

