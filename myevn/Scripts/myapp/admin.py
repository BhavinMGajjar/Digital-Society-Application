from django.contrib import admin
from . models import User, Watchmen, Events

# Register your models here.
admin.site.register(User)
admin.site.register(Watchmen)
admin.site.register(Events)
