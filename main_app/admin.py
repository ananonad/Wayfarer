from django.contrib import admin
from .models import Planet
from .models import Profile

admin.site.register(Planet)
admin.site.register(Profile)