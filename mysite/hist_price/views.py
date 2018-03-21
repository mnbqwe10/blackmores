from django.shortcuts import render, get_object_or_404
from .models import Brand

from django.http import HttpResponseRedirect
from .forms import SKUForm
# Create your views here.
def index(request):
    all_brands = Brand.objects.all()
    return render(request, 'hist_price/index.html', {'all_brands': all_brands})


def detail(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    return render(request, 'hist_price/detail.html', {'brand': brand})

def successful(request):
    return render(request, 'hist_price/successful.html')

def add_sku(request):
    if request.method == 'POST':
        form = SKUForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = SKUForm()

    return render(request, 'hist_price/detail.html', {'form': form})
