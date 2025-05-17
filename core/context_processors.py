from .models import Service

def services_processor(request):
    return {
        'nav_services': Service.objects.all()
    }
