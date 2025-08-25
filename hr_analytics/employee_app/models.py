from django.db import models

class Employee(models.Model):
    DESIGNATION_CHOICES = [
        ('assistant_professor', 'Assistant Professor'),
        ('associate_professor', 'Associate Professor'),
        ('professor_of_practice', 'Professor of Practice'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    NATURE_OR_ASSOCIATION_CHOICES = [
        ('regular','Regular'),
        ('contract','Contract')
    ]
    # Employee Basic Info
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)
    degree = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    year_of_attaining_higher_qualification = models.PositiveIntegerField()

    # Experience and Research
    research_publications = models.PositiveIntegerField(default=0)
    phd_guidance = models.PositiveIntegerField(default=0)
    faculty_received_phd_in_assessment_year = models.BooleanField(default=False)
    phd_during_the_assessment_year = models.PositiveIntegerField(default=0)
    years_of_teaching_experience = models.PositiveIntegerField(default=0)
    years_as_associate_professor = models.PositiveIntegerField(default=0)
    industry_experience_years = models.FloatField(default=0.0)

    # Job Status
    date_of_joining = models.DateField()
    currently_associated = models.BooleanField(default=True)
    date_of_leaving = models.DateField(null=True, blank=True)

    # Salary
    salary = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.name} - {self.designation}"