from django.contrib import admin
from .models import Contact,Testimonial,Application




@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at', 'approved')
    list_filter = ('approved',)
    search_fields = ('name', 'email', 'message')
    actions = ['approve_testimonials']

    def approve_testimonials(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected testimonials have been approved.")




@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant_name', 'job', 'applied_at', 'status')
    list_filter = ('status', 'applied_at')
    search_fields = ('applicant_name', 'job__jobtitle')


admin.site.register(Contact)

