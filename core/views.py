from django.shortcuts import render, redirect
from .models import PosterView, OurStory, AboutBanner, AboutUs, AboutDeals, Service, ContactBanner

from django.contrib import messages
from .forms import ContactForm

# Create your views here.



def poster(request):
    banners = PosterView.objects.all()
    stories = OurStory.objects.all()
    services = Service.objects.all()
    return render(request, 'home.html', {'banners': banners, 'stories': stories, 'services':services})

def aboutview(request):
    aboutbanner = AboutBanner.objects.all()
    aboutus = AboutUs.objects.all()
    aboutdeal = AboutDeals.objects.all()

    return render(request, 'aboutus.html', {'aboutbanner': aboutbanner, 'aboutus':aboutus, 'aboutdeals':aboutdeal})

######### Career page view ################
from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, CareerBanner, TrainingVideo
from .forms import JobApplicationForm

def careers_view(request):
    jobs = Job.objects.all()
    career_banner = CareerBanner.objects.all()
    videos = TrainingVideo.objects.all()
    return render(request, 'careers.html', {'jobs': jobs, 'career_banner': career_banner, 'videos':videos })

def job_detail_view(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            return redirect('/careers/thanks/')
    else:
        form = JobApplicationForm()
    return render(request, 'job_detail.html', {'job': job, 'form': form})

def career_thanks_view(request):
    return render(request, 'thank_you.html')  # or 'thanks.html' if that's the actual name






############# end career page view #############

############### Services Page starting ########

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'service_detail.html', {'service': service})


#### end Services page  ###################

############ Contact page details start #############

def contact_view(request):
    contactbanner = ContactBanner.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your message. We'll get back to you soon.")
            return redirect('core:contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'contactbanner':contactbanner})

######### ended contact page #################