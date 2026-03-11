from django.contrib import admin
from .models import Contact, Job,CustomUser,Testimonial
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'role', 'is_active', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('phone', 'profile_picture', 'role', 'experience', 'current_job_title', 'education_level', 'bio')}),
    )




@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at', 'approved')
    list_filter = ('approved',)
    search_fields = ('name', 'email', 'message')
    actions = ['approve_testimonials']

    def approve_testimonials(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected testimonials have been approved.")


admin.site.register(CustomUser, CustomUserAdmin)


admin.site.register(Contact)
admin.site.register(Job)

