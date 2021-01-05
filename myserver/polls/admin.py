from django.contrib import admin
from .models import Question
from .models import user,movie_itme,movie


admin.site.register(Question)
admin.site.register(user)
admin.site.register(movie_itme)
admin.site.register(movie)
# Register your models here.
