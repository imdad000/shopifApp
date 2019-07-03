from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import home_page
from Allorder.views import create_product,customer_detail,cutomer_page,edit_customer,edit_customer_page,webhook_call
urlpatterns = [
	url(r'^$', home_page),
	url(r'^Allorders/$',create_product),
	url(r'^Allcustomer/$',customer_detail),
	url(r'^customerpage/$',cutomer_page),
	url(r'^webhook/$',webhook_call),
    url(r'^editcustomer/(?P<customer_id>\d+)/$',edit_customer),
    url(r'^editcustomerpage/(?P<customer_id>\d+)/$', edit_customer_page),
    url(r'^admin/', admin.site.urls),
]
