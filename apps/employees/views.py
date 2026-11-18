from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .forms import EmployeeForm
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

def employee_create(request):
    """Handle the creation of a new employee."""

    if request.method == "POST":
        form = EmployeeForm(request.POST)

        if form.is_valid():
            employee = form.save()
            return redirect(
                "employees:employee_detail",
                pk=employee.pk
            )
    else:
        form = EmployeeForm()

    return render(
        request,
        "employees/employee_form.html",
        {
            "form": form,
            "page_title": "Add employee",
        }
    )

def employee_detail(request, pk):
    """Display the details of a selected employee."""

    employee = get_object_or_404(Employee, pk=pk)

    return render(
        request,
        "employees/employee_detail.html",
        {
            "employee": employee,
        }
    )

def employee_edit(request, pk):
    """Handle updating an existing employee."""

    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect(
                "employees:employee_detail",
                pk=employee.pk
            )
    else:
        form = EmployeeForm(instance=employee)

    return render(
        request,
        "employees/employee_form.html",
        {
            "form": form,
            "page_title": "Edit employee",
            "employee": employee,
        }
    )

def employee_delete(request, pk):
    """Handle the deletion of an employee."""

    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        employee.delete()
        return redirect("employees:employee_list")

    return render(
        request,
        "employees/employee_confirm_delete.html",
        {
            "employee": employee,
        }
    )