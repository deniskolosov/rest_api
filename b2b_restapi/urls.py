from django.urls import include, path
from django.contrib import admin


from rest_api import views

urlpatterns = [
    path('api/', include('rest_api.urls')),
    path('admin/', admin.site.urls),
]

