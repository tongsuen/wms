from django.contrib import admin
from accounts.models import Address,Driver
from django.contrib.auth import get_user_model
# Register your models here.
User = get_user_model()

admin.site.register(User)
admin.site.register(Address)
admin.site.register(Driver)
