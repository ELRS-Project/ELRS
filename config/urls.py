from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', include('apps.accounts.urls')),
    #path("", views.dashboard, name="dashboard"),
    path('admin/', admin.site.urls),
    path("employees/", include("apps.employees.urls")),
]
