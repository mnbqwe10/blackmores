# from django.shortcuts import render, get_object_or_404
# from .models import Brand, Item, PriceHistory
# import datetime
# 
# from django.http import HttpResponseRedirect
# from .forms import SKUForm
# 
# # from getinfos import add_sku_method
# 
# # Create your views here.
# def index(request):
#     all_brands = Brand.objects.all()
#     return render(request, 'hist_price/index.html', {'all_brands': all_brands})
# 
# 
# def detail(request, brand_id):
#     brand = get_object_or_404(Brand, pk=brand_id)
#     return render(request, 'hist_price/detail.html', {'brand': brand})
# 
# def successful(request):
#     return render(request, 'hist_price/successful.html')
# 
# def add_sku(request, brand_id):
# #    brand = get_object_or_404(Brand, pk=brand_id)
#  #   if request.method == 'POST':
#   #      form = SKUForm(request.POST)
#    #     if form.is_valid():
#     #        add_sku = form.cleaned_data['add_sku']
#      #       add_sku_methond(add_sku)
#       #      return render(request, 'hist_price/detail.html', {'brand': brand})
#    # else:
#     #    form = SKUForm()
#     brand = get_object_or_404(Brand, pk=brand_id)
#     try:
#         input_sku = request.POST['add_sku']
#         brand.item_set.create(pid=int(input_sku),name='new',size='10c',retailprice='9.9',url='gnc.com')
#         brand.save()
#     except(KeyError):
#         return render(request, 'hist_price/detail.html', {'brand': brand,'error_message': "Incorrect Input"})
# 
#     else:
#         return render(request, 'hist_price/detail.html', {'brand': brand})
# 
# def add_sku_method(sku):
#     gnc = Brand.objects.get(pk=1)
#     gnc.item_set.create(pid=int(sku), name='new', size='10caps', regularprice='9.9', url='www.gnc.com')
#     gnc.save()
# 
# def get_current_price(pid):
#     return float(pid)/1000.0
# 
# def update(request, brand_id):
#     brand = get_object_or_404(Brand, pk=brand_id)
#     for item in Item.objects.all():
#         if item.brand.name == 'GNC':
#             current_price = get_current_price(item.pid)
#             time_tag = datetime.datetime.now().strftime("%Y-%m-%d")
#             PriceHistory.objects.create(item=item, price=current_price, date=time_tag)
#     return render(request, 'hist_price/detail.html', {'brand': brand})
# coding: utf-8

import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse as r
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from hist_price.models import Item
from hist_price.crawler.crawler import BlackmoresCrawler


def products_list(request):
    queryset = Item.objects.filter(status=Item.OK)
    # queryset = Item.objects.all()
    querystring = request.GET.get('q')
    if querystring:
        queryset = queryset.filter(Q(name__icontains=querystring) | Q(pid__icontains=querystring))

    default_order = 'price_percentage_variance'
    order = request.GET.get('o', default_order)
    if order not in ['name', '-name', 
                     'pid', '-pid',
                     'current_price', '-current_price', 
                     'price_changes', '-price_changes', 
                     'price_percentage_variance', '-price_percentage_variance', 
                     # 'visited_at', '-visited_at',
                     ]:
        order = default_order
    queryset = queryset.order_by(order)

    paginator = Paginator(queryset, 100)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    sorting_labels = {
        'name': 'Name (a - z)',
        '-name': 'Name (z - a)',
        'price_percentage_variance': 'Greater prices decreases',
        '-price_percentage_variance': 'Greater prices increases',
        'current_price': 'Lowest prices',
        '-current_price': 'Highest prices',
        '-price_changes': 'Most variances',
        # '-visited_at': 'Recently visited',
    }

    label_sort_by = sorting_labels[order]

    return render(request, 'hist_price/products_list.html', {
            'products': products, 
            'order': order, 
            'querystring': querystring,
            'label_sort_by': label_sort_by
        })

def product_details(request, code):
    try:
        product = Item.objects.get(pid=int(code))
    except Item.DoesNotExist:
        # crawler = BlackmoresCrawler()
        # product = Item(pid=code)
        # product = crawler.howl(product)
        pass

    if product.status == Item.OK:
        price_history_chart = product.price_history.all().order_by('created_at')
        return render(request, 'hist_price/product_details.html', {
                'product': product,
                'price_history_chart': price_history_chart
            })
    else:
        # messages.error(request, u'Product with code {0} was not found.'.format(code))
        return redirect(r('home'))

# @require_POST
# def product_refresh(request, code):
#     try:
#         product = Product.objects.get(code=code)
#         crawler = hist_price()
#         crawler.howl(product)
#         return redirect(r('product', args=(code,)))
#     except Product.DoesNotExist:
#         messages.error(request, u'Product with code {0} was not found.'.format(code))
#         return redirect(r('home'))
#
# def hot(request):
#     today = datetime.datetime.today()
#     today = datetime.datetime(today.year, today.month, today.day)
#     products = Product.objects.filter(status=Product.OK, price_percentage_variance__lt=0.0, updated_at__gt=today).order_by('price_percentage_variance')
#     return render(request, 'core/hot.html', {
#             'products': products
#         })

