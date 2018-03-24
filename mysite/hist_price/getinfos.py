from .models import Brand, Item

def add_sku_method(sku):
    gnc = Brand.objects.get(id=1)
    gnc.item_set.create(pid=int(sku),name='new item', url='http://www.gnc.com', size='100 caps', regular_price='9.99')
    gnc.save()
