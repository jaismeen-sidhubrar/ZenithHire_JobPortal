from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout , get_user_model
from .models import CustomUser,Job , Contact,Testimonial
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from jobseeker.models import Application
from django.core.mail import send_mail
from .forms import EditRecruiterProfileForm





def home(request):
    return render(request,'recruiter/home.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        profile_picture = request.FILES.get('profile_picture')
        role = request.POST.get('role')
        experience = request.POST.get('experience')
        current_job_title = request.POST.get('current_job_title')
        education_level = request.POST.get('education_level')
        bio = request.POST.get('bio')

        if password != cpassword:
            messages.error(request, 'Passwords do not match')
        elif CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
        else:
            try:
                validate_password(password)
                user = CustomUser.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    phone=phone,
                    profile_picture=profile_picture,
                    role=role,
                    experience=experience,
                    current_job_title=current_job_title,
                    education_level=education_level,
                    bio=bio
                )

                if role == 'recruiter':
                    subject = 'Welcome to ZenithHire - Let’s Find Your Next Hire'
                    message_lines = [
                        f"Hi {username},",
                        "",
                        "Thanks for signing up as a recruiter on ZenithHire.",
                        "You can now create job listings and connect with qualified candidates.",
                        "",
                        "",
                        "Need any help? Reach out to us anytime at zenithhire365@gmail.com",
                        "",
                        "Best regards,",
                        "The ZenithHire Team"
                    ]
                else:
                    subject = 'Welcome to ZenithHire - Let’s Find Your Dream Job'
                    message_lines = [
                        f"Hi {username},",
                        "",
                        "Welcome to ZenithHire! You've successfully registered as a job seeker.",
                        "Start exploring new job opportunities and apply with just a few clicks.",
                        
                        "If you need assistance, we’re here for you ",
                        "",
                        "Wishing you all the best,",
                        "The ZenithHire Team"
                    ]

                message = "\n".join(message_lines)

                send_mail(
                    subject=subject,
                    message=message,
                    from_email='ZenithHire <zenithhire365@gmail.com>',
                    recipient_list=[email],
                    fail_silently=False,
                  
                )

                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login')

            except ValidationError as e:
                for error in e:
                    messages.error(request, error)

    return render(request, 'recruiter/signup.html')





def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        user = authenticate(request, email=email, password=password)
        if user is not None and user.role == role:
            login(request, user)

            subject = 'Login Alert - Job Portal'
            message_lines = [
                f"Hi {user.username},",
                "",
                "You’ve successfully logged into your ZenithHire account.",
                "",
                "If this wasn’t you, please change your password immediately to secure your account.",
                "",
                "If you need help, feel free to reach out to our support team .",
                "",
                "Best regards,",
                "The ZenithHire Team"
            ]
            
            message = "\n".join(message_lines)

            send_mail(
                subject=subject,
                message=message,
                from_email='ZenithHire <zenithhire365@gmail.com>',
                recipient_list=[user.email],
                fail_silently=False,
               
            )

            if user.role == 'recruiter':
                return redirect('recruiter')
            elif user.role == 'jobseeker':
                return redirect('jobseeker')

        else:
            messages.error(request, 'Invalid credentials or role mismatch')

    return render(request, 'recruiter/login.html')



@login_required
def recruiterIndex_views(request):
    return render(request,'recruiter/recruiter_index.html')

@login_required
def recruiter_about_views(request):
    return render(request,'recruiter/recruiter_about.html')

@login_required
def recruiter_postjob_views(request):
    if request.method == 'POST':
        job = Job.objects.create(
            user=request.user, 
            jobtitle=request.POST.get('jobtitle'),
            joblocation=request.POST.get('joblocation'),
            job_type=request.POST.get('job_type'),
            salary=request.POST.get('salary'),
            job_description=request.POST.get('job_description'),
            job_requirements=request.POST.get('job_requirements'),
            education_level=request.POST.get('education_level'),
            experience_level=request.POST.get('experience_level'),
            industry=request.POST.get('industry'),
            company_name=request.POST.get('company_name'),
            company_website=request.POST.get('company_website'),
            application_process=request.POST.get('application_process'),
            application_deadline=request.POST.get('application_deadline'),
            required_documents=request.POST.get('required_documents'),
            skills_keywords=request.POST.get('skills_keywords'),
            work_authorization=request.POST.get('work_authorization'),
            remote_work=request.POST.get('remote_work'),
            benefits=request.POST.get('benefits'),
            company_values=request.POST.get('company_values'),
            contact_info=request.POST.get('contact_info'),
        )
        messages.success(request, "Job posted successfully!")
        return redirect('r_postjob')  
    jobs = Job.objects.filter(user=request.user).order_by('-created_at')  
    return render(request, 'recruiter/recruiter_postjob.html', {'jobs': jobs})



@login_required
def recruiter_profile_views(request):
    CustomUser = get_user_model()
    user = CustomUser.objects.get(id=request.user.id) 
    return render(request, 'recruiter/recruiter_profile.html', {'user': user})


@login_required
def edit_recruiter_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditRecruiterProfileForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('r_profile')
    else:
        form = EditRecruiterProfileForm(instance=user)

    return render(request, 'recruiter/recruiter_edit_profile.html', {'form': form,'user':user})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def recruiter_testimonial_views(request):
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
            return redirect('r_testimonial')

    return render(request, 'recruiter/recruiter_testimonials.html', {'testimonials': testimonials})


def recruiter_contact_views(request):
    error_msg = None  
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if not name or not email or not message:
            error_msg = "All fields are required"
        else:
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(request, "Thank you! Your message has been sent.") 
            return redirect('r_contact')  
    return render(request, 'recruiter/recruiter_contact.html')  




 

@login_required
def job_applicants_view(request, job_id):
    job = get_object_or_404(Job, id=job_id, user=request.user)
    applications = Application.objects.filter(job=job)
    return render(request, 'recruiter/recruiter_applicants.html', {
        'job': job,
        'applications': applications
    })


@login_required
def delete_job_view(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == "POST":
        job.delete()
        messages.success(request, f"Job '{job.jobtitle}' deleted successfully.")
        return redirect('r_postjob')
    return redirect('r_postjob')

