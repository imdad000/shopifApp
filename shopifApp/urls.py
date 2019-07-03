from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import cutomer_page,edit_customer,edit_customer_page
from Allorder.views import create_product
urlpatterns = [
	url(r'^$', cutomer_page),
	url(r'^Allorders/$',create_product),
    url(r'^editcustomer/(?P<customer_id>\d+)/$',edit_customer),
    url(r'^editcustomerpage/(?P<customer_id>\d+)/$', edit_customer_page),
    url(r'^admin/', admin.site.urls),
]
