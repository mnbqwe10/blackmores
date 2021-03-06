from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'hist_price'

urlpatterns = [
    # /hist_price/
    path('', views.index, name='index'),

    # /hist_price/<brand_id>/
    path('<int:brand_id>/', views.detail, name='detail')
]
