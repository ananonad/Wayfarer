from lib2to3.pgen2.token import COMMENT
from django.contrib import admin
from .models import Planet
from .models import User, Comment

admin.site.register(Planet)
admin.site.register(User)
admin.site.register(Comment)
