from django import forms
from .models import CustomUser  

class EditRecruiterProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['current_job_title', 'bio', 'experience','profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }
