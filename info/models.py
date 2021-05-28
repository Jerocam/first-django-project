from django.db import models

class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=35)
    min_salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    max_salary = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'

class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    hire_date = models.DateField()
    job = models.ForeignKey('Jobs', models.DO_NOTHING)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    manager = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey('Departments', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'

class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=30)
    location = models.ForeignKey('Locations', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'

class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    street_address = models.CharField(max_length=40, blank=True, null=True)
    postal_code = models.CharField(max_length=12, blank=True, null=True)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=25, blank=True, null=True)
    country = models.ForeignKey('Countries', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'locations'

class Regions(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions'

class EmployeesGreeting(models.Model):
    id = models.BigAutoField(primary_key=True)
    when = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'employees_greeting'

class Dependents(models.Model):
    dependent_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=25)
    employee = models.ForeignKey('Employees', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dependents'

class Countries(models.Model):
    country_id = models.CharField(primary_key=True, max_length=2)
    country_name = models.CharField(max_length=40, blank=True, null=True)
    region = models.ForeignKey('Regions', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'countries'