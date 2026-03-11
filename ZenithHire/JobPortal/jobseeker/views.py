from django.shortcuts import render, redirect
from django.contrib import messages
from recruiter.models import Contact, CustomUser, Job
from jobseeker.models import Testimonial,Application
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EditJobseekerProfileForm
from django.contrib.auth import get_user_model


@login_required
def jobseekerIndex_views(request):
    return render(request, 'jobseeker/jobseeker_index.html')

@login_required
def jobseeker_about_views(request):
    return render(request, 'jobseeker/jobseeker_about.html')

@login_required
def jobseeker_contact_views(request):
    error_msg = None  # Start with no error message

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Validation:
        if not name or not email or not message:
            error_msg = "All fields are required"
        else:
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(request, "Thank you! Your message has been sent.") 
    return render(request, 'jobseeker/jobseeker_contact.html', {'error_msg': error_msg})

@login_required
def jobseeker_testimonial_views(request):
    testimonials = Testimonial.objects.filter(approved=True).order_by('-created_at')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if not name or not email or not message:
            messages.error(request, "All fields are required")
        else:
            Testimonial.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(request, "Thank you! Your testimonial is pending approval")    
    return render(request, 'jobseeker/jobseeker_testimonial.html', {'testimonials': testimonials})

@login_required
def jobseeker_findjob_view(request):
    jobs = Job.objects.all().order_by('-id')
    
    # Filters
    location_filter = request.GET.get('location')
    title_filter = request.GET.get('title')
    
    if location_filter:
        jobs = jobs.filter(joblocation__icontains=location_filter)
    if title_filter:
        jobs = jobs.filter(jobtitle__icontains=title_filter)
    
    paginator = Paginator(jobs, 6)
    page = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    return render(request, 'jobseeker/jobseeker_findjob.html', {
        'page_obj': page_obj,
        'location': location_filter,
        'title': title_filter
    })









@login_required
def jobseeker_apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        resume = request.FILES.get('resume') 
        
        # Validation
        if not all([name, email, resume]):
            messages.error(request, "All fields are required!")
            return redirect('job_detail', job_id=job.id)
            
        try:
            Application.objects.create(
                job=job,
                user=request.user,
                applicant_name=name,
                applicant_email=email,
                resume=resume
            )
            messages.success(request, "Application submitted successfully!")
            return redirect('findjob')
            
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect('job_detail', job_id=job.id)
    
    return redirect('findjob')


    


@login_required
def job_detail_view(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobseeker/jobseeker_jobdetail.html', {'job': job})


@login_required
def jobseeker_profile_view(request):
    CustomUser = get_user_model()
    user = CustomUser.objects.get(id=request.user.id)  
    return render(request, 'jobseeker/jobseeker_profile.html', {'user': user})



@login_required
def edit_jobseeker_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditJobseekerProfileForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('js_profile')
    else:
        form = EditJobseekerProfileForm(instance=user)

    return render(request, 'jobseeker/jobseeker_edit_profile.html', {'form': form,'user':user})


