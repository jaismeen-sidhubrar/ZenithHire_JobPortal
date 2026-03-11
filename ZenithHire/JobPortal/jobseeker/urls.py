from django.urls import path
from . import views

urlpatterns = [
    path('', views.jobseekerIndex_views, name='jobseeker'),
    path('about/', views.jobseeker_about_views, name='js_about'),
    path('contact/', views.jobseeker_contact_views, name='js_contact'),
    path('testimonial/', views.jobseeker_testimonial_views, name='js_testimonial'),
    path('job/<int:job_id>/', views.job_detail_view, name='job_detail'),
    path('apply/<int:job_id>/', views.jobseeker_apply_for_job, name='jobseeker_apply_for_job'),
    path('findjob/', views.jobseeker_findjob_view, name='findjob'),
    path('profile/', views.jobseeker_profile_view, name='js_profile'),
    path('profile/edit/', views.edit_jobseeker_profile, name='js_edit_profile'),

]