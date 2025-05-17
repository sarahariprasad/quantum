from django.contrib import admin
from django.utils.html import format_html




from .models import PosterView, OurStory, AboutBanner, AboutUs, AboutDeals, Job, JobApplication, CareerBanner,Service, ContactMessage, ContactBanner,TrainingVideo

# Register your models here.

@admin.register(PosterView)
class PosterAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'subtitle']

@admin.register(OurStory)
class OurStoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'description2']

@admin.register(AboutBanner)
class AboutBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title','description', 'description2', 'image']


@admin.register(AboutDeals)
class AboutDealsAdmin(admin.ModelAdmin):
    list_display = ['title','number']

#### services admin ####

@admin.register(Service)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title', 'short_description', 'long_description', 'image', 'bannerimage', 'decimage']
    prepopulated_fields = {"slug": ("title",)}

### services admin end ####


###### careers admin ######################

@admin.register(CareerBanner)
class CareerBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_type', 'education', 'posted_on')
    search_fields = ('title', 'education')
    list_filter = ('job_type', 'posted_on')
    ordering = ('-posted_on',)

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job', 'applied_on')
    search_fields = ('name', 'email', 'job__title')
    list_filter = ('applied_on', 'job')
    readonly_fields = ('applied_on',)
    ordering = ('-applied_on',)

    # Optional: Show a download link for resumes
    def resume_link(self, obj):
        if obj.resume:
            return format_html('<a href="{}" download>Download</a>', obj.resume.url)
        return "-"
    resume_link.short_description = "Resume"

@admin.register(TrainingVideo)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_file','uploaded_on' )
########### end forms admin ################


######### Contact form admin ##################

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']

@admin.register(ContactBanner)
class ContactBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    


############ Ended Contact form ##############
