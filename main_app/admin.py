from lib2to3.pgen2.token import COMMENT
from django.contrib import admin
from .models import Planet
from .models import Profile, Comment

admin.site.register(Planet)
admin.site.register(Profile)
admin.site.register(Comment)