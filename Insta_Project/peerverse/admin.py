from django.contrib import admin
from .models import Post,Profile,UserMessage

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(UserMessage)