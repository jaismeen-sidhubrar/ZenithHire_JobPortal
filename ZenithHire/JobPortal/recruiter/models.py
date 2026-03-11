from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings  

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True) 
    phone = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True, null=True)
    role = models.CharField(max_length=20, choices=(('jobseeker', 'Jobseeker'), ('recruiter', 'Recruiter')))
    experience = models.CharField(max_length=100, blank=True, null=True)
    current_job_title = models.CharField(max_length=100)
    education_level = models.CharField(max_length=50,blank=True, null=True)
    bio = models.TextField(blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  

    def __str__(self):
        return f"Testimonial by {self.name}"





# contact us 
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name




class Job(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    jobtitle = models.CharField(max_length=100)
    joblocation = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    salary = models.CharField(max_length=50, blank=True)
    job_description = models.TextField()
    job_requirements = models.TextField()
    education_level = models.CharField(max_length=50)
    experience_level = models.CharField(max_length=50)
    industry = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_website = models.URLField(blank=True)
    application_process = models.TextField()
    application_deadline = models.DateField(null=True, blank=True)
    required_documents = models.CharField(max_length=100, blank=True)
    skills_keywords = models.CharField(max_length=100, blank=True)
    work_authorization = models.CharField(max_length=100, blank=True)
    remote_work = models.CharField(max_length=10)
    benefits = models.TextField(blank=True)
    company_values = models.TextField(blank=True)
    contact_info = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.jobtitle


