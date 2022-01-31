from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from project.models import User,Project,Issue,Comment,Contributor

admin.site.register(User,UserAdmin)
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(Comment)
admin.site.register(Contributor)
