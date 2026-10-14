from django.db import models

class Department(models.Model):
    id_department = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)


class Employee(models.Model):
    id_employee = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    messenger_link = models.CharField(max_length=255, null=True, blank=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )


class Project(models.Model):
    id_project = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50)
    start_date = models.DateField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)

    manager = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )


class TaskType(models.Model):
    id_type = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=255)


class Task(models.Model):
    id_task = models.AutoField(primary_key=True)

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )
    type = models.ForeignKey(
        TaskType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    estimated_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    assignee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tasks',
    )
    author = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='authored_tasks',
    )


class TaskLink(models.Model):
    id_task_link = models.AutoField(primary_key=True)

    source_task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='source_links',
    )
    target_task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='target_links',
    )
    link_type = models.CharField(max_length=50, null=True, blank=True)


class ProjectRole(models.Model):
    id_role = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255)


class ProjectParticipation(models.Model):
    id_participation = models.AutoField(primary_key=True)

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
    )
    role = models.ForeignKey(
        ProjectRole,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    joined_at = models.DateField(null=True, blank=True)


class TimeEntry(models.Model):
    id_entry = models.AutoField(primary_key=True)

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
    )
    work_date = models.DateField(null=True, blank=True)
    hours_spent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
