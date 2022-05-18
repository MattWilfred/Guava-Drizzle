from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import DataForm

from .models import Data, DataB


# Create your views here.

#def index(response):
    #return render(response, 'myapp/home.html')

def index(request):
    return render(request, 'myapp/landing_page.html')

def home(request):
    return render(request, 'myapp/home.html')

def aboutus(request):
    return render(request, 'myapp/aboutus.html')

def contactus(request):
    return render(request, 'myapp/contactus.html')

#def home(response):
  #  if response.method == "POST":
      #  print(response.POST)
       # if response.POST.get("option-cb") == '1':
          #  return render(response,"myapp/base.html",{"method":1})
       # if response.POST.get("option-cb") == '2':
           # return render(response,"myapp/base.html",{"method":2})

    #return render(response, "myapp/base.html",{})

def predictcrop(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('predictedcrops')
    else:
        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'myapp/predictcrop.html', context)

def predictedcrops(request):
    predicted_crops = Data.objects.all()
    context={
        'predicted_crops': predicted_crops
    }
    return render(request, 'myapp/predictedcrops.html', context)

def checkoptimal(request):
    return render(request, 'myapp/checkoptimal.html')

def information_page(request):
    return render(request, 'myapp/information_page.html')