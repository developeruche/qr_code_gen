from django.shortcuts import render, redirect
from .forms import CreateQrCode
from .models import QrDetails

# Create your views here.
def HomeView(request):
    if(request.method == 'POST'):
        form = CreateQrCode(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('list')
    else:
        form = CreateQrCode()
    return render(request, 'home.html', {
        'form': form
    })

def QrList(request):
    list_of_qrs = QrDetails.objects.all()
    return render(request, 'list.html', {
        'list': list_of_qrs
    })
