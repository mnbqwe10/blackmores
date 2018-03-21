from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'hist_price'

urlpatterns = [
    # /hist_price/
    path('', views.index, name='index'),
    #url("", views.index, name='index'),
    # /hist_price/<brand_id>/
    path('<int:brand_id>/', views.detail, name='detail'),
    #url(r'^(<int:poll_id>\d+)/$', views.detail, name='detail'),
    path('name/', views.add_sku, name='add_sku'),
    path('successful/', views.successful, name='successful'),
]
