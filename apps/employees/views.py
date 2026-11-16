from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from .models import Employee


def employee_list(request):
    """Display a searchable, filterable and paginated employee list."""

    employees = Employee.objects.all()

    search_query = request.GET.get("search", "").strip()
    department = request.GET.get("department", "").strip()
    status = request.GET.get("status", "").strip()

    if search_query:
        employees = employees.filter(
            Q(first_name__icontains=search_query)
            | Q(last_name__icontains=search_query)
            | Q(email__icontains=search_query)
        )

    if department:
        employees = employees.filter(department=department)

    if status == "active":
        employees = employees.filter(is_active=True)
    elif status == "inactive":
        employees = employees.filter(is_active=False)

    paginator = Paginator(employees, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    departments = (
        Employee.objects
        .values_list("department", flat=True)
        .distinct()
        .order_by("department")
    )

    context = {
        "page_obj": page_obj,
        "departments": departments,
        "search_query": search_query,
        "selected_department": department,
        "selected_status": status,
    }

    return render(request, "employees/employee_list.html", context)
