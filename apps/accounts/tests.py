import pytest
from django.urls import reverse
from apps.accounts.models import User


@pytest.mark.django_db
def test_dashboard_redirects_anonymous_user(client):
    """Ensure unauthenticated users are redirected to the login page."""
    response = client.get(reverse('dashboard'))
    assert response.status_code == 302
    assert reverse('login') in response.url


@pytest.mark.django_db
def test_user_roles_properties():
    """Verify role hierarchy properties (is_admin, is_it_manager) for all user roles."""
    admin_user = User.objects.create_user(username='admin1', password='password123', role=User.Role.ADMIN)
    manager_user = User.objects.create_user(username='mgr1', password='password123', role=User.Role.IT_MANAGER)
    emp_user = User.objects.create_user(username='emp1', password='password123', role=User.Role.EMPLOYEE)

    assert admin_user.is_admin is True
    assert admin_user.is_it_manager is True

    assert manager_user.is_admin is False
    assert manager_user.is_it_manager is True

    assert emp_user.is_admin is False
    assert emp_user.is_it_manager is False


@pytest.mark.django_db
def test_login_success(client):
    """Verify that valid credentials log the user in and redirect to the dashboard."""
    User.objects.create_user(username='janek', password='secretpassword123')
    response = client.post(reverse('login'), {'username': 'janek', 'password': 'secretpassword123'})
    assert response.status_code == 302
    assert response.url == reverse('dashboard')