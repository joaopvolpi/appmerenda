from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()


admin.site.register(User)
admin.site.register(Marmita)


