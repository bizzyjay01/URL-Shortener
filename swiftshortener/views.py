from django.shortcuts import render, redirect
from .models import URL
from .forms import URLForm
import shortuuid
from urllib.parse import urljoin

# Create your views here.
def home(request):
    form = URLForm()
    if request.method=='POST':
        form = URLForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data['long_url']
            short_code = shortuuid.uuid()[:2]
            
            complete_url = f'{request.get_host()}/{short_code}'

            URL.objects.create(long_url=long_url, short_code=short_code)
            return render(request, 'swiftshortener/success.html', {'short_url':complete_url})

    return render(request, 'swiftshortener/home.html', {'form':form})

def redirect_original(request, short_code):
    url = URL.objects.get(short_code=short_code)
    return redirect(url.long_url)