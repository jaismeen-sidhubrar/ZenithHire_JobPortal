from django import forms
from recruiter.models import CustomUser  

class EditJobseekerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['current_job_title', 'bio', 'experience','profile_picture', 'education_level']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }
