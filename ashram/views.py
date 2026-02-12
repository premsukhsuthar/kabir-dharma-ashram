from django.shortcuts import render
from .models import Event, DonationInfo, ContactMessage
def home(request):
    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')

def kabir(request):
    return render(request, 'kabir.html')

def ashram_page(request):
    return render(request, 'ashram.html')

def trust(request):
    return render(request, 'trust.html')

def contact(request):
    return render(request, 'contact.html')

from .models import Event

def events(request):
    all_events = Event.objects.all().order_by('date')
    return render(request, 'events.html', {'events': all_events})

from .models import GalleryImage

def gallery(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery.html', {'images': images})

from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')
def donate(request):
    return render(request, 'donate.html')





