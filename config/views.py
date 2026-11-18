from django.shortcuts import render


def dashboard(request):
    """Display the main system dashboard."""

    return render(request, "dashboard/dashboard.html")