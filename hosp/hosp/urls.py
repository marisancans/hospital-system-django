from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path(r'', include('app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # new
]


AUTH_USER_MODEL = "app.CustomUser" 