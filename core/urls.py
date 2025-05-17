from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.poster, name='poster'),
    path('about/', views.aboutview, name='about'),
    path('careers/', views.careers_view, name='careers'),
    path('careers/<int:job_id>/', views.job_detail_view, name='job_detail'),
    path('careers/thanks/', views.career_thanks_view, name='career_thanks'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('contact/', views.contact_view, name='contact'),

    ]
