from django.shortcuts import render
from .models import *


def department_list(request):
    departments = Department.objects.all()

    search = request.GET.get('search', '')
    if search:
        departments = departments.filter(name__icontains=search)

    context = {
        'departments': departments,
        'search': search,
    }
    return render(request, 'department_table.html', context)


def employee_list(request):
    employees = Employee.objects.select_related('department').all()

    search = request.GET.get('search', '')
    if search:
        employees = employees.filter(full_name__icontains=search)

    filter_department = request.GET.get('filter_department', '')
    if filter_department:
        employees = employees.filter(department_id=filter_department)

    departments = Department.objects.all()

    context = {
        'employees': employees,
        'departments': departments,
        'search': search,
        'filter_department': filter_department,
    }
    return render(request, 'employee_table.html', context)


def project_list(request):
    projects = Project.objects.select_related('manager').all()

    search = request.GET.get('search', '')
    if search:
        projects = projects.filter(name__icontains=search)

    filter_status = request.GET.get('filter_status', '')
    if filter_status:
        projects = projects.filter(status=filter_status)

    statuses = Project.objects.values_list('status', flat=True).distinct()

    context = {
        'projects': projects,
        'statuses': statuses,
        'search': search,
        'filter_status': filter_status,
    }
    return render(request, 'project_table.html', context)


def task_type_list(request):
    task_types = TaskType.objects.all()

    search = request.GET.get('search', '')
    if search:
        task_types = task_types.filter(type_name__icontains=search)

    context = {
        'task_types': task_types,
        'search': search,
    }
    return render(request, 'task_type_table.html', context)


def task_list(request):
    tasks = Task.objects.select_related('project', 'type', 'assignee', 'author').all()

    search = request.GET.get('search', '')
    if search:
        tasks = tasks.filter(title__icontains=search)

    filter_status = request.GET.get('filter_status', '')
    if filter_status:
        tasks = tasks.filter(status=filter_status)

    statuses = Task.objects.values_list('status', flat=True).distinct()

    context = {
        'tasks': tasks,
        'statuses': statuses,
        'search': search,
        'filter_status': filter_status,
    }
    return render(request, 'task_table.html', context)


def task_link_list(request):
    task_links = TaskLink.objects.select_related('source_task', 'target_task').all()

    filter_link_type = request.GET.get('filter_link_type', '')
    if filter_link_type:
        task_links = task_links.filter(link_type=filter_link_type)

    link_types = TaskLink.objects.values_list('link_type', flat=True).distinct()

    context = {
        'task_links': task_links,
        'link_types': link_types,
        'filter_link_type': filter_link_type,
    }
    return render(request, 'task_link_table.html', context)


def project_role_list(request):
    roles = ProjectRole.objects.all()

    search = request.GET.get('search', '')
    if search:
        roles = roles.filter(role_name__icontains=search)

    context = {
        'roles': roles,
        'search': search,
    }
    return render(request, 'project_role_table.html', context)


def project_participation_list(request):
    participations = ProjectParticipation.objects.select_related(
        'project', 'employee', 'role'
    ).all()

    filter_project = request.GET.get('filter_project', '')
    if filter_project:
        participations = participations.filter(project_id=filter_project)

    projects = Project.objects.all()

    context = {
        'participations': participations,
        'projects': projects,
        'filter_project': filter_project,
    }
    return render(request, 'project_participation_table.html', context)


def time_entry_list(request):
    entries = TimeEntry.objects.select_related('task', 'employee').all()

    filter_employee = request.GET.get('filter_employee', '')
    if filter_employee:
        entries = entries.filter(employee_id=filter_employee)

    employees = Employee.objects.all()

    context = {
        'entries': entries,
        'employees': employees,
        'filter_employee': filter_employee,
    }
    return render(request, 'time_entry_table.html', context)