from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.admin import TokenAdmin

from users.models import User

admin.site.register(User, UserAdmin)
TokenAdmin.raw_id_fields = ["user"]
