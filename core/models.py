from django.db import models
from django.utils.text import slugify

# Create your models here.

class PosterView(models.Model):
    image = models.ImageField(upload_to='images/banner', default='images/default.png')
    title = models.CharField(max_length=100)
    subtitle = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
class OurStory(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(blank=True)
    description = models.TextField(max_length=1000)
    description2 = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='images/story', default=None)

    def __str__(self):
        return self.title
    
class AboutBanner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/about', default=None)


    def __str__(self):
        return self.title
    
class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    description2 = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/about', default=None)
    

    def __str__(self):
        return self.title
    
class AboutDeals(models.Model):
    title = models.CharField(max_length=100)
    number = models.CharField(max_length=100)

    def __str__(self):
        return self.title


############# Careers page design #################

class CareerBanner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField('images/career', default=None)

    def __str__(self):
        return self.title

class Job(models.Model):
    title = models.CharField(max_length=200)
    education = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50, choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')])
    description = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.job.title}"
    
class TrainingVideo(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='training_videos/')
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


################ended career page ####

################# services page ##################

class Service(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    image = models.ImageField(upload_to='images/services/', null=True)
    bannerimage = models.ImageField(upload_to='images/services', null=True)
    decimage = models.ImageField(upload_to='images/services', null=True)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Service.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


##########end serverices page ######################

############# Contact form ########

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
class ContactBanner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/contact', null=True)

##### end Contact form ##############