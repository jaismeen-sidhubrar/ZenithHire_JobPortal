from django.db import models
from recruiter.models import Job 
from django.conf import settings

 
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Contact from {self.name}"

# Testimonial Model
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Testimonial by {self.name}"

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=200)
    applicant_email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending', choices=[
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('rejected', 'Rejected'),
        ('hired', 'Hired')
    ])

    def __str__(self):
        return f"{self.user.email} - {self.job.jobtitle}"
