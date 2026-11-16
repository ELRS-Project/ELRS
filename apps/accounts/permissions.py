from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Access control mixin restricting view access exclusively to users
    with the Administrator role.
    """
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin


class ITManagerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Access control mixin restricting view access to users with
    IT Manager or Administrator privileges.
    """
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_it_manager