from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from django.http import HttpResponse

# def home(request):
#     return render(request, 'home.html')

def add_employee(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        designation = request.POST.get('designation')
        degree = request.POST.get('degree')
        specialization = request.POST.get('specialization')
        department = request.POST.get('department')
        university = request.POST.get('university')
        year = request.POST.get('year_of_attaining_higher_qualification')
        publications = request.POST.get('research_publications')
        phd_guidance = request.POST.get('phd_guidance')
        phd_received = request.POST.get('faculty_received_phd_in_assessment_year') == 'on'
        phd_during_year = request.POST.get('phd_during_the_assessment_year')
        teaching_exp = request.POST.get('years_of_teaching_experience')
        assoc_prof_exp = request.POST.get('years_as_associate_professor')
        industry_exp = request.POST.get('industry_experience_years')
        doj = request.POST.get('date_of_joining')
        associated = request.POST.get('currently_associated') == 'on'
        dol = request.POST.get('date_of_leaving') or None
        salary = request.POST.get('salary')

        emp = Employee(
            id=id,
            name=name,
            gender=gender,
            designation=designation,
            degree=degree,
            specialization=specialization,
            department=department,
            university=university,
            year_of_attaining_higher_qualification=year,
            research_publications=publications,
            phd_guidance=phd_guidance,
            faculty_received_phd_in_assessment_year=phd_received,
            phd_during_the_assessment_year=phd_during_year,
            years_of_teaching_experience=teaching_exp,
            years_as_associate_professor=assoc_prof_exp,
            industry_experience_years=industry_exp,
            date_of_joining=doj,
            currently_associated=associated,
            date_of_leaving=dol,
            salary=salary,
        )
        emp.save()
        # return redirect('all_employees')
         # return render(request, 'employee_app/add_employee.html')
    return render(request, 'add_employee.html')

# def delete_employee(request, emp_id):
#     emp = get_object_or_404(Employee, id=emp_id)
#     emp.delete()
#     return redirect('all_employees')

# def promote_employee(request, emp_id):
#     emp = get_object_or_404(Employee, id=emp_id)
#     if request.method == 'POST':
#         try:
#             amount = float(request.POST.get('amount'))
#             emp.salary += amount
#             emp.save()
#             return redirect('all_employees')
#         except:
#             return HttpResponse("Invalid amount")
#     return render(request, 'promote_employee.html', {'employee': emp})

# def all_employees(request):
#     employees = Employee.objects.all()
    return render(request, 'all_employees.html', {'employees': employees})
