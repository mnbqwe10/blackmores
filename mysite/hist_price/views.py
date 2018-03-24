from django.shortcuts import render, get_object_or_404
from .models import Brand, Item

from django.http import HttpResponseRedirect
from .forms import SKUForm

# from getinfos import add_sku_method

# Create your views here.
def index(request):
    all_brands = Brand.objects.all()
    return render(request, 'hist_price/index.html', {'all_brands': all_brands})


def detail(request, brand_id):
    brand = get_object_or_404(Brand, pk=brand_id)
    return render(request, 'hist_price/detail.html', {'brand': brand})

def successful(request):
    return render(request, 'hist_price/successful.html')

def add_sku(request, brand_id):
#    brand = get_object_or_404(Brand, pk=brand_id)
 #   if request.method == 'POST':
  #      form = SKUForm(request.POST)
   #     if form.is_valid():
    #        add_sku = form.cleaned_data['add_sku']
     #       add_sku_methond(add_sku)
      #      return render(request, 'hist_price/detail.html', {'brand': brand})
   # else:
    #    form = SKUForm()
    brand = get_object_or_404(Brand, pk=brand_id)
    try:
        input_sku = request.POST['add_sku']
        brand.item_set.create(pid=int(input_sku),name='new',size='10c',retailprice='9.9',url='gnc.com')
        brand.save()
    except(KeyError):
        return render(request, 'hist_price/detail.html', {'brand': brand,'error_message': "Incorrect Input"})

    else:
        return render(request, 'hist_price/detail.html', {'brand': brand})

def add_sku_method(sku):
    gnc = Brand.objects.get(pk=1)
    gnc.item_set.create(pid=int(sku), name='new', size='10caps', regularprice='9.9', url='www.gnc.com')
    gnc.save()
