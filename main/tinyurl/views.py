from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from .forms import UrlForm
from .models import Urls

# Create your views here.

def tinyurl(request, tiny_url = None):
    if tiny_url:
        url = Urls.objects.get(tiny_url=tiny_url)
        return HttpResponseRedirect(url.main_url)
    
    form = UrlForm()
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError:
                pass
            url = Urls.objects.get(main_url=form.cleaned_data['main_url'])
            domain = request.META['HTTP_HOST']
            print(domain, url.tiny_url)
            return render(request, 'main.html', {'tiny_url': url.tiny_url, 'domain': domain})

    return render(request, 'main.html', {'form': form})

