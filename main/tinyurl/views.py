from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UrlForm
from .models import Urls

# Create your views here.

def tinyurl(request):
    form = UrlForm()
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['main_url'])
            form.save()
    return render(request, 'main.html', {'form': form})

def redirect(request, tiny_url):
    url = Urls.objects.get(tiny_url=tiny_url)
    return HttpResponseRedirect(url.main_url)