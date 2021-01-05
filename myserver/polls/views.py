from django.http import HttpResponse
from .models import Question
from .models import movie,user,movie_itme
from django.template import loader
from django.shortcuts import render

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
def index(request, number):
    now_user = user.objects.get(id = number)
    template = loader.get_template('polls/index.html')
    context = {
        'user_name': now_user.username,
        'user_id':now_user.id
    }
    return HttpResponse(template.render(context, request))

def movies(request, number):
    latest_movie_list = movie.objects.get(id=number)
    url = 'polls/movie_'+str(number)+'.html'
    template = loader.get_template(url)
    latest_movie_list.moviestar = (float)(latest_movie_list.moviestar/10)
    context = {
        'id': 0 ,
        'latest_movie_list': latest_movie_list,
        'username':'user1'
    }
    return HttpResponse(template.render(context, request))

def movies_2(request, number , user_id):
    latest_movie_list = movie.objects.get(id=number)
    now_user = user.objects.get(id = user_id)
    latest_movie_itme = movie_itme.objects.filter(moviename = latest_movie_list.moviename)
    for dx in latest_movie_itme:
        if dx.username == now_user.username:
            star = (float)(dx.moviestar/10)
            context = {
                'id': 1,
                'user_name': now_user.username,
                'user_id':now_user.id,
                'star':star,
                'latest_movie_list':latest_movie_list
            }
            url = 'polls/movie_'+str(number)+'.html'
            template = loader.get_template(url)
            return HttpResponse(template.render(context, request))
    latest_movie_list.moviestar = (float)(latest_movie_list.moviestar/10)
    context = {
        'id': 0,
        'user_name': now_user.username,
        'user_id':now_user.id,
        'latest_movie_list': latest_movie_list,
    }
    url = 'polls/movie_'+str(number)+'.html'
    template = loader.get_template(url)
    return HttpResponse(template.render(context, request))

def movies_item(request, number, user_name, star):
    latest_movie = movie.objects.get(id = number)
    latest_user = user.objects.get(id = user_name)
    # latest_movie_itme_list = movie_itme.objects.filter(username = user_name)
    # for letter in latest_movie_itme_list:
    #     if letter.moviename == latest_movie.moviename:
    #         break
    addmovie_item = movie_itme(moviename=latest_movie.moviename,username=latest_user.username,moviestar=star)
    addmovie_item.save()
    latest_movie.moviestar = (latest_movie.moviestar*latest_movie.people+star)/(latest_movie.people+1)
    latest_movie.people=latest_movie.people+1
    latest_movie.save()
    url = 'polls/movie_'+str(number)+'.html'
    template = loader.get_template(url)
    latest_movie.moviestar = (float)(latest_movie.moviestar/10)
    context = {
        'id': 1,
        'user_id': latest_user.id,
        'user_name': latest_user.username,
        'star':star,
        'latest_movie_list':latest_movie
    }
    return HttpResponse(template.render(context, request))

def login(request):
    if request.method == 'GET':
        return render(request, 'polls/login.html')
    if request.method == "POST":
        now_username = request.POST.get('username')
        now_password = request.POST.get('password')
        try:
            now_user = user.objects.get(username = now_username)
            if(now_user.password == now_password):
                print(now_username,now_password)
                template = loader.get_template('polls/index.html')
                context = {
                    'user_name': now_user.username,
                    'user_id':now_user.id
                }
                return HttpResponse(template.render(context, request))
            template = loader.get_template('polls/login.html')
            context = {
                'message': '密码错误'
            }
            return HttpResponse(template.render(context, request))
        except:
            template = loader.get_template('polls/login.html')
            context = {
                'message': '无此用户'
            }
            return HttpResponse(template.render(context, request))
