from django.contrib import admin
from .models import Post, Schedule

# 관리자(admin)가 게시글(Post)에 접근 가능
admin.site.register(Post)
admin.site.register(Schedule)
