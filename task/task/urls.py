from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    # Add other URL patterns if needed
   
]
