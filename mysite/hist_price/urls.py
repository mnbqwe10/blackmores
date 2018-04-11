from django.conf.urls import url
# from django.urls import path
# from . import views

app_name = 'hist_price'

# urlpatterns = [
#     # /hist_price/
#     path('', views.index, name='index'),
#     #url("", views.index, name='index'),
#     # /hist_price/<brand_id>/
#     path('<int:brand_id>/', views.detail, name='detail'),
#     #url(r'^(<int:poll_id>\d+)/$', views.detail, name='detail'),
#     path('add_sku/<int:brand_id>/', views.add_sku, name='add_sku'),
#     path('update/<int:brand_id>/', views.update, name='update'),
#     path('successful/', views.successful, name='successful'),
# ]

urlpatterns = [
    url(r'^$', 'hist_price.views.products_list', name='home'),
    url(r'^products/$', 'hist_price.views.products_list', name='products'),
    url(r'^products/(\d+)/$', 'hist_price.views.product_details', name='product'),
    # url(r'^products/(\d+)/refresh/$', 'bloodhound.core.views.product_refresh', name='refresh'),
    # url(r'^hot/$', 'bloodhound.core.views.hot', name='hot'),
    # url(r'^api/', include('bloodhound.api.urls', namespace='api')),
]
