from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from employees.models import Employee

# Create your views here.
def home(request):
    employees = Employee.objects.all()
    context = {
        "employees":employees
    }
    print(context)
    return render (request, 'home.html' , context)


def employee_details(request , pk):
    # try:
    #     employ = Employee.objects.get(pk = pk)
    #     print(employ)
    # except:
    #     raise Http404
    # short form
    employee = get_object_or_404(Employee , pk=pk)
    print(employee)
    context = {
        "employee": employee
    }
    return render(request, 'employee_details.html' ,context)