from .models import About

def about_processor(request):
    about = About.objects.first()
    context = {
        'about': about
    }
    return context