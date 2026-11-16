from django.urls import path
from .views import CustomLoginView, CustomLogoutView, DashboardView, CustomPasswordChangeView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
]