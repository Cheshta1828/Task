from django.contrib import admin

# Register your models here.
from .models import auth,customer
admin.site.register(auth)
admin.site.register(customer)