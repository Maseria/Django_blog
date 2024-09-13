from django.contrib import admin
from .models import Post

# register models for viewing in admin site
admin.site.register(Post)