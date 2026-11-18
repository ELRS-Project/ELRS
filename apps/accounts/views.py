from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm, CustomPasswordChangeForm

class CustomLoginView(LoginView):
    """Handle user authentication using a custom Bootstrap template."""
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    """Log out the user via POST request and redirect to the login page."""
    next_page = reverse_lazy('login')


class DashboardView(LoginRequiredMixin, TemplateView):
    """Render the main system dashboard for authenticated users."""
    template_name = 'dashboard/index.html'

class RegisterView(CreateView):
    """Handle new user registration and automatically log them in."""
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """Allow authenticated users to change their own password."""
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('dashboard')

class DashboardView(LoginRequiredMixin, TemplateView):
    """Render the main system dashboard."""
    template_name = 'dashboard/index.html'