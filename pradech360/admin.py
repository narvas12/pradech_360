from django.contrib import admin
from .models import Blog, For_creatives, For_partnership
# Register your models here.

admin.site.register(Blog)
admin.site.register(For_partnership)
admin.site.register(For_creatives)
