from django.urls import path
from . import views

urlpatterns=[
    path('', views.recruiterIndex_views, name='recruiter'),
    path('about/', views.recruiter_about_views, name='r_about'),
    path('contact/', views.recruiter_contact_views, name='r_contact'),
    path('testimonial/', views.recruiter_testimonial_views, name='r_testimonial'),
    path('postjob/', views.recruiter_postjob_views, name='r_postjob'),
    path('profile/', views.recruiter_profile_views, name='r_profile'),
    path('profile/edit/', views.edit_recruiter_profile, name='r_edit_profile'),
    path('job/<int:job_id>/applicants/', views.job_applicants_view, name='job_applicants'),
    path('job/delete/<int:job_id>/', views.delete_job_view, name='delete_job'),



]