from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('accountant', 'Accountant'),
        ('guest', 'Guest'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('staff', 'Staff'),
        ('parent', 'Parent'),
        ('alumni', 'Alumni'),
        ('visitor', 'Visitor'),
        ('researcher', 'Researcher'),
        ('volunteer', 'Volunteer'),
        ('contractor', 'Contractor'),
        ('intern', 'Intern'),
        ('consultant', 'Consultant'),
        ('partner', 'Partner'),
        ('sponsor', 'Sponsor'),
        ('donor', 'Donor'),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    # Extra fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # username still required unless removed

    def __str__(self):
        return f"{self.first_name or self.username} ({self.email})"

